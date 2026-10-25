/**
 * TownRenderer - Realistic 3D Urban Environment for GitHub Tech Town.
 * Features realistic asphalt roads with lane markings and crosswalks, concrete sidewalks,
 * high-rise glass curtain-wall skyscrapers with lit windows, modern corporate headquarters,
 * residential complexes with balconies, organic trees, streetlamps, traffic lights, and detailed 3D vehicles.
 */
class TownRenderer {
  constructor(scene) {
    this.scene = scene;
    this.roadGroup = new THREE.Group();
    this.sidewalkGroup = new THREE.Group();
    this.buildingGroup = new THREE.Group();
    this.vehicleGroup = new THREE.Group();
    this.streetFurnitureGroup = new THREE.Group();
    this.natureGroup = new THREE.Group();
    
    this.scene.add(this.roadGroup);
    this.scene.add(this.sidewalkGroup);
    this.scene.add(this.buildingGroup);
    this.scene.add(this.vehicleGroup);
    this.scene.add(this.streetFurnitureGroup);
    this.scene.add(this.natureGroup);

    this.vehicleMeshes = new Map();
    this.buildingMeshes = new Map();
    this.interactiveObjects = [];

    // Cache procedural textures
    this.textures = this._createProceduralTextures();

    this._createRealisticTerrain();
  }

