/**
 * TownRenderer - Procedural 3D rendering for roads, buildings, vehicles, and districts.
 */
class TownRenderer {
  constructor(scene) {
    this.scene = scene;
    this.buildingGroup = new THREE.Group();
    this.roadGroup = new THREE.Group();
    this.vehicleGroup = new THREE.Group();
    this.decorGroup = new THREE.Group();
    
    this.scene.add(this.roadGroup);
    this.scene.add(this.buildingGroup);
    this.scene.add(this.vehicleGroup);
    this.scene.add(this.decorGroup);

    this.vehicleMeshes = new Map();
    this.buildingMeshes = new Map();
    this.interactiveObjects = [];

    this._createTerrain();
  }

  _createTerrain() {
    // Cyber Grid Floor
    const gridHelper = new THREE.GridHelper(500, 100, 0x00f0ff, 0x1e293b);
    gridHelper.position.y = 0.02;
    this.scene.add(gridHelper);

    // Deep Dark Base Ground
    const groundGeo = new THREE.PlaneGeometry(600, 600);
    const groundMat = new THREE.MeshStandardMaterial({
      color: 0x070b14,
      roughness: 0.9,
      metalness: 0.1
    });
    const ground = new THREE.Mesh(groundGeo, groundMat);
    ground.rotation.x = -Math.PI / 2;
    ground.receiveShadow = true;
    this.scene.add(ground);

    // District Boundary Circles
    const districts = [
      { name: "Silicon Central", center: [0, 0], radius: 55, color: 0x00f0ff },
      { name: "Innovation Matrix", center: [100, 100], radius: 65, color: 0xa855f7 },
      { name: "Residential Quarter", center: [-100, 80], radius: 70, color: 0x22c55e },
      { name: "Cyber Commons", center: [-80, -90], radius: 60, color: 0xeab308 },
      { name: "Industrial Sector", center: [90, -100], radius: 65, color: 0xf97316 },
    ];

    districts.forEach(d => {
      const ringGeo = new THREE.RingGeometry(d.radius - 1, d.radius, 64);
      const ringMat = new THREE.MeshBasicMaterial({
        color: d.color,
        side: THREE.DoubleSide,
        transparent: true,
        opacity: 0.35
      });
      const ring = new THREE.Mesh(ringGeo, ringMat);
      ring.rotation.x = -Math.PI / 2;
      ring.position.set(d.center[0], 0.05, d.center[1]);
      this.decorGroup.add(ring);
    });
  }

  renderRoads(roads) {
    // Clear old roads
    while (this.roadGroup.children.length > 0) {
      this.roadGroup.remove(this.roadGroup.children[0]);
    }

    roads.forEach(road => {
      const sx = road.start[0], sz = road.start[1];
      const ex = road.end[0], ez = road.end[1];
      const dx = ex - sx;
      const dz = ez - sz;
      const length = Math.hypot(dx, dz);
      if (length < 1) return;

      const angle = Math.atan2(dx, dz);
      const midX = (sx + ex) / 2;
      const midZ = (sz + ez) / 2;

      // Road Surface
      const roadGeo = new THREE.PlaneGeometry(road.width || 6.0, length);
      const roadMat = new THREE.MeshStandardMaterial({
        color: 0x0f172a,
        roughness: 0.7,
        metalness: 0.3
      });
      const roadMesh = new THREE.Mesh(roadGeo, roadMat);
      roadMesh.rotation.x = -Math.PI / 2;
      roadMesh.rotation.z = -angle;
      roadMesh.position.set(midX, 0.08, midZ);
      roadMesh.receiveShadow = true;
      this.roadGroup.add(roadMesh);

      // Glowing Center Line
      const lineGeo = new THREE.PlaneGeometry(0.4, length);
      const lineMat = new THREE.MeshBasicMaterial({
        color: 0x00f0ff,
        transparent: true,
        opacity: 0.7
      });
      const lineMesh = new THREE.Mesh(lineGeo, lineMat);
      lineMesh.rotation.x = -Math.PI / 2;
      lineMesh.rotation.z = -angle;
      lineMesh.position.set(midX, 0.1, midZ);
      this.roadGroup.add(lineMesh);
    });
  }

