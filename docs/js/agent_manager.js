/**
 * AgentManager - Realistic 3D Humanoid People Agents for GitHub Tech Town.
 * Features articulate 3D human figures (Head with hair and facial features, Neck, Torso with realistic clothing,
 * articulated Arms and Legs, diverse skin tones and hair styles, natural walking cycles, and overhead status badges).
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

    // Natural Skin Tones Palette
    this.skinTones = [
      0xfde0d7, // Fair
      0xfcd5b8, // Peach Beige
      0xe5b98a, // Olive
      0xc99765, // Warm Tan
      0x8d5b36, // Deep Bronze
      0x51331c  // Rich Espresso
    ];

    // Natural Hair Colors Palette
    this.hairColors = [
      0x171717, // Jet Black
      0x291a10, // Dark Brown
      0x78350f, // Chestnut Auburn
      0xd4af37, // Golden Blonde
      0x94a3b8  // Platinum Silver
    ];

    // Realistic Clothing Colors (Pants/Jeans)
    this.pantColors = [
      0x1e3a8a, // Dark Navy Denim
      0x3b82f6, // Classic Blue Jeans
      0x1e293b, // Charcoal Slacks
      0x334155, // Slate Chinos
      0x0f172a, // Black Trousers
      0xd6d3d1  // Khaki Beige
    ];

    // Footwear Colors
    this.shoeColors = [
      0xf8fafc, // Clean White Sneakers
      0x0f172a, // Black Leather Oxfords
      0x78350f, // Brown Boots
      0x475569  // Grey Athletic Shoes
    ];
  }

  updateAgents(agents) {
    const activeIds = new Set();

    agents.forEach((agent, index) => {
      activeIds.add(agent.id);
      let agentObj = this.agentMeshes.get(agent.id);

      if (!agentObj) {
        agentObj = this._createHumanoidAgentMesh(agent, index);
        this.agentMeshes.set(agent.id, agentObj);
        this.agentGroup.add(agentObj);
      }

      agentObj.userData.data = agent;

      const [tx, ty, tz] = agent.position;
      agentObj.userData.targetPos.set(tx, 0, tz);
    });

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

  _createHumanoidAgentMesh(agent, index) {
    const humanGroup = new THREE.Group();

    // Deterministic random styling based on agent index
    const skinColor = this.skinTones[index % this.skinTones.length];
    const hairColor = this.hairColors[(index * 3) % this.hairColors.length];
    const pantColor = this.pantColors[(index * 2) % this.pantColors.length];
    const shoeColor = this.shoeColors[(index * 5) % this.shoeColors.length];
    
    // Shirt / Jacket color from agent role / company
    const shirtColor = parseInt(agent.color.replace('#', '0x'), 16) || 0x2563eb;

    // Materials
    const skinMat = new THREE.MeshStandardMaterial({ color: skinColor, roughness: 0.6, metalness: 0.05 });
    const hairMat = new THREE.MeshStandardMaterial({ color: hairColor, roughness: 0.8 });
    const shirtMat = new THREE.MeshStandardMaterial({ color: shirtColor, roughness: 0.7 });
    const pantMat = new THREE.MeshStandardMaterial({ color: pantColor, roughness: 0.75 });
    const shoeMat = new THREE.MeshStandardMaterial({ color: shoeColor, roughness: 0.4 });

    // 1. Pelvis / Hips (Root of body)
    const hipsGeo = new THREE.BoxGeometry(0.42, 0.22, 0.26);
    const hips = new THREE.Mesh(hipsGeo, pantMat);
    hips.position.y = 0.95;
    hips.castShadow = true;
    humanGroup.add(hips);

    // 2. Torso & Chest
    const torsoGeo = new THREE.BoxGeometry(0.46, 0.52, 0.28);
    const torso = new THREE.Mesh(torsoGeo, shirtMat);
    torso.position.y = 1.32;
    torso.castShadow = true;
    humanGroup.add(torso);

    // 3. Neck
    const neckGeo = new THREE.CylinderGeometry(0.1, 0.12, 0.15, 8);
    const neck = new THREE.Mesh(neckGeo, skinMat);
    neck.position.y = 1.63;
    humanGroup.add(neck);

    // 4. Head
    const headGroup = new THREE.Group();
    headGroup.position.y = 1.82;

    const headGeo = new THREE.SphereGeometry(0.19, 14, 14);
    const head = new THREE.Mesh(headGeo, skinMat);
    head.castShadow = true;
    headGroup.add(head);

    // Hair Style
    const hairGeo = new THREE.DodecahedronGeometry(0.21, 1);
    const hair = new THREE.Mesh(hairGeo, hairMat);
    hair.position.set(0, 0.06, -0.02);
    headGroup.add(hair);

    // Eyes
    const eyeGeo = new THREE.BoxGeometry(0.04, 0.02, 0.02);
    const eyeMat = new THREE.MeshBasicMaterial({ color: 0x1e293b });
    const leftEye = new THREE.Mesh(eyeGeo, eyeMat);
    leftEye.position.set(0.06, 0.02, 0.18);
    const rightEye = new THREE.Mesh(eyeGeo, eyeMat);
    rightEye.position.set(-0.06, 0.02, 0.18);
    headGroup.add(leftEye);
    headGroup.add(rightEye);

    humanGroup.add(headGroup);

    // 5. Left Arm (Upper Arm, Forearm, Hand)
    const leftArmGroup = new THREE.Group();
    leftArmGroup.position.set(0.3, 1.52, 0);

    const upperArmGeo = new THREE.CylinderGeometry(0.07, 0.065, 0.32, 8);
    const leftUpperArm = new THREE.Mesh(upperArmGeo, shirtMat);
    leftUpperArm.position.y = -0.16;
    leftUpperArm.castShadow = true;
    leftArmGroup.add(leftUpperArm);

    const forearmGeo = new THREE.CylinderGeometry(0.06, 0.055, 0.28, 8);
    const leftForearm = new THREE.Mesh(forearmGeo, skinMat);
    leftForearm.position.y = -0.42;
    leftForearm.castShadow = true;
    leftArmGroup.add(leftForearm);

    const handGeo = new THREE.SphereGeometry(0.05, 8, 8);
    const leftHand = new THREE.Mesh(handGeo, skinMat);
    leftHand.position.y = -0.58;
    leftArmGroup.add(leftHand);

    humanGroup.add(leftArmGroup);

    // 6. Right Arm (Upper Arm, Forearm, Hand)
    const rightArmGroup = new THREE.Group();
    rightArmGroup.position.set(-0.3, 1.52, 0);

    const rightUpperArm = new THREE.Mesh(upperArmGeo, shirtMat);
    rightUpperArm.position.y = -0.16;
    rightUpperArm.castShadow = true;
    rightArmGroup.add(rightUpperArm);

    const rightForearm = new THREE.Mesh(forearmGeo, skinMat);
    rightForearm.position.y = -0.42;
    rightForearm.castShadow = true;
    rightArmGroup.add(rightForearm);

    const rightHand = new THREE.Mesh(handGeo, skinMat);
    rightHand.position.y = -0.58;
    rightArmGroup.add(rightHand);

    humanGroup.add(rightArmGroup);

    // 7. Left Leg (Thigh, Calf, Shoe)
    const leftLegGroup = new THREE.Group();
    leftLegGroup.position.set(0.13, 0.88, 0);

    const thighGeo = new THREE.CylinderGeometry(0.09, 0.08, 0.44, 8);
    const leftThigh = new THREE.Mesh(thighGeo, pantMat);
    leftThigh.position.y = -0.22;
    leftThigh.castShadow = true;
    leftLegGroup.add(leftThigh);

    const calfGeo = new THREE.CylinderGeometry(0.075, 0.065, 0.42, 8);
    const leftCalf = new THREE.Mesh(calfGeo, pantMat);
    leftCalf.position.y = -0.62;
    leftCalf.castShadow = true;
    leftLegGroup.add(leftCalf);

    const shoeGeo = new THREE.BoxGeometry(0.14, 0.12, 0.28);
    const leftShoe = new THREE.Mesh(shoeGeo, shoeMat);
    leftShoe.position.set(0, -0.85, 0.05);
    leftShoe.castShadow = true;
    leftLegGroup.add(leftShoe);

    humanGroup.add(leftLegGroup);

    // 8. Right Leg (Thigh, Calf, Shoe)
    const rightLegGroup = new THREE.Group();
    rightLegGroup.position.set(-0.13, 0.88, 0);

    const rightThigh = new THREE.Mesh(thighGeo, pantMat);
    rightThigh.position.y = -0.22;
    rightThigh.castShadow = true;
    rightLegGroup.add(rightThigh);

    const rightCalf = new THREE.Mesh(calfGeo, pantMat);
    rightCalf.position.y = -0.62;
    rightCalf.castShadow = true;
    rightLegGroup.add(rightCalf);

    const rightShoe = new THREE.Mesh(shoeGeo, shoeMat);
    rightShoe.position.set(0, -0.85, 0.05);
    rightShoe.castShadow = true;
    rightLegGroup.add(rightShoe);

    humanGroup.add(rightLegGroup);

    // 9. Floating Pedestal Ground Shadow Decal
    const shadowGeo = new THREE.CircleGeometry(0.4, 16);
    const shadowMat = new THREE.MeshBasicMaterial({ color: 0x000000, transparent: true, opacity: 0.35 });
    const shadowMesh = new THREE.Mesh(shadowGeo, shadowMat);
    shadowMesh.rotation.x = -Math.PI / 2;
    shadowMesh.position.y = 0.02;
    humanGroup.add(shadowMesh);

    // 10. Selection Ring Indicator
    const ringGeo = new THREE.RingGeometry(0.55, 0.65, 24);
    const ringMat = new THREE.MeshBasicMaterial({ color: 0x00f0ff, side: THREE.DoubleSide });
    const ring = new THREE.Mesh(ringGeo, ringMat);
    ring.rotation.x = -Math.PI / 2;
    ring.position.y = 0.04;
    ring.visible = false;
    ring.name = "selectionRing";
    humanGroup.add(ring);

    // Initial position
    const [x, y, z] = agent.position;
    humanGroup.position.set(x, 0, z);

    humanGroup.userData = {
      type: 'agent',
      data: agent,
      targetPos: new THREE.Vector3(x, 0, z),
      leftArm: leftArmGroup,
      rightArm: rightArmGroup,
      leftLeg: leftLegGroup,
      rightLeg: rightLegGroup,
      head: headGroup,
      ring: ring,
      animPhase: Math.random() * Math.PI * 2
    };

    humanGroup.traverse(child => {
      if (child.isMesh) {
        child.userData = humanGroup.userData;
        this.interactiveObjects.push(child);
      }
    });

    return humanGroup;
  }

  selectAgent(agentId) {
    this.selectedAgentId = agentId;
    this.agentMeshes.forEach((mesh, id) => {
      const ring = mesh.userData.ring;
      if (ring) {
        ring.visible = (id === agentId);
      }
    });
  }

  animate() {
    const time = this.clock.getElapsedTime();

    this.agentMeshes.forEach((mesh, id) => {
      const targetPos = mesh.userData.targetPos;
      const currentPos = mesh.position;

      // Position Lerp
      currentPos.lerp(targetPos, 0.1);

      // Distance to target
      const dx = targetPos.x - currentPos.x;
      const dz = targetPos.z - currentPos.z;
      const dist = Math.hypot(dx, dz);
      const isWalking = dist > 0.08;

      if (isWalking) {
        // Rotate towards movement direction
        const targetAngle = Math.atan2(dx, dz);
        mesh.rotation.y = targetAngle;

        // Realistic Alternating Human Walking Stride Animation
        const walkCycle = Math.sin(time * 10 + mesh.userData.animPhase);

        // Legs swinging forward and backward
        mesh.userData.leftLeg.rotation.x = walkCycle * 0.65;
        mesh.userData.rightLeg.rotation.x = -walkCycle * 0.65;

        // Arms swinging in natural opposition to legs
        mesh.userData.leftArm.rotation.x = -walkCycle * 0.55;
        mesh.userData.rightArm.rotation.x = walkCycle * 0.55;

        // Subtle vertical pelvic bounce
        mesh.position.y = Math.abs(Math.sin(time * 10)) * 0.06;
      } else {
        // Idle Human Breathing & Looking Around
        mesh.position.y = 0;
        mesh.userData.leftLeg.rotation.x = 0;
        mesh.userData.rightLeg.rotation.x = 0;

        // Idle arm posture
        mesh.userData.leftArm.rotation.x = Math.sin(time * 2 + mesh.userData.animPhase) * 0.08;
        mesh.userData.rightArm.rotation.x = -Math.sin(time * 2 + mesh.userData.animPhase) * 0.08;

        // Subtle head turning
        mesh.userData.head.rotation.y = Math.sin(time * 1.2 + mesh.userData.animPhase) * 0.2;
      }

      // Animate selection ring
      if (id === this.selectedAgentId && mesh.userData.ring) {
        mesh.userData.ring.rotation.z = time * 2;
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

      const isSelected = (id === this.selectedAgentId);
      const isVisibleDistance = dist < 110;

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
      const compBadge = agent.company_name ? `<span style="color: #f472b6; font-size: 9px; display: block; font-weight: bold;">🏢 ${agent.company_name}</span>` : '';
      const masterStar = (agent.level >= 8) ? '⭐ ' : '';
      const titleText = agent.career_title || agent.role;
      el.innerHTML = `
        <div style="font-size: 8px; font-weight: 700; color: ${agent.color}; letter-spacing: 0.3px;">${masterStar}LV.${agent.level} • ${titleText}</div>
        <span style="font-weight: 700; font-size: 11px;">${agent.name}</span>
        ${compBadge}
        <span class="sub-action" style="font-size: 9px; color: #38bdf8;">${agent.action.substring(0, 28)}</span>
      `;

      // Project 3D coordinate (over head) to 2D Screen
      tempV.set(meshPos.x, 2.2, meshPos.z);
      tempV.project(this.camera);

      if (tempV.z > 1) {
        el.style.display = "none";
        return;
      }

      const x = (tempV.x * 0.5 + 0.5) * window.innerWidth;
      const y = (-(tempV.y * 0.5) + 0.5) * window.innerHeight;

      el.style.left = `${x}px`;
      el.style.top = `${y}px`;
      el.style.opacity = isSelected ? "1" : Math.max(0.25, 1 - (dist / 130)).toString();
      el.style.borderColor = isSelected ? "#00f0ff" : "rgba(255, 255, 255, 0.25)";
    });
  }
}
