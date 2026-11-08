/**
 * Interaction - Raycasting, mouse selection, click events, and camera targeting.
 */
class InteractionController {
  constructor(camera, scene, renderer, controls, agentManager, townRenderer, ui) {
    this.camera = camera;
    this.scene = scene;
    this.renderer = renderer;
    this.controls = controls;
    this.agentManager = agentManager;
    this.townRenderer = townRenderer;
    this.ui = ui;

    this.raycaster = new THREE.Raycaster();
    this.mouse = new THREE.Vector2();
    this.followedAgent = null;
    this.isFollowing = false;
    this.keys = {};
    this._hoverScheduled = false;

    this._bindEvents();
  }

  _bindEvents() {
    const dom = this.renderer.domElement;

    dom.addEventListener('pointermove', (e) => {
      this.mouse.x = (e.clientX / window.innerWidth) * 2 - 1;
      this.mouse.y = -(e.clientY / window.innerHeight) * 2 + 1;

      // Throttled hover feedback
      if (!this._hoverScheduled) {
        this._hoverScheduled = true;
        requestAnimationFrame(() => {
          this._hoverScheduled = false;
          this.raycaster.setFromCamera(this.mouse, this.camera);
          const objects = [...this.agentManager.interactiveObjects, ...this.townRenderer.interactiveObjects];
          const intersects = this.raycaster.intersectObjects(objects);
          dom.style.cursor = intersects.length > 0 ? 'pointer' : 'default';
        });
      }
    });

    dom.addEventListener('click', (e) => {
      this.mouse.x = (e.clientX / window.innerWidth) * 2 - 1;
      this.mouse.y = -(e.clientY / window.innerHeight) * 2 + 1;

      this.raycaster.setFromCamera(this.mouse, this.camera);
      const objects = [...this.agentManager.interactiveObjects, ...this.townRenderer.interactiveObjects];
      const intersects = this.raycaster.intersectObjects(objects);

      if (intersects.length > 0) {
        // Prioritize clicking agent meshes inside rooms over exterior building shells
        const agentHit = intersects.find(i => i.object.userData && i.object.userData.type === 'agent');
        const hit = agentHit ? agentHit.object : intersects[0].object;
        if (hit.userData) {
          this.handleSelection(hit.userData.data, hit.userData.type);
        }
      }
    });

    // Keyboard Navigation & Hotkeys
    window.addEventListener('keydown', (e) => {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
      this.keys[e.key.toLowerCase()] = true;

      if (e.key === 'f' || e.key === 'F') {
        this.toggleFollow();
      } else if (e.key === 'l' || e.key === 'L') {
        if (this.agentManager) this.agentManager.toggleLabels();
      } else if (e.key === '1') {
        document.getElementById('cam-iso')?.click();
      } else if (e.key === '2') {
        document.getElementById('cam-top')?.click();
      } else if (e.key === '3') {
        document.getElementById('cam-street')?.click();
      } else if (e.key === 'n' || e.key === 'N') {
        document.getElementById('btn-day-night')?.click();
      } else if (e.key === ' ' || e.code === 'Space') {
        e.preventDefault();
        document.getElementById('btn-trigger-tick')?.click();
      } else if (e.key === 'Escape') {
        if (this.ui) this.ui.closeInspector();
        document.getElementById('search-hud')?.classList.remove('mobile-open');
        this.ui?.closeModal?.();
      } else if (e.key === '/') {
        e.preventDefault();
        const searchHud = document.getElementById('search-hud');
        const searchInput = document.getElementById('agent-search-input');
        if (searchHud && searchInput) {
          searchHud.classList.add('mobile-open');
          searchInput.focus();
          searchInput.select();
        }
      }
    });

    window.addEventListener('keyup', (e) => {
      this.keys[e.key.toLowerCase()] = false;
    });
  }

  handleSelection(data, type) {
    if (type === 'agent') {
      this.agentManager.selectAgent(data.id);
      const mesh = this.agentManager.agentMeshes.get(data.id);
      const liveData = mesh?.userData?.data || data;
      this.ui.showAgentInspector(liveData);
      const isSleeping = (liveData.schedule_state === 'SLEEPING') || (liveData.work_mode === 'SLEEPING') || (window.app && window.app.isNightMode);
      const bldgId = isSleeping ? liveData.home_building_id : liveData.workplace_id;
      if (bldgId && this.townRenderer) {
        this.townRenderer.focusBuildingInterior(bldgId);
      }
      const focusPos = mesh ? [mesh.position.x, mesh.position.y, mesh.position.z] : liveData.position;
      this.focusOnPosition(focusPos, 14);
    } else if (type === 'building') {
      this.ui.showBuildingInspector(data);
      if (this.townRenderer) {
        this.townRenderer.focusBuildingInterior(data.id);
      }
      this.focusOnPosition(data.position, 28);
    } else if (type === 'vehicle') {
      this.ui.showVehicleInspector(data);
      this.focusOnPosition(data.position, 20);
    }
  }