  renderBuildings(buildings) {
    buildings.forEach(b => {
      if (this.buildingMeshes.has(b.id)) {
        return; // Already rendered
      }

      const [w, h, d] = b.size;
      const [x, y, z] = b.position;
      const group = new THREE.Group();
      group.position.set(x, 0, z);

      const colorHex = parseInt(b.color.replace('#', '0x'), 16) || 0x00f0ff;

      if (b.type === "Tech Tower") {
        // High-rise Tower
        const bodyGeo = new THREE.BoxGeometry(w, h, d);
        const bodyMat = new THREE.MeshStandardMaterial({
          color: 0x091428,
          roughness: 0.2,
          metalness: 0.8
        });
        const body = new THREE.Mesh(bodyGeo, bodyMat);
        body.position.y = h / 2;
        body.castShadow = true;
        body.receiveShadow = true;
        group.add(body);

        // Neon Edge Wireframe
        const wireGeo = new THREE.EdgesGeometry(bodyGeo);
        const wireMat = new THREE.LineBasicMaterial({ color: colorHex, linewidth: 2 });
        const wire = new THREE.LineSegments(wireGeo, wireMat);
        wire.position.y = h / 2;
        group.add(wire);

        // Roof Spire / Beacon
        const spireGeo = new THREE.CylinderGeometry(0.2, 1.2, 12, 8);
        const spireMat = new THREE.MeshBasicMaterial({ color: colorHex });
        const spire = new THREE.Mesh(spireGeo, spireMat);
        spire.position.y = h + 6;
        group.add(spire);

      } else if (b.type === "AI Research Lab") {
        // Hexagonal / Dome Complex
        const baseGeo = new THREE.CylinderGeometry(w / 1.7, w / 1.5, h * 0.8, 8);
        const baseMat = new THREE.MeshStandardMaterial({ color: 0x1e1035, roughness: 0.3, metalness: 0.7 });
        const base = new THREE.Mesh(baseGeo, baseMat);
        base.position.y = (h * 0.8) / 2;
        group.add(base);

        // Glowing Core Dome
        const domeGeo = new THREE.SphereGeometry(w / 2.2, 16, 16, 0, Math.PI * 2, 0, Math.PI / 2);
        const domeMat = new THREE.MeshBasicMaterial({ color: colorHex, wireframe: true });
        const dome = new THREE.Mesh(domeGeo, domeMat);
        dome.position.y = h * 0.8;
        group.add(dome);

      } else if (b.type === "Holo Park") {
        // Green Grass Base
        const lawnGeo = new THREE.BoxGeometry(w, 0.4, d);
        const lawnMat = new THREE.MeshStandardMaterial({ color: 0x064e3b, roughness: 0.8 });
        const lawn = new THREE.Mesh(lawnGeo, lawnMat);
        lawn.position.y = 0.2;
        group.add(lawn);

        // Cyber Trees
        for (let i = 0; i < 4; i++) {
          const tx = (Math.random() - 0.5) * (w * 0.6);
          const tz = (Math.random() - 0.5) * (d * 0.6);
          const trunkGeo = new THREE.CylinderGeometry(0.3, 0.5, 4, 6);
          const trunkMat = new THREE.MeshStandardMaterial({ color: 0x334155 });
          const trunk = new THREE.Mesh(trunkGeo, trunkMat);
          trunk.position.set(tx, 2, tz);
          group.add(trunk);

          const canopyGeo = new THREE.IcosahedronGeometry(1.8, 1);
          const canopyMat = new THREE.MeshBasicMaterial({ color: 0x10b981, wireframe: true });
          const canopy = new THREE.Mesh(canopyGeo, canopyMat);
          canopy.position.set(tx, 4.5, tz);
          group.add(canopy);
        }

      } else {
        // Standard Modern Modular Building
        const boxGeo = new THREE.BoxGeometry(w, h, d);
        const boxMat = new THREE.MeshStandardMaterial({
          color: 0x111827,
          roughness: 0.4,
          metalness: 0.6
        });
        const box = new THREE.Mesh(boxGeo, boxMat);
        box.position.y = h / 2;
        box.castShadow = true;
        box.receiveShadow = true;
        group.add(box);

        // Accent Frame
        const edges = new THREE.EdgesGeometry(boxGeo);
        const line = new THREE.LineSegments(edges, new THREE.LineBasicMaterial({ color: colorHex }));
        line.position.y = h / 2;
        group.add(line);
      }

      // Metadata for raycasting
      group.userData = { type: 'building', data: b };
      group.children.forEach(c => {
        c.userData = { type: 'building', data: b };
        this.interactiveObjects.push(c);
      });

      this.buildingGroup.add(group);
      this.buildingMeshes.set(b.id, group);
    });
  }

  renderVehicles(vehicles) {
    vehicles.forEach(v => {
      let vehObj = this.vehicleMeshes.get(v.id);
      if (!vehObj) {
        // Create 3D Vehicle Model
        const group = new THREE.Group();
        const colorHex = parseInt(v.color.replace('#', '0x'), 16) || 0x00f0ff;

        // Chassis
        const bodyGeo = new THREE.BoxGeometry(3.0, 1.0, 5.0);
        const bodyMat = new THREE.MeshStandardMaterial({
          color: 0x0f172a,
          roughness: 0.2,
          metalness: 0.9
        });
        const body = new THREE.Mesh(bodyGeo, bodyMat);
        body.position.y = 0.5;
        group.add(body);

        // Cockpit Canopy
        const canopyGeo = new THREE.BoxGeometry(2.4, 0.8, 2.5);
        const canopyMat = new THREE.MeshBasicMaterial({ color: colorHex, wireframe: true });
        const canopy = new THREE.Mesh(canopyGeo, canopyMat);
        canopy.position.set(0, 1.2, -0.4);
        group.add(canopy);

        // Headlights (Front Neon)
        const lightGeo = new THREE.BoxGeometry(2.2, 0.2, 0.2);
        const lightMat = new THREE.MeshBasicMaterial({ color: 0x00f0ff });
        const light = new THREE.Mesh(lightGeo, lightMat);
        light.position.set(0, 0.6, 2.55);
        group.add(light);

        // Taillights (Rear Red)
        const tailGeo = new THREE.BoxGeometry(2.2, 0.2, 0.2);
        const tailMat = new THREE.MeshBasicMaterial({ color: 0xf43f5e });
        const tail = new THREE.Mesh(tailGeo, tailMat);
        tail.position.set(0, 0.6, -2.55);
        group.add(tail);

        group.userData = { type: 'vehicle', data: v };
        group.children.forEach(c => {
          c.userData = { type: 'vehicle', data: v };
          this.interactiveObjects.push(c);
        });

        this.vehicleGroup.add(group);
        this.vehicleMeshes.set(v.id, group);
        vehObj = group;
      }

      // Smooth Position & Rotation Interpolation
      const [tx, ty, tz] = v.position;
      vehObj.position.lerp(new THREE.Vector3(tx, ty, tz), 0.15);

      if (v.target) {
        const dx = v.target[0] - tx;
        const dz = v.target[2] - tz;
        if (Math.hypot(dx, dz) > 0.5) {
          const targetAngle = Math.atan2(dx, dz);
          vehObj.rotation.y = targetAngle;
        }
      }
      vehObj.userData.data = v;
    });
  }
}
