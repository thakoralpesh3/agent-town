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

    this._bindEvents();
  }

  _bindEvents() {
    const dom = this.renderer.domElement;

    dom.addEventListener('pointermove', (e) => {
      this.mouse.x = (e.clientX / window.innerWidth) * 2 - 1;
      this.mouse.y = -(e.clientY / window.innerHeight) * 2 + 1;

      // Hover feedback
      this.raycaster.setFromCamera(this.mouse, this.camera);
      const objects = [...this.agentManager.interactiveObjects, ...this.townRenderer.interactiveObjects];
      const intersects = this.raycaster.intersectObjects(objects);

      if (intersects.length > 0) {
        dom.style.cursor = 'pointer';
      } else {
        dom.style.cursor = 'default';
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
}