  _createProceduralTextures() {
    // 1. Asphalt Road Texture (with noise and lane markings)
    const asphaltCanvas = document.createElement('canvas');
    asphaltCanvas.width = 512;
    asphaltCanvas.height = 512;
    const actx = asphaltCanvas.getContext('2d');
    
    // Base dark asphalt
    actx.fillStyle = '#1e2229';
    actx.fillRect(0, 0, 512, 512);
    
    // Asphalt grain/gravel noise
    for (let i = 0; i < 40000; i++) {
      const v = Math.floor(Math.random() * 30 + 20);
      actx.fillStyle = `rgb(${v},${v},${v})`;
      actx.fillRect(Math.random() * 512, Math.random() * 512, 1.5, 1.5);
    }
    
    // Double Yellow Center Line
    actx.fillStyle = '#f59e0b';
    actx.fillRect(250, 0, 4, 512);
    actx.fillRect(258, 0, 4, 512);

    // White Outer Dashed Lines
    actx.fillStyle = 'rgba(255, 255, 255, 0.85)';
    for (let y = 0; y < 512; y += 48) {
      actx.fillRect(80, y, 5, 28);
      actx.fillRect(428, y, 5, 28);
    }

    const asphaltTex = new THREE.CanvasTexture(asphaltCanvas);
    asphaltTex.wrapS = THREE.RepeatWrapping;
    asphaltTex.wrapT = THREE.RepeatWrapping;

    // 2. Concrete Sidewalk Tile Texture
    const sidewalkCanvas = document.createElement('canvas');
    sidewalkCanvas.width = 256;
    sidewalkCanvas.height = 256;
    const sctx = sidewalkCanvas.getContext('2d');
    sctx.fillStyle = '#94a3b8';
    sctx.fillRect(0, 0, 256, 256);
    // Subtle noise
    for (let i = 0; i < 8000; i++) {
      const v = Math.floor(Math.random() * 25 + 140);
      sctx.fillStyle = `rgb(${v},${v},${v})`;
      sctx.fillRect(Math.random() * 256, Math.random() * 256, 2, 2);
    }
    // Concrete slabs grid lines
    sctx.strokeStyle = '#64748b';
    sctx.lineWidth = 3;
    sctx.strokeRect(0, 0, 128, 128);
    sctx.strokeRect(128, 0, 128, 128);
    sctx.strokeRect(0, 128, 128, 128);
    sctx.strokeRect(128, 128, 128, 128);
    const sidewalkTex = new THREE.CanvasTexture(sidewalkCanvas);
    sidewalkTex.wrapS = THREE.RepeatWrapping;
    sidewalkTex.wrapT = THREE.RepeatWrapping;

    // 3. High-Rise Glass Skyscraper Facade Texture
    const glassCanvas = document.createElement('canvas');
    glassCanvas.width = 256;
    glassCanvas.height = 512;
    const gctx = glassCanvas.getContext('2d');
    gctx.fillStyle = '#0f172a';
    gctx.fillRect(0, 0, 256, 512);

    // Office Windows Grid
    const cols = 8;
    const rows = 24;
    const wWidth = 256 / cols;
    const wHeight = 512 / rows;

    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        const isLit = Math.random() > 0.35;
        if (isLit) {
          const warm = Math.random() > 0.3 ? '#fef08a' : '#38bdf8';
          gctx.fillStyle = warm;
        } else {
          gctx.fillStyle = '#1e293b';
        }
        gctx.fillRect(c * wWidth + 3, r * wHeight + 3, wWidth - 6, wHeight - 6);
      }
    }
    const glassTex = new THREE.CanvasTexture(glassCanvas);
    glassTex.wrapS = THREE.RepeatWrapping;
    glassTex.wrapT = THREE.RepeatWrapping;

    // 4. Modern Residential Apartment Balcony Texture
    const resCanvas = document.createElement('canvas');
    resCanvas.width = 256;
    resCanvas.height = 256;
    const rctx = resCanvas.getContext('2d');
    rctx.fillStyle = '#e2e8f0';
    rctx.fillRect(0, 0, 256, 256);
    for (let r = 0; r < 6; r++) {
      for (let c = 0; c < 4; c++) {
        // Balcony window & glass rail
        rctx.fillStyle = '#0369a1';
        rctx.fillRect(c * 64 + 8, r * 42 + 6, 48, 22);
        rctx.fillStyle = '#334155';
        rctx.fillRect(c * 64 + 4, r * 42 + 28, 56, 12);
      }
    }
    const resTex = new THREE.CanvasTexture(resCanvas);
    resTex.wrapS = THREE.RepeatWrapping;
    resTex.wrapT = THREE.RepeatWrapping;

    return {
      asphalt: asphaltTex,
      sidewalk: sidewalkTex,
      glass: glassTex,
      residential: resTex
    };
  }

  _createRealisticTerrain() {
    // 1. Lush Green City Turf
    const groundGeo = new THREE.PlaneGeometry(650, 650);
    const groundMat = new THREE.MeshStandardMaterial({
      color: 0x2d5a27,
      roughness: 0.85,
      metalness: 0.05
    });
    const ground = new THREE.Mesh(groundGeo, groundMat);
    ground.rotation.x = -Math.PI / 2;
    ground.receiveShadow = true;
    this.scene.add(ground);

    // 2. Concrete Plaza Central Base
    const plazaGeo = new THREE.CylinderGeometry(60, 60, 0.15, 48);
    const plazaMat = new THREE.MeshStandardMaterial({
      color: 0xcfd8dc,
      roughness: 0.6,
      metalness: 0.1
    });
    const plaza = new THREE.Mesh(plazaGeo, plazaMat);
    plaza.position.y = 0.08;
    plaza.receiveShadow = true;
    this.scene.add(plaza);

    // 3. Central Plaza Fountain
    this._createPlazaFountain(0, 0);

    // 4. District Boundary Ground Inlays
    const districts = [
      { name: "Silicon Central", center: [0, 0], radius: 52, color: 0x0284c7 },
      { name: "Innovation Matrix", center: [100, 100], radius: 62, color: 0x9333ea },
      { name: "Residential Quarter", center: [-100, 80], radius: 65, color: 0x16a34a },
      { name: "Cyber Commons", center: [-80, -90], radius: 58, color: 0xd97706 },
      { name: "Industrial Sector", center: [90, -100], radius: 62, color: 0xe11d48 },
    ];

    districts.forEach(d => {
      const ringGeo = new THREE.RingGeometry(d.radius - 0.8, d.radius, 64);
      const ringMat = new THREE.MeshBasicMaterial({
        color: d.color,
        side: THREE.DoubleSide,
        transparent: true,
        opacity: 0.5
      });
      const ring = new THREE.Mesh(ringGeo, ringMat);
      ring.rotation.x = -Math.PI / 2;
      ring.position.set(d.center[0], 0.12, d.center[1]);
      this.scene.add(ring);
    });
  }

  _createPlazaFountain(x, z) {
    const basinGeo = new THREE.CylinderGeometry(8, 9, 1.2, 32);
    const basinMat = new THREE.MeshStandardMaterial({ color: 0x475569, roughness: 0.5 });
    const basin = new THREE.Mesh(basinGeo, basinMat);
    basin.position.set(x, 0.6, z);
    basin.castShadow = true;
    basin.receiveShadow = true;
    this.streetFurnitureGroup.add(basin);

    // Water surface
    const waterGeo = new THREE.CylinderGeometry(7.8, 7.8, 0.2, 32);
    const waterMat = new THREE.MeshStandardMaterial({
      color: 0x0284c7,
      roughness: 0.1,
      metalness: 0.8,
      transparent: true,
      opacity: 0.85
    });
    const water = new THREE.Mesh(waterGeo, waterMat);
    water.position.set(x, 1.15, z);
    this.streetFurnitureGroup.add(water);

    // Center Spire
    const spireGeo = new THREE.CylinderGeometry(0.8, 1.4, 4, 16);
    const spire = new THREE.Mesh(spireGeo, basinMat);
    spire.position.set(x, 2.5, z);
    spire.castShadow = true;
    this.streetFurnitureGroup.add(spire);
  }

  renderRoads(roads) {
    while (this.roadGroup.children.length > 0) {
      this.roadGroup.remove(this.roadGroup.children[0]);
    }
    while (this.sidewalkGroup.children.length > 0) {
      this.sidewalkGroup.remove(this.sidewalkGroup.children[0]);
    }
    while (this.streetFurnitureGroup.children.length > 0) {
      this.streetFurnitureGroup.remove(this.streetFurnitureGroup.children[0]);
    }

    roads.forEach(road => {
      const sx = road.start[0], sz = road.start[1];
      const ex = road.end[0], ez = road.end[1];
      const dx = ex - sx;
      const dz = ez - sz;
      const length = Math.hypot(dx, dz);
      if (length < 2) return;

      const angle = Math.atan2(dx, dz);
      const midX = (sx + ex) / 2;
      const midZ = (sz + ez) / 2;
      const roadWidth = road.width || 8.0;

      // 1. Realistic Asphalt Road Surface
      const roadGeo = new THREE.PlaneGeometry(roadWidth, length);
      const tex = this.textures.asphalt.clone();
      tex.repeat.set(1, Math.max(1, Math.round(length / 20)));
      tex.needsUpdate = true;

      const roadMat = new THREE.MeshStandardMaterial({
        map: tex,
        roughness: 0.75,
        metalness: 0.15
      });
      const roadMesh = new THREE.Mesh(roadGeo, roadMat);
      roadMesh.rotation.x = -Math.PI / 2;
      roadMesh.rotation.z = -angle;
      roadMesh.position.set(midX, 0.14, midZ);
      roadMesh.receiveShadow = true;
      this.roadGroup.add(roadMesh);

      // 2. Concrete Sidewalks on Both Sides
      const sidewalkWidth = 2.4;
      const offsetDist = (roadWidth / 2) + (sidewalkWidth / 2);
      const perpX = Math.cos(angle) * offsetDist;
      const perpZ = -Math.sin(angle) * offsetDist;

      // Left Sidewalk
      const swGeo = new THREE.BoxGeometry(sidewalkWidth, 0.22, length);
      const swMat = new THREE.MeshStandardMaterial({
        color: 0x94a3b8,
        roughness: 0.7
      });
      const leftSw = new THREE.Mesh(swGeo, swMat);
      leftSw.rotation.y = angle;
      leftSw.position.set(midX + perpX, 0.16, midZ + perpZ);
      leftSw.receiveShadow = true;
      leftSw.castShadow = true;
      this.sidewalkGroup.add(leftSw);

      // Right Sidewalk
      const rightSw = new THREE.Mesh(swGeo, swMat);
      rightSw.rotation.y = angle;
      rightSw.position.set(midX - perpX, 0.16, midZ - perpZ);
      rightSw.receiveShadow = true;
      rightSw.castShadow = true;
      this.sidewalkGroup.add(rightSw);

      // 3. Street Lamps along the sidewalk
      const lampInterval = 32;
      const numLamps = Math.floor(length / lampInterval);
      for (let i = 1; i <= numLamps; i++) {
        const t = (i * lampInterval) / length;
        const lx = sx + dx * t;
        const lz = sz + dz * t;
        this._createStreetLamp(lx + perpX * 1.05, lz + perpZ * 1.05);
        this._createStreetLamp(lx - perpX * 1.05, lz - perpZ * 1.05);

        // Natural Roadside Trees
        if (i % 2 === 0) {
          this._createRealisticTree(lx + perpX * 1.8, lz + perpZ * 1.8);
          this._createRealisticTree(lx - perpX * 1.8, lz - perpZ * 1.8);
        }
      }

      // 4. Crosswalk (Zebra Stripes) at road ends
      this._createCrosswalk(sx, sz, angle, roadWidth);
      this._createCrosswalk(ex, ez, angle, roadWidth);
    });
  }

  _createCrosswalk(x, z, angle, width) {
    const cwGroup = new THREE.Group();
    cwGroup.position.set(x, 0.16, z);
    cwGroup.rotation.y = angle;

    const stripeGeo = new THREE.PlaneGeometry(0.7, 4.0);
    const stripeMat = new THREE.MeshBasicMaterial({ color: 0xffffff });

    const numStripes = 6;
    for (let i = -numStripes / 2; i <= numStripes / 2; i++) {
      const stripe = new THREE.Mesh(stripeGeo, stripeMat);
      stripe.rotation.x = -Math.PI / 2;
      stripe.position.set(i * 1.1, 0, 0);
      cwGroup.add(stripe);
    }
    this.roadGroup.add(cwGroup);
  }

  _createStreetLamp(x, z) {
    const lampGroup = new THREE.Group();
    lampGroup.position.set(x, 0, z);

    // Pole
    const poleGeo = new THREE.CylinderGeometry(0.12, 0.18, 5.5, 8);
    const poleMat = new THREE.MeshStandardMaterial({ color: 0x334155, metalness: 0.8, roughness: 0.3 });
    const pole = new THREE.Mesh(poleGeo, poleMat);
    pole.position.y = 2.75;
    pole.castShadow = true;
    lampGroup.add(pole);

    // Curved Arm & Fixture
    const armGeo = new THREE.BoxGeometry(0.1, 0.1, 1.2);
    const arm = new THREE.Mesh(armGeo, poleMat);
    arm.position.set(0, 5.4, 0.5);
    lampGroup.add(arm);

    // Lantern Head
    const headGeo = new THREE.BoxGeometry(0.35, 0.15, 0.6);
    const headMat = new THREE.MeshStandardMaterial({ color: 0x1e293b });
    const head = new THREE.Mesh(headGeo, headMat);
    head.position.set(0, 5.35, 1.0);
    lampGroup.add(head);

    // Glowing Bulb
    const bulbGeo = new THREE.SphereGeometry(0.16, 8, 8);
    const bulbMat = new THREE.MeshBasicMaterial({ color: 0xfef08a });
    const bulb = new THREE.Mesh(bulbGeo, bulbMat);
    bulb.position.set(0, 5.2, 1.0);
    lampGroup.add(bulb);

    this.streetFurnitureGroup.add(lampGroup);
  }

  _createRealisticTree(x, z) {
    const treeGroup = new THREE.Group();
    treeGroup.position.set(x, 0, z);

    // Tree Trunk (Wood)
    const trunkHeight = 3.5 + Math.random() * 1.5;
    const trunkGeo = new THREE.CylinderGeometry(0.25, 0.45, trunkHeight, 8);
    const trunkMat = new THREE.MeshStandardMaterial({ color: 0x5c4033, roughness: 0.9 });
    const trunk = new THREE.Mesh(trunkGeo, trunkMat);
    trunk.position.y = trunkHeight / 2;
    trunk.castShadow = true;
    treeGroup.add(trunk);

    // Multi-layer Organic Canopy (Oak / Maple Foliage)
    const foliageMat = new THREE.MeshStandardMaterial({
      color: 0x228b22,
      roughness: 0.8,
      flatShading: true
    });

    const canopyLayers = [
      { r: 2.2, y: trunkHeight * 0.8 },
      { r: 1.8, y: trunkHeight * 1.1 },
      { r: 1.3, y: trunkHeight * 1.35 },
    ];

    canopyLayers.forEach(layer => {
      const sphereGeo = new THREE.DodecahedronGeometry(layer.r, 1);
      const foliage = new THREE.Mesh(sphereGeo, foliageMat);
      foliage.position.set(
        (Math.random() - 0.5) * 0.4,
        layer.y,
        (Math.random() - 0.5) * 0.4
      );
      foliage.castShadow = true;
      treeGroup.add(foliage);
    });

    this.natureGroup.add(treeGroup);
  }

  renderBuildings(buildings) {
    buildings.forEach(b => {
      if (this.buildingMeshes.has(b.id)) {
        return;
      }

      const [w, h, d] = b.size;
      const [x, y, z] = b.position;
      const group = new THREE.Group();
      group.position.set(x, 0, z);

      const colorHex = parseInt(b.color.replace('#', '0x'), 16) || 0x0284c7;

      if (b.type === "Company Headquarters" || b.company_name) {
        // High-Rise Modern Glass Corporate Megatower
        const bodyGeo = new THREE.BoxGeometry(w, h, d);
        const tex = this.textures.glass.clone();
        tex.repeat.set(Math.max(1, Math.round(w / 8)), Math.max(1, Math.round(h / 12)));
        tex.needsUpdate = true;

        const bodyMat = new THREE.MeshStandardMaterial({
          map: tex,
          roughness: 0.15,
          metalness: 0.85
        });
        const body = new THREE.Mesh(bodyGeo, bodyMat);
        body.position.y = h / 2;
        body.castShadow = true;
        body.receiveShadow = true;
        group.add(body);

        // Ground Floor Glass Lobby
        const lobbyGeo = new THREE.BoxGeometry(w + 1.2, 5, d + 1.2);
        const lobbyMat = new THREE.MeshStandardMaterial({
          color: 0x1e293b,
          roughness: 0.2,
          metalness: 0.7
        });
        const lobby = new THREE.Mesh(lobbyGeo, lobbyMat);
        lobby.position.y = 2.5;
        group.add(lobby);

        // Rooftop Penthouse & Helipad
        const roofGeo = new THREE.BoxGeometry(w * 0.75, 4, d * 0.75);
        const roofMat = new THREE.MeshStandardMaterial({ color: 0x334155 });
        const roof = new THREE.Mesh(roofGeo, roofMat);
        roof.position.y = h + 2;
        group.add(roof);

        // Helipad Yellow Circle
        const heliGeo = new THREE.RingGeometry(w * 0.2, w * 0.25, 24);
        const heliMat = new THREE.MeshBasicMaterial({ color: 0xfacc15, side: THREE.DoubleSide });
        const heli = new THREE.Mesh(heliGeo, heliMat);
        heli.rotation.x = -Math.PI / 2;
        heli.position.y = h + 4.05;
        group.add(heli);

        // Floating Corporate Sign Billboard
        const signGeo = new THREE.BoxGeometry(w * 0.6, 5, 0.4);
        const signMat = new THREE.MeshStandardMaterial({
          color: colorHex,
          emissive: colorHex,
          emissiveIntensity: 0.6
        });
        const sign = new THREE.Mesh(signGeo, signMat);
        sign.position.y = h + 7.5;
        group.add(sign);

      } else if (b.type === "Tech Tower") {
        // Modern Commercial Skyscraper
        const bodyGeo = new THREE.BoxGeometry(w, h, d);
        const tex = this.textures.glass.clone();
        tex.repeat.set(Math.max(1, Math.round(w / 8)), Math.max(1, Math.round(h / 10)));
        tex.needsUpdate = true;

        const bodyMat = new THREE.MeshStandardMaterial({
          map: tex,
          roughness: 0.2,
          metalness: 0.8
        });
        const body = new THREE.Mesh(bodyGeo, bodyMat);
        body.position.y = h / 2;
        body.castShadow = true;
        body.receiveShadow = true;
        group.add(body);

        // Spire Antenna
        const spireGeo = new THREE.CylinderGeometry(0.15, 0.8, 14, 8);
        const spireMat = new THREE.MeshStandardMaterial({ color: 0x94a3b8, metalness: 0.9 });
        const spire = new THREE.Mesh(spireGeo, spireMat);
        spire.position.y = h + 7;
        group.add(spire);

        // Red Aviation Warning Light
        const beaconGeo = new THREE.SphereGeometry(0.3, 8, 8);
        const beaconMat = new THREE.MeshBasicMaterial({ color: 0xef4444 });
        const beacon = new THREE.Mesh(beaconGeo, beaconMat);
        beacon.position.y = h + 14.2;
        group.add(beacon);

      } else if (b.type === "Residential Pod") {
        // Modern Apartment Complex with Balconies
        const bodyGeo = new THREE.BoxGeometry(w, h, d);
        const tex = this.textures.residential.clone();
        tex.repeat.set(Math.max(1, Math.round(w / 6)), Math.max(1, Math.round(h / 6)));
        tex.needsUpdate = true;

        const bodyMat = new THREE.MeshStandardMaterial({
          map: tex,
          roughness: 0.6,
          metalness: 0.1
        });
        const body = new THREE.Mesh(bodyGeo, bodyMat);
        body.position.y = h / 2;
        body.castShadow = true;
        body.receiveShadow = true;
        group.add(body);

        // Balcony Overhangs
        for (let fl = 1; fl < Math.floor(h / 4); fl++) {
          const balGeo = new THREE.BoxGeometry(w * 0.8, 0.3, 1.2);
          const balMat = new THREE.MeshStandardMaterial({ color: 0x64748b });
          const bal = new THREE.Mesh(balGeo, balMat);
          bal.position.set(0, fl * 4, (d / 2) + 0.6);
          group.add(bal);
        }

      } else if (b.type === "Holo Park") {
        // City Garden / Park with Ponds & Benches
        const lawnGeo = new THREE.BoxGeometry(w, 0.4, d);
        const lawnMat = new THREE.MeshStandardMaterial({ color: 0x15803d, roughness: 0.9 });
        const lawn = new THREE.Mesh(lawnGeo, lawnMat);
        lawn.position.y = 0.2;
        group.add(lawn);

        // Park Trees
        for (let i = 0; i < 5; i++) {
          const tx = (Math.random() - 0.5) * (w * 0.7);
          const tz = (Math.random() - 0.5) * (d * 0.7);
          this._createRealisticTree(x + tx, z + tz);
        }

        // Park Benches
        for (let i = 0; i < 2; i++) {
          const benchGeo = new THREE.BoxGeometry(2.0, 0.5, 0.8);
          const benchMat = new THREE.MeshStandardMaterial({ color: 0x854d0e });
          const bench = new THREE.Mesh(benchGeo, benchMat);
          bench.position.set((i === 0 ? 4 : -4), 0.5, 0);
          group.add(bench);
        }

      } else {
        // Contemporary Architectural Office Building
        const bodyGeo = new THREE.BoxGeometry(w, h, d);
        const bodyMat = new THREE.MeshStandardMaterial({
          color: 0x1e293b,
          roughness: 0.3,
          metalness: 0.7
        });
        const body = new THREE.Mesh(bodyGeo, bodyMat);
        body.position.y = h / 2;
        body.castShadow = true;
        body.receiveShadow = true;
        group.add(body);

        // Accent Window Bands
        const bandGeo = new THREE.BoxGeometry(w + 0.2, h * 0.15, d + 0.2);
        const bandMat = new THREE.MeshStandardMaterial({
          color: colorHex,
          roughness: 0.1,
          metalness: 0.9
        });
        const band = new THREE.Mesh(bandGeo, bandMat);
        band.position.y = h * 0.6;
        group.add(band);
      }

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
        // Detailed 3D Real-World Car Model
        const group = new THREE.Group();
        const colorHex = parseInt(v.color.replace('#', '0x'), 16) || 0x0284c7;

        // 1. Car Lower Chassis / Body
        const chassisGeo = new THREE.BoxGeometry(2.4, 0.7, 4.6);
        const paintMat = new THREE.MeshStandardMaterial({
          color: colorHex,
          roughness: 0.2,
          metalness: 0.85
        });
        const chassis = new THREE.Mesh(chassisGeo, paintMat);
        chassis.position.y = 0.65;
        chassis.castShadow = true;
        group.add(chassis);

        // 2. Car Cabin / Roof with Glass Windows
        const cabinGeo = new THREE.BoxGeometry(2.1, 0.75, 2.6);
        const glassMat = new THREE.MeshStandardMaterial({
          color: 0x0f172a,
          roughness: 0.05,
          metalness: 0.95
        });
        const cabin = new THREE.Mesh(cabinGeo, glassMat);
        cabin.position.set(0, 1.35, -0.2);
        cabin.castShadow = true;
        group.add(cabin);

        // 3. Four Realistic Wheels with Rims
        const wheelGeo = new THREE.CylinderGeometry(0.42, 0.42, 0.35, 16);
        wheelGeo.rotateZ(Math.PI / 2);
        const tireMat = new THREE.MeshStandardMaterial({ color: 0x111827, roughness: 0.9 });
        const rimGeo = new THREE.CylinderGeometry(0.24, 0.24, 0.37, 12);
        rimGeo.rotateZ(Math.PI / 2);
        const rimMat = new THREE.MeshStandardMaterial({ color: 0xd1d5db, metalness: 0.9, roughness: 0.2 });

        const wheelPositions = [
          [1.15, 0.42, 1.3],
          [-1.15, 0.42, 1.3],
          [1.15, 0.42, -1.3],
          [-1.15, 0.42, -1.3],
        ];

        wheelPositions.forEach(([wx, wy, wz]) => {
          const tire = new THREE.Mesh(wheelGeo, tireMat);
          const rim = new THREE.Mesh(rimGeo, rimMat);
          tire.position.set(wx, wy, wz);
          rim.position.set(wx, wy, wz);
          tire.castShadow = true;
          group.add(tire);
          group.add(rim);
        });

        // 4. Realistic Headlights & Taillights
        const headlightGeo = new THREE.BoxGeometry(0.5, 0.2, 0.1);
        const headMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
        const leftHead = new THREE.Mesh(headlightGeo, headMat);
        leftHead.position.set(0.8, 0.7, 2.3);
        const rightHead = new THREE.Mesh(headlightGeo, headMat);
        rightHead.position.set(-0.8, 0.7, 2.3);
        group.add(leftHead);
        group.add(rightHead);

        const taillightGeo = new THREE.BoxGeometry(0.5, 0.18, 0.1);
        const tailMat = new THREE.MeshBasicMaterial({ color: 0xdc2626 });
        const leftTail = new THREE.Mesh(taillightGeo, tailMat);
        leftTail.position.set(0.8, 0.7, -2.3);
        const rightTail = new THREE.Mesh(taillightGeo, tailMat);
        rightTail.position.set(-0.8, 0.7, -2.3);
        group.add(leftTail);
        group.add(rightTail);

        group.userData = { type: 'vehicle', data: v };
        group.children.forEach(c => {
          c.userData = { type: 'vehicle', data: v };
          this.interactiveObjects.push(c);
        });

        this.vehicleGroup.add(group);
        this.vehicleMeshes.set(v.id, group);
        vehObj = group;
      }

      // Smooth Position & Heading
      const [tx, ty, tz] = v.position;
      vehObj.position.lerp(new THREE.Vector3(tx, ty, tz), 0.18);

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
