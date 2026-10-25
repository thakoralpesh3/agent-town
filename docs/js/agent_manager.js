/**
 * AgentManager - Handles 200+ 3D Agent Avatars, animations, and overhead nameplates.
 */
class AgentManager {
  constructor(scene, camera, nameplateContainer) {
    this.scene = scene;
    this.camera = camera;
    this.nameplateContainer = nameplateContainer;
    this.agentGroup = new THREE.Group();
    this.scene.add(this.agentGroup);

    this.agentMeshes = new Map();
    this.nameplateElements = new Map();
    this.interactiveObjects = [];
    this.selectedAgentId = null;
    this.showLabels = true;
    this.clock = new THREE.Clock();

    // Shared Materials for high performance
    this._initSharedMaterials();
  }

  _initSharedMaterials() {
    this.headGeo = new THREE.SphereGeometry(0.5, 12, 12);
    this.visorGeo = new THREE.CylinderGeometry(0.52, 0.52, 0.2, 12);
    this.torsoGeo = new THREE.CylinderGeometry(0.4, 0.5, 1.2, 8);
    this.ringGeo = new THREE.RingGeometry(0.7, 0.9, 16);
    this.ringGeo.rotateX(-Math.PI / 2);

    this.visorMat = new THREE.MeshBasicMaterial({ color: 0x00f0ff });
    this.headMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.3 });
  }

  updateAgents(agents) {
    const activeIds = new Set();

    agents.forEach(agent => {
      activeIds.add(agent.id);
      let agentObj = this.agentMeshes.get(agent.id);

      if (!agentObj) {
        agentObj = this._createAgentMesh(agent);
        this.agentMeshes.set(agent.id, agentObj);
        this.agentGroup.add(agentObj);
      }

      // Update Agent Data
      agentObj.userData.data = agent;

      // Smooth target interpolation
      const [tx, ty, tz] = agent.position;
      agentObj.userData.targetPos.set(tx, ty, tz);
    });

    // Remove obsolete agents if any
    for (const [id, mesh] of this.agentMeshes.entries()) {
      if (!activeIds.has(id)) {
        this.agentGroup.remove(mesh);
        this.agentMeshes.delete(id);
        const nameplate = this.nameplateElements.get(id);
        if (nameplate) {
          nameplate.remove();
          this.nameplateElements.delete(id);
        }
      }
    }
  }

  _createAgentMesh(agent) {
    const group = new THREE.Group();
    const colorHex = parseInt(agent.color.replace('#', '0x'), 16) || 0x3b82f6;

    // Torso (Role Colored)
    const torsoMat = new THREE.MeshStandardMaterial({
      color: colorHex,
      roughness: 0.4,
      metalness: 0.5
    });
    const torso = new THREE.Mesh(this.torsoGeo, torsoMat);
    torso.position.y = 0.9;
    torso.castShadow = true;
    group.add(torso);

    // Head
    const head = new THREE.Mesh(this.headGeo, this.headMat);
    head.position.y = 1.8;
    head.castShadow = true;
    group.add(head);

    // Visor
    const visor = new THREE.Mesh(this.visorGeo, this.visorMat);
    visor.position.y = 1.8;
    group.add(visor);

    // Ground Neon Ring
    const ringMat = new THREE.MeshBasicMaterial({
      color: colorHex,
      side: THREE.DoubleSide,
      transparent: true,
      opacity: 0.6
    });
    const ring = new THREE.Mesh(this.ringGeo, ringMat);
    ring.position.y = 0.05;
    group.add(ring);

    // Selection Beacon (Hidden by default)
    const beaconGeo = new THREE.ConeGeometry(0.4, 0.8, 4);
    beaconGeo.rotateX(Math.PI);
    const beaconMat = new THREE.MeshBasicMaterial({ color: 0x00f0ff });
    const beacon = new THREE.Mesh(beaconGeo, beaconMat);
    beacon.position.y = 2.8;
    beacon.visible = false;
    beacon.name = "selectionBeacon";
    group.add(beacon);

    // Initial position
    const [x, y, z] = agent.position;
    group.position.set(x, y, z);

    group.userData = {
      type: 'agent',
      data: agent,
      targetPos: new THREE.Vector3(x, y, z),
      beacon: beacon
    };

    group.children.forEach(c => {
      c.userData = group.userData;
      this.interactiveObjects.push(c);
    });

    return group;
  }

  selectAgent(agentId) {
    this.selectedAgentId = agentId;
    this.agentMeshes.forEach((mesh, id) => {
      const beacon = mesh.userData.beacon;
      if (beacon) {
        beacon.visible = (id === agentId);
      }
    });
  }

  animate() {
    const elapsedTime = this.clock.getElapsedTime();
    const tempVec = new THREE.Vector3();

    this.agentMeshes.forEach((mesh, id) => {
      const targetPos = mesh.userData.targetPos;
      const currentPos = mesh.position;

      // Position Lerp
      currentPos.lerp(targetPos, 0.1);

      // Walking Bobbing
      const dist = currentPos.distanceTo(targetPos);
      if (dist > 0.05) {
        mesh.position.y = targetPos.y + Math.abs(Math.sin(elapsedTime * 8)) * 0.2;
        const dx = targetPos.x - currentPos.x;
        const dz = targetPos.z - currentPos.z;
        mesh.rotation.y = Math.atan2(dx, dz);
      } else {
        mesh.position.y = targetPos.y;
      }

      // Animate selection beacon
      if (id === this.selectedAgentId && mesh.userData.beacon) {
        mesh.userData.beacon.rotation.y = elapsedTime * 3;
        mesh.userData.beacon.position.y = 2.8 + Math.sin(elapsedTime * 4) * 0.2;
      }
    });

    this._updateNameplates();
  }

  _updateNameplates() {
    if (!this.showLabels) {
      if (this.nameplateContainer) {
        this.nameplateContainer.style.display = "none";
      }
      return;
    }
    if (this.nameplateContainer) {
      this.nameplateContainer.style.display = "block";
    }

    const tempV = new THREE.Vector3();
    const cameraPos = this.camera.position;

    this.agentMeshes.forEach((mesh, id) => {
      const agent = mesh.userData.data;
      const meshPos = mesh.position;
      const dist = cameraPos.distanceTo(meshPos);

      // Only show nameplates within reasonable viewing distance (e.g. 140 units) or if selected
      const isSelected = (id === this.selectedAgentId);
      const isVisibleDistance = dist < 120;

      let el = this.nameplateElements.get(id);

      if (!isVisibleDistance && !isSelected) {
        if (el) el.style.display = "none";
        return;
      }

      if (!el) {
        el = document.createElement("div");
        el.className = "agent-nameplate";
        this.nameplateContainer.appendChild(el);
        this.nameplateElements.set(id, el);
      }

      el.style.display = "block";
      el.innerHTML = `
        <span>${agent.name}</span>
        <span class="sub-action">${agent.action.substring(0, 24)}</span>
      `;

      // Project 3D position to 2D Screen
      tempV.set(meshPos.x, meshPos.y + 2.5, meshPos.z);
      tempV.project(this.camera);

      // Check if behind camera
      if (tempV.z > 1) {
        el.style.display = "none";
        return;
      }

      const x = (tempV.x * 0.5 + 0.5) * window.innerWidth;
      const y = (-(tempV.y * 0.5) + 0.5) * window.innerHeight;

      el.style.left = `${x}px`;
      el.style.top = `${y}px`;
      el.style.opacity = isSelected ? "1" : Math.max(0.2, 1 - (dist / 140)).toString();
      el.style.borderColor = isSelected ? "var(--cyan-neon)" : "rgba(255, 255, 255, 0.2)";
    });
  }
}