  focusOnPosition(pos, distance = 30) {
    const [x, y, z] = pos;
    const targetVec = new THREE.Vector3(x, y, z);
    
    // Smooth OrbitControls target transition
    const startTarget = this.controls.target.clone();
    const startCam = this.camera.position.clone();
    const endCam = new THREE.Vector3(x + distance * 0.7, y + distance * 0.6, z + distance * 0.7);

    let progress = 0;
    const duration = 30; // frames

    const animateTransition = () => {
      progress++;
      const t = progress / duration;
      const ease = t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t;

      this.controls.target.lerpVectors(startTarget, targetVec, ease);
      this.camera.position.lerpVectors(startCam, endCam, ease);
      this.controls.update();

      if (progress < duration) {
        requestAnimationFrame(animateTransition);
      }
    };
    animateTransition();
  }

  startFollowing(agent) {
    this.followedAgent = agent;
    this.isFollowing = true;
    this.ui.updateFollowButton(true);
  }

  stopFollowing() {
    this.followedAgent = null;
    this.isFollowing = false;
    this.ui.updateFollowButton(false);
  }

  toggleFollow() {
    if (this.isFollowing) {
      this.stopFollowing();
    } else if (this.agentManager.selectedAgentId) {
      const mesh = this.agentManager.agentMeshes.get(this.agentManager.selectedAgentId);
      if (mesh && mesh.userData.data) {
        this.startFollowing(mesh.userData.data);
      }
    }
  }

  updateFollowCam() {
    if (!this.isFollowing || !this.followedAgent) return;
    const mesh = this.agentManager.agentMeshes.get(this.followedAgent.id);
    if (!mesh) return;

    const [ax, ay, az] = [mesh.position.x, mesh.position.y, mesh.position.z];
    this.controls.target.set(ax, ay + 1.2, az);
    
    // Maintain smooth follow distance
    const offset = new THREE.Vector3(12, 10, 12);
    this.camera.position.lerp(new THREE.Vector3(ax + offset.x, ay + offset.y, az + offset.z), 0.05);
    this.controls.update();
  }

  updateKeyboardNavigation() {
    if (this.isFollowing) return;
    const moveSpeed = 1.3;
    const forward = new THREE.Vector3();
    this.camera.getWorldDirection(forward);
    forward.y = 0;
    forward.normalize();
    const right = new THREE.Vector3();
    right.crossVectors(this.camera.up, forward).negate().normalize();

    let moved = false;
    if (this.keys['w'] || this.keys['arrowup']) {
      this.camera.position.addScaledVector(forward, moveSpeed);
      this.controls.target.addScaledVector(forward, moveSpeed);
      moved = true;
    }
    if (this.keys['s'] || this.keys['arrowdown']) {
      this.camera.position.addScaledVector(forward, -moveSpeed);
      this.controls.target.addScaledVector(forward, -moveSpeed);
      moved = true;
    }
    if (this.keys['a'] || this.keys['arrowleft']) {
      this.camera.position.addScaledVector(right, -moveSpeed);
      this.controls.target.addScaledVector(right, -moveSpeed);
      moved = true;
    }
    if (this.keys['d'] || this.keys['arrowright']) {
      this.camera.position.addScaledVector(right, moveSpeed);
      this.controls.target.addScaledVector(right, moveSpeed);
      moved = true;
    }
    if (this.keys['q']) {
      this.camera.position.y += moveSpeed * 0.8;
      this.controls.target.y += moveSpeed * 0.8;
      moved = true;
    }
    if (this.keys['e']) {
      this.camera.position.y = Math.max(2, this.camera.position.y - moveSpeed * 0.8);
      this.controls.target.y = Math.max(0, this.controls.target.y - moveSpeed * 0.8);
      moved = true;
    }
    if (moved) {
      this.controls.update();
    }
  }
}
