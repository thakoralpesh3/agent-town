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

    this.isInteriorMode = false;
    this.focusedBuildingId = null;
    this.interiorMaterials = this._createInteriorMaterials();

    // Cache procedural textures
    this.textures = this._createProceduralTextures();

    this._createRealisticTerrain();
  }

  _createInteriorMaterials() {
    return {
      carpetRes: new THREE.MeshStandardMaterial({
        color: 0x1e293b,
        roughness: 0.9,
        metalness: 0.1
      }),
      floorTile: new THREE.MeshStandardMaterial({
        color: 0x334155,
        roughness: 0.4,
        metalness: 0.2
      }),
      woodDesk: new THREE.MeshStandardMaterial({
        color: 0x78350f,
        roughness: 0.6,
        metalness: 0.1
      }),
      metalLeg: new THREE.MeshStandardMaterial({
        color: 0x94a3b8,
        roughness: 0.2,
        metalness: 0.85
      }),
      chairBlack: new THREE.MeshStandardMaterial({
        color: 0x0f172a,
        roughness: 0.7,
        metalness: 0.3
      }),
      pcTower: new THREE.MeshStandardMaterial({
        color: 0x090d16,
        roughness: 0.3,
        metalness: 0.7
      }),
      screenGlowCyan: new THREE.MeshStandardMaterial({
        color: 0x00f0ff,
        emissive: 0x00f0ff,
        emissiveIntensity: 0.85,
        roughness: 0.2
      }),
      screenGlowAmber: new THREE.MeshStandardMaterial({
        color: 0xf59e0b,
        emissive: 0xf59e0b,
        emissiveIntensity: 0.75,
        roughness: 0.2
      }),
      keyboardMat: new THREE.MeshStandardMaterial({
        color: 0x1e293b,
        roughness: 0.5,
        metalness: 0.5
      }),
      blueprintCyan: new THREE.MeshStandardMaterial({
        color: 0x0284c7,
        emissive: 0x0369a1,
        emissiveIntensity: 0.3,
        roughness: 0.8
      }),
      paperWhite: new THREE.MeshStandardMaterial({
        color: 0xf8fafc,
        roughness: 0.9
      }),
      stylusNeon: new THREE.MeshStandardMaterial({
        color: 0x06b6d4,
        emissive: 0x06b6d4,
        emissiveIntensity: 0.6,
        roughness: 0.3
      }),
      bedFrameWood: new THREE.MeshStandardMaterial({
        color: 0x451a03,
        roughness: 0.6
      }),
      mattressBedding: new THREE.MeshStandardMaterial({
        color: 0x2563eb,
        roughness: 0.8
      }),
      pillowWhite: new THREE.MeshStandardMaterial({
        color: 0xffffff,
        roughness: 0.95
      }),
      nightLampGlow: new THREE.MeshStandardMaterial({
        color: 0xfef08a,
        emissive: 0xfef08a,
        emissiveIntensity: 0.9,
        roughness: 0.1
      }),
      holoBeacon: new THREE.MeshStandardMaterial({
        color: 0x00f0ff,
        emissive: 0x00f0ff,
        emissiveIntensity: 0.6,
        transparent: true,
        opacity: 0.65
      }),
      labSteel: new THREE.MeshStandardMaterial({
        color: 0xe2e8f0,
        roughness: 0.2,
        metalness: 0.9
      }),
      labGlassGlow: new THREE.MeshStandardMaterial({
        color: 0x38bdf8,
        emissive: 0x38bdf8,
        emissiveIntensity: 0.5,
        transparent: true,
        opacity: 0.75
      })
    };
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
    // 1. Lush Green City Turf (National Territory 900x900)
    const groundGeo = new THREE.PlaneGeometry(900, 900);
    const groundMat = new THREE.MeshStandardMaterial({
      color: 0x1f3d1b,
      roughness: 0.9,
      metalness: 0.05
    });
    const ground = new THREE.Mesh(groundGeo, groundMat);
    ground.rotation.x = -Math.PI / 2;
    ground.receiveShadow = true;
    this.scene.add(ground);

    // 2. Grand National Plaza Marble Base
    const plazaGeo = new THREE.CylinderGeometry(70, 70, 0.2, 64);
    const plazaMat = new THREE.MeshStandardMaterial({
      color: 0xe2e8f0,
      roughness: 0.45,
      metalness: 0.15
    });
    const plaza = new THREE.Mesh(plazaGeo, plazaMat);
    plaza.position.y = 0.1;
    plaza.receiveShadow = true;
    this.scene.add(plaza);

    // 3. Grand Sovereign Obelisk (Center of National Plaza [0, 0])
    this._createNationalMonumentObelisk(0, 0);

    // 4. Sovereign National Flagpole
    this._createNationalFlagpole(16, -16);

    // 5. Grand Central Plaza Fountain
    this._createPlazaFountain(0, -26);

    // 6. 7 Sovereign Territory District Inlays
    const districts = [
      { name: "Capitol Hill & National Plaza", center: [0, 0], radius: 65, color: 0xf59e0b },
      { name: "Silicon Central Metropolis", center: [0, 110], radius: 70, color: 0x00f0ff },
      { name: "Quantum Science & University Campus", center: [120, 40], radius: 65, color: 0xa855f7 },
      { name: "Health Citadel & Medical Complex", center: [-120, 40], radius: 60, color: 0xef4444 },
      { name: "Cyber Living Townships", center: [-100, -100], radius: 75, color: 0x22c55e },
      { name: "Industrial Harbor & Transit Hub", center: [110, -110], radius: 70, color: 0xf97316 },
      { name: "Biosphere Reserve & Fusion Grid", center: [0, -140], radius: 65, color: 0x10b981 },
    ];

    districts.forEach(d => {
      const ringGeo = new THREE.RingGeometry(d.radius - 1.2, d.radius, 64);
      const ringMat = new THREE.MeshBasicMaterial({
        color: d.color,
        side: THREE.DoubleSide,
        transparent: true,
        opacity: 0.55
      });
      const ring = new THREE.Mesh(ringGeo, ringMat);
      ring.rotation.x = -Math.PI / 2;
      ring.position.set(d.center[0], 0.14, d.center[1]);
      this.scene.add(ring);
    });
  }

  _createNationalMonumentObelisk(x, z) {
    const obeliskGroup = new THREE.Group();
    obeliskGroup.position.set(x, 0, z);

    // Stepped Marble Pedestal
    const step1 = new THREE.Mesh(new THREE.BoxGeometry(14, 0.8, 14), new THREE.MeshStandardMaterial({ color: 0x94a3b8, roughness: 0.4 }));
    step1.position.y = 0.4;
    step1.receiveShadow = true;
    obeliskGroup.add(step1);

    const step2 = new THREE.Mesh(new THREE.BoxGeometry(10, 0.8, 10), new THREE.MeshStandardMaterial({ color: 0xcfd8dc, roughness: 0.4 }));
    step2.position.y = 1.2;
    step2.receiveShadow = true;
    obeliskGroup.add(step2);

    const plinth = new THREE.Mesh(new THREE.BoxGeometry(6.5, 2.5, 6.5), new THREE.MeshStandardMaterial({ color: 0x334155, metalness: 0.3, roughness: 0.5 }));
    plinth.position.y = 2.85;
    plinth.castShadow = true;
    obeliskGroup.add(plinth);

    // 4-sided Tapered Obelisk Shaft (Height 32m)
    const shaftGeo = new THREE.CylinderGeometry(1.6, 3.2, 30, 4);
    const shaftMat = new THREE.MeshStandardMaterial({
      color: 0xe2e8f0,
      roughness: 0.3,
      metalness: 0.2
    });
    const shaft = new THREE.Mesh(shaftGeo, shaftMat);
    shaft.rotation.y = Math.PI / 4; // Align 4 flat faces with axes
    shaft.position.y = 4.1 + 15;
    shaft.castShadow = true;
    obeliskGroup.add(shaft);

    // Golden Pyramidion Apex
    const apexGeo = new THREE.ConeGeometry(2.26, 4.2, 4);
    const apexMat = new THREE.MeshStandardMaterial({
      color: 0xfbbf24,
      emissive: 0xd97706,
      emissiveIntensity: 0.6,
      metalness: 0.95,
      roughness: 0.1
    });
    const apex = new THREE.Mesh(apexGeo, apexMat);
    apex.rotation.y = Math.PI / 4;
    apex.position.y = 4.1 + 30 + 2.1;
    apex.castShadow = true;
    obeliskGroup.add(apex);

    // Vertical Glowing Cybernetic Inscription Runes along each face
    const runeMat = new THREE.MeshBasicMaterial({ color: 0x00f0ff });
    for (let angle = 0; angle < 4; angle++) {
      const rot = (angle * Math.PI) / 2;
      const stripeGeo = new THREE.PlaneGeometry(0.35, 26);
      const stripe = new THREE.Mesh(stripeGeo, runeMat);
      stripe.position.y = 4.1 + 15;
      if (angle === 0) stripe.position.z = 2.4;
      else if (angle === 1) { stripe.position.x = 2.4; stripe.rotation.y = Math.PI / 2; }
      else if (angle === 2) { stripe.position.z = -2.4; stripe.rotation.y = Math.PI; }
      else if (angle === 3) { stripe.position.x = -2.4; stripe.rotation.y = -Math.PI / 2; }
      obeliskGroup.add(stripe);
    }

    const monumentData = {
      id: "monument-001",
      name: "Grand Sovereign Obelisk",
      type: "National Monument",
      district: "Capitol Hill & National Plaza",
      position: [x, 18, z],
      size: [14, 38, 14],
      color: "#f59e0b",
      builder_name: "Leonardo Cyber",
      builder_id: "agent-018",
      purpose: "Sovereign Monument celebrating 320 autonomous citizens and perpetual Git immutability",
      floors: 1,
      capacity: 100,
      departments: ["National Memorial", "Genesis Rune Chamber"],
      amenities: ["Golden Pyramidion Beacon", "Quantum Cyber-Inscribed Runes", "Ceremonial Steps"],
      power_consumption_mw: 0.5,
      security_level: "Level 1 - Public National Monument",
      maintenance_status: "Perpetual Optimal",
      occupants: []
    };

    obeliskGroup.userData = { type: 'building', data: monumentData };
    obeliskGroup.children.forEach(c => {
      c.userData = { type: 'building', data: monumentData };
      this.interactiveObjects.push(c);
    });

    this.streetFurnitureGroup.add(obeliskGroup);
    this.buildingMeshes.set("monument-001", obeliskGroup);
  }

  _createNationalFlagpole(x, z) {
    const flagGroup = new THREE.Group();
    flagGroup.position.set(x, 0, z);

    // Marble Base
    const base = new THREE.Mesh(new THREE.CylinderGeometry(1.5, 1.8, 0.8, 16), new THREE.MeshStandardMaterial({ color: 0x475569 }));
    base.position.y = 0.4;
    flagGroup.add(base);

    // Tall Chrome Pole (20m)
    const pole = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.22, 22, 16), new THREE.MeshStandardMaterial({ color: 0xe2e8f0, metalness: 0.95, roughness: 0.1 }));
    pole.position.y = 11.4;
    pole.castShadow = true;
    flagGroup.add(pole);

    // Gold Finial Sphere
    const finial = new THREE.Mesh(new THREE.SphereGeometry(0.4, 16, 16), new THREE.MeshStandardMaterial({ color: 0xfbbf24, metalness: 0.9, roughness: 0.2 }));
    finial.position.y = 22.6;
    flagGroup.add(finial);

    // Flag Canvas Texture
    const fCanvas = document.createElement('canvas');
    fCanvas.width = 256;
    fCanvas.height = 160;
    const fctx = fCanvas.getContext('2d');
    fctx.fillStyle = '#0f172a';
    fctx.fillRect(0, 0, 256, 160);
    // Cyan stripe
    fctx.fillStyle = '#00f0ff';
    fctx.fillRect(0, 0, 256, 24);
    fctx.fillRect(0, 136, 256, 24);
    // Gold emblem shield in center
    fctx.fillStyle = '#f59e0b';
    fctx.beginPath();
    fctx.arc(128, 80, 36, 0, Math.PI * 2);
    fctx.fill();
    fctx.fillStyle = '#0f172a';
    fctx.font = 'bold 22px Rajdhani, sans-serif';
    fctx.textAlign = 'center';
    fctx.fillText('TECH', 128, 76);
    fctx.fillText('TOWN', 128, 96);

    const flagTex = new THREE.CanvasTexture(fCanvas);
    const flagGeo = new THREE.PlaneGeometry(6.5, 4.0, 12, 6);
    // Subtle wave
    const flagMat = new THREE.MeshStandardMaterial({
      map: flagTex,
      side: THREE.DoubleSide,
      roughness: 0.5
    });
    const flag = new THREE.Mesh(flagGeo, flagMat);
    flag.position.set(3.4, 20.0, 0);
    flag.castShadow = true;
    flagGroup.add(flag);

    this.streetFurnitureGroup.add(flagGroup);
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

      if (b.type === "Sovereign Capitol Building") {
        // Grand Sovereign Capitol & Parliament (Neoclassical-Futuristic Rotunda)
        // Main podium base & ceremonial steps
        const baseGeo = new THREE.BoxGeometry(w, 4, d);
        const marbleMat = new THREE.MeshStandardMaterial({ color: 0xf1f5f9, roughness: 0.35, metalness: 0.1 });
        const baseMesh = new THREE.Mesh(baseGeo, marbleMat);
        baseMesh.position.y = 2;
        baseMesh.castShadow = true;
        baseMesh.receiveShadow = true;
        group.add(baseMesh);

        // Main Parliamentary Building Body
        const bodyHeight = h * 0.55;
        const bodyGeo = new THREE.BoxGeometry(w * 0.9, bodyHeight, d * 0.9);
        const bodyMesh = new THREE.Mesh(bodyGeo, marbleMat);
        bodyMesh.position.y = 4 + bodyHeight / 2;
        bodyMesh.castShadow = true;
        bodyMesh.receiveShadow = true;
        group.add(bodyMesh);

        // Classical Front Portico Colonnade (6 Stately Columns)
        const colGeo = new THREE.CylinderGeometry(0.8, 0.9, bodyHeight, 16);
        const colMat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.25 });
        for (let i = -2.5; i <= 2.5; i += 1) {
          const col = new THREE.Mesh(colGeo, colMat);
          col.position.set(i * (w * 0.14), 4 + bodyHeight / 2, (d * 0.45) + 1.2);
          col.castShadow = true;
          group.add(col);
        }

        // Triangular Pediment over Portico
        const pedGeo = new THREE.ConeGeometry(w * 0.45, 5, 4);
        pedGeo.rotateY(Math.PI / 4);
        const goldMat = new THREE.MeshStandardMaterial({ color: 0xfbbf24, metalness: 0.85, roughness: 0.2 });
        const ped = new THREE.Mesh(pedGeo, goldMat);
        ped.position.set(0, 4 + bodyHeight + 2.5, (d * 0.45) + 1.2);
        group.add(ped);

        // Central Rotunda Cylindrical Drum
        const drumHeight = h * 0.25;
        const drumRadius = w * 0.28;
        const drumGeo = new THREE.CylinderGeometry(drumRadius, drumRadius, drumHeight, 32);
        const drum = new THREE.Mesh(drumGeo, marbleMat);
        drum.position.y = 4 + bodyHeight + drumHeight / 2;
        drum.castShadow = true;
        group.add(drum);

        // Grand Golden Dome
        const domeGeo = new THREE.SphereGeometry(drumRadius * 1.05, 32, 16, 0, Math.PI * 2, 0, Math.PI / 2);
        const dome = new THREE.Mesh(domeGeo, goldMat);
        dome.position.y = 4 + bodyHeight + drumHeight;
        dome.castShadow = true;
        group.add(dome);

        // Lantern Cupola & Golden Sovereign Spire
        const spireGeo = new THREE.CylinderGeometry(0.2, 0.6, 6, 8);
        const spire = new THREE.Mesh(spireGeo, goldMat);
        spire.position.y = 4 + bodyHeight + drumHeight + (drumRadius * 1.05) + 3;
        group.add(spire);

      } else if (b.type === "Supreme Court of Justice") {
        // Supreme Court of Justice (Stately Pillared Courthouse)
        const baseGeo = new THREE.BoxGeometry(w, 3, d);
        const marbleMat = new THREE.MeshStandardMaterial({ color: 0xf8fafc, roughness: 0.3 });
        const baseMesh = new THREE.Mesh(baseGeo, marbleMat);
        baseMesh.position.y = 1.5;
        group.add(baseMesh);

        const bodyGeo = new THREE.BoxGeometry(w * 0.85, h * 0.65, d * 0.85);
        const bodyMesh = new THREE.Mesh(bodyGeo, marbleMat);
        bodyMesh.position.y = 3 + (h * 0.65) / 2;
        bodyMesh.castShadow = true;
        group.add(bodyMesh);

        // Perimeter Classical Pillars
        const colGeo = new THREE.CylinderGeometry(0.7, 0.8, h * 0.65, 12);
        const colMat = new THREE.MeshStandardMaterial({ color: 0xe2e8f0 });
        for (let i = -3; i <= 3; i += 2) {
          const col = new THREE.Mesh(colGeo, colMat);
          col.position.set(i * (w * 0.12), 3 + (h * 0.65) / 2, (d * 0.42) + 0.8);
          group.add(col);
        }

        // Roof Pediment with Golden Scales of Justice Sign
        const roofGeo = new THREE.ConeGeometry(w * 0.5, 4.5, 4);
        roofGeo.rotateY(Math.PI / 4);
        const roof = new THREE.Mesh(roofGeo, new THREE.MeshStandardMaterial({ color: 0xd97706, metalness: 0.7 }));
        roof.position.set(0, 3 + (h * 0.65) + 2.25, 0);
        group.add(roof);

      } else if (b.type === "National Central Bank & Treasury") {
        // Fortified Ziggurat Vault with Golden Inlays
        const steps = 4;
        for (let s = 0; s < steps; s++) {
          const sw = w * (1 - s * 0.12);
          const sd = d * (1 - s * 0.12);
          const sh = h / steps;
          const sGeo = new THREE.BoxGeometry(sw, sh, sd);
          const sMat = new THREE.MeshStandardMaterial({
            color: s % 2 === 0 ? 0x1e293b : 0x334155,
            metalness: 0.6,
            roughness: 0.4
          });
          const tier = new THREE.Mesh(sGeo, sMat);
          tier.position.y = s * sh + sh / 2;
          tier.castShadow = true;
          group.add(tier);

          // Golden Accent Trims
          const trimGeo = new THREE.BoxGeometry(sw + 0.4, 0.6, sd + 0.4);
          const trimMat = new THREE.MeshStandardMaterial({ color: 0xfbbf24, metalness: 0.95, roughness: 0.1 });
          const trim = new THREE.Mesh(trimGeo, trimMat);
          trim.position.y = (s + 1) * sh;
          group.add(trim);
        }

      } else if (b.type === "National Hospital & Nanomedical Citadel" || b.type === "Cybernetic Clinic") {
        // Modern White Medical Citadel with Glowing Red Cross & Helipad
        const bodyGeo = new THREE.BoxGeometry(w, h * 0.85, d);
        const medMat = new THREE.MeshStandardMaterial({ color: 0xf8fafc, roughness: 0.25 });
        const body = new THREE.Mesh(bodyGeo, medMat);
        body.position.y = (h * 0.85) / 2;
        body.castShadow = true;
        group.add(body);

        // Cantilever Cross Wing
        const wingGeo = new THREE.BoxGeometry(w * 1.15, h * 0.35, d * 0.7);
        const wing = new THREE.Mesh(wingGeo, new THREE.MeshStandardMaterial({ color: 0xe2e8f0 }));
        wing.position.y = (h * 0.85) * 0.55;
        group.add(wing);

        // Glowing 3D Red Cross Insignia on Facade
        const crossMat = new THREE.MeshBasicMaterial({ color: 0xef4444 });
        const crossV = new THREE.Mesh(new THREE.BoxGeometry(1.4, 5.0, 0.4), crossMat);
        crossV.position.set(0, (h * 0.85) * 0.7, (d / 2) + 0.3);
        group.add(crossV);
        const crossH = new THREE.Mesh(new THREE.BoxGeometry(5.0, 1.4, 0.4), crossMat);
        crossH.position.set(0, (h * 0.85) * 0.7, (d / 2) + 0.3);
        group.add(crossH);

        // Rooftop Helipad
        const heliBase = new THREE.Mesh(new THREE.CylinderGeometry(w * 0.35, w * 0.35, 0.4, 24), new THREE.MeshStandardMaterial({ color: 0x334155 }));
        heliBase.position.y = (h * 0.85) + 0.2;
        group.add(heliBase);
        const heliRing = new THREE.Mesh(new THREE.RingGeometry(w * 0.25, w * 0.28, 24), new THREE.MeshBasicMaterial({ color: 0xfacc15, side: THREE.DoubleSide }));
        heliRing.rotation.x = -Math.PI / 2;
        heliRing.position.y = (h * 0.85) + 0.42;
        group.add(heliRing);

      } else if (b.type === "Grand Astronomical Observatory") {
        // Cylindrical Observatory Tower with Rotating Hemispherical Dome
        const towerGeo = new THREE.CylinderGeometry(w * 0.42, w * 0.48, h * 0.7, 32);
        const towerMat = new THREE.MeshStandardMaterial({ color: 0x475569, roughness: 0.5 });
        const tower = new THREE.Mesh(towerGeo, towerMat);
        tower.position.y = (h * 0.7) / 2;
        tower.castShadow = true;
        group.add(tower);

        // Half-Sphere Dome
        const domeGeo = new THREE.SphereGeometry(w * 0.45, 32, 16, 0, Math.PI * 2, 0, Math.PI / 2);
        const domeMat = new THREE.MeshStandardMaterial({ color: 0x94a3b8, metalness: 0.8, roughness: 0.2 });
        const dome = new THREE.Mesh(domeGeo, domeMat);
        dome.position.y = h * 0.7;
        dome.castShadow = true;
        group.add(dome);

        // Telescope Barrel pointing upward at 45 degrees
        const scopeGeo = new THREE.CylinderGeometry(0.8, 1.1, 8, 16);
        const scopeMat = new THREE.MeshStandardMaterial({ color: 0x0284c7, metalness: 0.9, roughness: 0.1 });
        const scope = new THREE.Mesh(scopeGeo, scopeMat);
        scope.rotation.x = Math.PI / 4;
        scope.position.set(0, (h * 0.7) + (w * 0.28), w * 0.18);
        group.add(scope);

      } else if (b.type === "Tokamak Fusion Reactor Station" || b.type === "Solar Fusion Array") {
        // Heavy Containment Bunker + Roof Magnetic Torus Coil
        const bunkerGeo = new THREE.BoxGeometry(w, h * 0.65, d);
        const bunkerMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.7 });
        const bunker = new THREE.Mesh(bunkerGeo, bunkerMat);
        bunker.position.y = (h * 0.65) / 2;
        bunker.castShadow = true;
        group.add(bunker);

        // Magnetic Torus Ring
        const torusGeo = new THREE.TorusGeometry(w * 0.32, 2.0, 16, 32);
        const torusMat = new THREE.MeshStandardMaterial({ color: 0xbe123c, metalness: 0.85, roughness: 0.2 });
        const torus = new THREE.Mesh(torusGeo, torusMat);
        torus.rotation.x = Math.PI / 2;
        torus.position.y = (h * 0.65) + 2.5;
        group.add(torus);

        // Glowing Pulsing Plasma Core Sphere
        const plasmaGeo = new THREE.SphereGeometry(w * 0.18, 16, 16);
        const plasmaMat = new THREE.MeshBasicMaterial({ color: 0xef4444 });
        const plasma = new THREE.Mesh(plasmaGeo, plasmaMat);
        plasma.position.y = (h * 0.65) + 2.5;
        group.add(plasma);

      } else if (b.type === "Hydroponic Agricultural Biodome") {
        // Translucent Green Geodesic Biodome
        const baseGeo = new THREE.CylinderGeometry(w * 0.52, w * 0.52, 2, 32);
        const baseMesh = new THREE.Mesh(baseGeo, new THREE.MeshStandardMaterial({ color: 0x334155 }));
        baseMesh.position.y = 1;
        group.add(baseMesh);

        // Geodesic Glass Dome
        const domeGeo = new THREE.SphereGeometry(w * 0.5, 24, 16, 0, Math.PI * 2, 0, Math.PI / 2);
        const domeMat = new THREE.MeshStandardMaterial({
          color: 0x22c55e,
          transparent: true,
          opacity: 0.65,
          roughness: 0.1,
          metalness: 0.3
        });
        const dome = new THREE.Mesh(domeGeo, domeMat);
        dome.position.y = 2;
        dome.castShadow = true;
        group.add(dome);

        // Interior Spiraling Aeroponics Plant Columns
        for (let i = 0; i < 4; i++) {
          const colGeo = new THREE.CylinderGeometry(0.8, 0.8, h * 0.6, 8);
          const colMat = new THREE.MeshStandardMaterial({ color: 0x15803d, roughness: 0.8 });
          const plantCol = new THREE.Mesh(colGeo, colMat);
          const a = (i * Math.PI) / 2;
          plantCol.position.set(Math.cos(a) * (w * 0.22), (h * 0.6) / 2 + 2, Math.sin(a) * (w * 0.22));
          group.add(plantCol);
        }

      } else if (b.type === "Autonomous Vehicle Mega-Plant" || b.type === "Hyperloop Central Terminus" || b.type === "Drone Logistics Freight Port") {
        // Industrial Manufacturing Facility with Gantry Trusses
        const factoryGeo = new THREE.BoxGeometry(w, h * 0.7, d);
        const factoryMat = new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 0.6, metalness: 0.4 });
        const factory = new THREE.Mesh(factoryGeo, factoryMat);
        factory.position.y = (h * 0.7) / 2;
        factory.castShadow = true;
        group.add(factory);

        // Sawtooth / Gantry Roof Truss
        const trussGeo = new THREE.BoxGeometry(w * 0.95, 3.5, d * 0.95);
        const trussMat = new THREE.MeshStandardMaterial({ color: 0xf59e0b, metalness: 0.8 });
        const truss = new THREE.Mesh(trussGeo, trussMat);
        truss.position.y = (h * 0.7) + 1.75;
        group.add(truss);

        // Industrial Warning Stripe Bands
        const stripeGeo = new THREE.BoxGeometry(w + 0.2, 1.2, d + 0.2);
        const stripeMat = new THREE.MeshBasicMaterial({ color: 0xfbbf24 });
        const stripe = new THREE.Mesh(stripeGeo, stripeMat);
        stripe.position.y = (h * 0.7) * 0.45;
        group.add(stripe);

      } else if (b.type === "Company Headquarters" || b.company_name) {
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

      } else if (b.type === "Tech Tower" || b.type.includes("Tower") || b.type.includes("Spire") || b.type.includes("Exchange")) {
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

      } else if (b.type.includes("Residential") || b.type.includes("Township")) {
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

      } else if (b.type === "Holo Park" || b.type.includes("Park") || b.type.includes("Reserve")) {
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

      // Collect exterior meshes before adding interior
      const exteriorMeshes = [];
      group.traverse(child => {
        if (child.isMesh) {
          exteriorMeshes.push(child);
        }
      });

      // Build and attach detailed 3D interior
      const interiorGroup = this._buildBuildingInterior(b, w, h, d);
      group.add(interiorGroup);

      group.userData = {
        type: 'building',
        data: b,
        exteriorMeshes: exteriorMeshes,
        interiorGroup: interiorGroup
      };

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

  _buildBuildingInterior(b, w, h, d) {
    const interiorGroup = new THREE.Group();
    const mats = this.interiorMaterials;

    const isResidential = (b.interior_type === "RESIDENTIAL_SUITE") ||
                          (b.name && (b.name.includes("Township") || b.name.includes("Apartment") || b.name.includes("Residences")));

    // 1. Interior Floor Slab
    const floorGeo = new THREE.BoxGeometry(w * 0.86, 0.12, d * 0.86);
    const floorMesh = new THREE.Mesh(floorGeo, isResidential ? mats.carpetRes : mats.floorTile);
    floorMesh.position.y = 0.06;
    floorMesh.receiveShadow = true;
    interiorGroup.add(floorMesh);

    if (isResidential) {
      // Residential Bedroom Suites with Comfortable Beds & Nightstands
      const bedPositions = [
        [-(w * 0.28), 0, -(d * 0.25), 0],
        [(w * 0.28), 0, -(d * 0.25), 0],
        [-(w * 0.28), 0, (d * 0.25), Math.PI],
        [(w * 0.28), 0, (d * 0.25), Math.PI],
      ];

      bedPositions.forEach(([bx, by, bz, rot]) => {
        const bedUnit = this._buildBedUnit(mats);
        bedUnit.position.set(bx, by, bz);
        bedUnit.rotation.y = rot;
        interiorGroup.add(bedUnit);
      });

      // Central Living Room Lounge: Sofa + Coffee Table + Area Rug
      const rugGeo = new THREE.BoxGeometry(3.6, 0.02, 2.4);
      const rug = new THREE.Mesh(rugGeo, new THREE.MeshStandardMaterial({ color: 0x1e3a8a, roughness: 0.9 }));
      rug.position.set(0, 0.13, 0);
      interiorGroup.add(rug);

      const sofaGeo = new THREE.BoxGeometry(2.8, 0.65, 1.1);
      const sofa = new THREE.Mesh(sofaGeo, new THREE.MeshStandardMaterial({ color: 0x0f172a, roughness: 0.7 }));
      sofa.position.set(0, 0.45, 0.8);
      interiorGroup.add(sofa);

      const tableGeo = new THREE.BoxGeometry(1.6, 0.35, 0.8);
      const table = new THREE.Mesh(tableGeo, mats.woodDesk);
      table.position.set(0, 0.3, 0);
      interiorGroup.add(table);

    } else {
      // Workplace / Corporate / Lab Interior:
      // A. Dual-Monitor PC Workstations (Typing Code & Matrix Operations)
      const pcPositions = [
        [-(w * 0.26), 0, -(d * 0.25), 0],
        [(w * 0.26), 0, -(d * 0.25), 0],
        [-(w * 0.26), 0, (d * 0.25), Math.PI],
      ];
      pcPositions.forEach(([px, py, pz, rot]) => {
        const pcStation = this._buildOfficeWorkstation(mats, true, false);
        pcStation.position.set(px, py, pz);
        pcStation.rotation.y = rot;
        interiorGroup.add(pcStation);
      });

      // B. Architectural Drafting & Paper Blueprints Station (Writing on blueprints & charters)
      const paperStation = this._buildOfficeWorkstation(mats, false, true);
      paperStation.position.set(w * 0.26, 0, d * 0.25);
      paperStation.rotation.y = Math.PI;
      interiorGroup.add(paperStation);

      // C. Central Conference / Boardroom Strategy Table with Holographic Projector
      const confTable = this._buildConferenceTable(mats, w, d);
      confTable.position.set(0, 0, 0);
      interiorGroup.add(confTable);

      // D. Laboratory Research Bench if lab/hospital/university
      if (b.interior_type === "LABORATORY" || (b.name && (b.name.includes("Lab") || b.name.includes("Citadel") || b.name.includes("University") || b.name.includes("Foundry")))) {
        const labBench = this._buildLabBench(mats);
        labBench.position.set(0, 0, -(d * 0.35));
        interiorGroup.add(labBench);
      }
    }

    return interiorGroup;
  }

  _buildOfficeWorkstation(mats, hasPC, hasPaper) {
    const ws = new THREE.Group();

    // 1. Sturdy Work Desk Top
    const deskGeo = new THREE.BoxGeometry(2.4, 0.08, 1.2);
    const desk = new THREE.Mesh(deskGeo, mats.woodDesk);
    desk.position.y = 0.75;
    desk.castShadow = true;
    ws.add(desk);

    // 4 Metallic Desk Legs
    const legGeo = new THREE.CylinderGeometry(0.04, 0.04, 0.75, 8);
    const legPositions = [
      [1.05, 0.375, 0.45],
      [-1.05, 0.375, 0.45],
      [1.05, 0.375, -0.45],
      [-1.05, 0.375, -0.45]
    ];
    legPositions.forEach(([lx, ly, lz]) => {
      const leg = new THREE.Mesh(legGeo, mats.metalLeg);
      leg.position.set(lx, ly, lz);
      ws.add(leg);
    });

    // 2. Ergonomic Office Chair
    const seatGeo = new THREE.BoxGeometry(0.55, 0.08, 0.55);
    const seat = new THREE.Mesh(seatGeo, mats.chairBlack);
    seat.position.set(0, 0.48, 0.85);
    ws.add(seat);

    const backGeo = new THREE.BoxGeometry(0.55, 0.52, 0.08);
    const back = new THREE.Mesh(backGeo, mats.chairBlack);
    back.position.set(0, 0.78, 1.08);
    ws.add(back);

    const chairBaseGeo = new THREE.CylinderGeometry(0.04, 0.04, 0.48, 8);
    const chairBase = new THREE.Mesh(chairBaseGeo, mats.metalLeg);
    chairBase.position.set(0, 0.24, 0.85);
    ws.add(chairBase);

    if (hasPC) {
      // 3. Computer Tower under desk
      const towerGeo = new THREE.BoxGeometry(0.24, 0.45, 0.45);
      const tower = new THREE.Mesh(towerGeo, mats.pcTower);
      tower.position.set(0.85, 0.25, -0.2);
      ws.add(tower);

      // 4. Dual Monitors (Left: Cyan Code Screen, Right: Amber Systems Screen)
      const standGeo = new THREE.CylinderGeometry(0.03, 0.03, 0.38, 8);
      const stand = new THREE.Mesh(standGeo, mats.metalLeg);
      stand.position.set(0, 0.98, -0.28);
      ws.add(stand);

      const crossbarGeo = new THREE.BoxGeometry(1.6, 0.04, 0.04);
      const crossbar = new THREE.Mesh(crossbarGeo, mats.metalLeg);
      crossbar.position.set(0, 1.15, -0.28);
      ws.add(crossbar);

      // Left Monitor (IDE / Code in glowing cyan)
      const leftMonGeo = new THREE.BoxGeometry(0.85, 0.52, 0.03);
      const leftMon = new THREE.Mesh(leftMonGeo, mats.screenGlowCyan);
      leftMon.position.set(-0.42, 1.15, -0.25);
      leftMon.rotation.y = 0.18;
      ws.add(leftMon);

      // Right Monitor (Telemetry / Terminal in glowing amber)
      const rightMonGeo = new THREE.BoxGeometry(0.85, 0.52, 0.03);
      const rightMon = new THREE.Mesh(rightMonGeo, mats.screenGlowAmber);
      rightMon.position.set(0.42, 1.15, -0.25);
      rightMon.rotation.y = -0.18;
      ws.add(rightMon);

      // 5. Keyboard with Keys
      const kbGeo = new THREE.BoxGeometry(0.65, 0.02, 0.22);
      const kb = new THREE.Mesh(kbGeo, mats.keyboardMat);
      kb.position.set(0, 0.8, 0.1);
      ws.add(kb);

      // Mouse
      const mouseGeo = new THREE.BoxGeometry(0.08, 0.025, 0.12);
      const mouse = new THREE.Mesh(mouseGeo, mats.chairBlack);
      mouse.position.set(0.45, 0.8, 0.1);
      ws.add(mouse);
    }

    if (hasPaper) {
      // 6. Architectural Blueprint Sheet
      const bpGeo = new THREE.BoxGeometry(1.2, 0.02, 0.8);
      const bp = new THREE.Mesh(bpGeo, mats.blueprintCyan);
      bp.position.set(-0.2, 0.8, 0.05);
      ws.add(bp);

      // 7. Stack of White Paper Documents / Charters
      const paperGeo = new THREE.BoxGeometry(0.4, 0.08, 0.3);
      const papers = new THREE.Mesh(paperGeo, mats.paperWhite);
      papers.position.set(0.75, 0.83, -0.15);
      papers.rotation.y = 0.12;
      ws.add(papers);

      // 8. Rolled Blueprint Scroll
      const scrollGeo = new THREE.CylinderGeometry(0.06, 0.06, 0.65, 12);
      const scroll = new THREE.Mesh(scrollGeo, mats.paperWhite);
      scroll.position.set(0.75, 0.83, 0.25);
      scroll.rotation.z = Math.PI / 2;
      ws.add(scroll);

      // 9. Digital Stylus Drafting Pen
      const penGeo = new THREE.CylinderGeometry(0.015, 0.015, 0.28, 8);
      const pen = new THREE.Mesh(penGeo, mats.stylusNeon);
      pen.position.set(-0.15, 0.82, 0.15);
      pen.rotation.z = Math.PI / 2;
      pen.rotation.y = 0.35;
      ws.add(pen);
    }

    return ws;
  }

  _buildBedUnit(mats) {
    const bed = new THREE.Group();

    // 1. Bed Frame
    const frameGeo = new THREE.BoxGeometry(2.3, 0.35, 1.35);
    const frame = new THREE.Mesh(frameGeo, mats.bedFrameWood);
    frame.position.y = 0.2;
    bed.add(frame);

    // 2. Headboard
    const headboardGeo = new THREE.BoxGeometry(0.12, 0.8, 1.35);
    const headboard = new THREE.Mesh(headboardGeo, mats.bedFrameWood);
    headboard.position.set(-1.1, 0.55, 0);
    bed.add(headboard);

    // 3. Mattress & Bedding Blanket
    const matGeo = new THREE.BoxGeometry(2.15, 0.22, 1.25);
    const mattress = new THREE.Mesh(matGeo, mats.mattressBedding);
    mattress.position.set(0.05, 0.42, 0);
    bed.add(mattress);

    // 4. Soft White Pillow
    const pilGeo = new THREE.BoxGeometry(0.48, 0.12, 0.85);
    const pillow = new THREE.Mesh(pilGeo, mats.pillowWhite);
    pillow.position.set(-0.75, 0.56, 0);
    bed.add(pillow);

    // 5. Beside Nightstand
    const standGeo = new THREE.BoxGeometry(0.55, 0.45, 0.55);
    const stand = new THREE.Mesh(standGeo, mats.bedFrameWood);
    stand.position.set(-0.85, 0.25, 1.05);
    bed.add(stand);

    // 6. Glowing Nightlamp
    const lampStem = new THREE.Mesh(new THREE.CylinderGeometry(0.03, 0.03, 0.25, 8), mats.metalLeg);
    lampStem.position.set(-0.85, 0.58, 1.05);
    bed.add(lampStem);

    const lampShade = new THREE.Mesh(new THREE.SphereGeometry(0.14, 12, 12), mats.nightLampGlow);
    lampShade.position.set(-0.85, 0.74, 1.05);
    bed.add(lampShade);

    return bed;
  }

  _buildConferenceTable(mats, w, d) {
    const conf = new THREE.Group();

    // Table Top
    const tableGeo = new THREE.BoxGeometry(3.8, 0.1, 1.8);
    const table = new THREE.Mesh(tableGeo, mats.woodDesk);
    table.position.y = 0.75;
    conf.add(table);

    // Pedestal Supports
    const p1 = new THREE.Mesh(new THREE.CylinderGeometry(0.25, 0.25, 0.72, 12), mats.metalLeg);
    p1.position.set(-1.1, 0.36, 0);
    conf.add(p1);

    const p2 = new THREE.Mesh(new THREE.CylinderGeometry(0.25, 0.25, 0.72, 12), mats.metalLeg);
    p2.position.set(1.1, 0.36, 0);
    conf.add(p2);

    // 6 Chairs
    const chairOffsets = [
      [-1.1, 0, 1.25, Math.PI],
      [0, 0, 1.25, Math.PI],
      [1.1, 0, 1.25, Math.PI],
      [-1.1, 0, -1.25, 0],
      [0, 0, -1.25, 0],
      [1.1, 0, -1.25, 0],
    ];
    chairOffsets.forEach(([cx, cy, cz, rot]) => {
      const chairSeat = new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.08, 0.5), mats.chairBlack);
      chairSeat.position.set(cx, 0.48, cz);
      const chairBack = new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.5, 0.08), mats.chairBlack);
      chairBack.position.set(cx, 0.76, cz + (rot === 0 ? -0.22 : 0.22));
      conf.add(chairSeat);
      conf.add(chairBack);
    });

    // Central Holographic Projector Beacon
    const beaconBase = new THREE.Mesh(new THREE.CylinderGeometry(0.35, 0.4, 0.08, 16), mats.metalLeg);
    beaconBase.position.y = 0.84;
    conf.add(beaconBase);

    const holoCone = new THREE.Mesh(new THREE.CylinderGeometry(0.08, 0.45, 1.2, 16), mats.holoBeacon);
    holoCone.position.y = 1.48;
    conf.add(holoCone);

    return conf;
  }

  _buildLabBench(mats) {
    const lab = new THREE.Group();

    // Stainless Steel Countertop
    const benchGeo = new THREE.BoxGeometry(3.2, 0.1, 1.0);
    const bench = new THREE.Mesh(benchGeo, mats.labSteel);
    bench.position.y = 0.85;
    lab.add(bench);

    // Legs
    const l1 = new THREE.Mesh(new THREE.BoxGeometry(0.1, 0.85, 0.9), mats.metalLeg);
    l1.position.set(-1.45, 0.425, 0);
    lab.add(l1);
    const l2 = new THREE.Mesh(new THREE.BoxGeometry(0.1, 0.85, 0.9), mats.metalLeg);
    l2.position.set(1.45, 0.425, 0);
    lab.add(l2);

    // Diagnostic Hologram Screen
    const diagGeo = new THREE.BoxGeometry(1.2, 0.65, 0.02);
    const diagScreen = new THREE.Mesh(diagGeo, mats.labGlassGlow);
    diagScreen.position.set(0, 1.35, -0.2);
    lab.add(diagScreen);

    // Sample Rack with Glowing Tubes
    for (let i = -0.4; i <= 0.4; i += 0.2) {
      const tube = new THREE.Mesh(new THREE.CylinderGeometry(0.025, 0.025, 0.25, 8), mats.screenGlowCyan);
      tube.position.set(i, 1.0, 0.2);
      lab.add(tube);
    }

    return lab;
  }

  toggleInteriorMode(forceState) {
    if (typeof forceState === 'boolean') {
      this.isInteriorMode = forceState;
    } else {
      this.isInteriorMode = !this.isInteriorMode;
    }

    this.buildingMeshes.forEach((group, id) => {
      const extMeshes = group.userData.exteriorMeshes || [];
      const interior = group.userData.interiorGroup;
      const isFocused = (this.focusedBuildingId === id);
      const makeTransparent = this.isInteriorMode || isFocused;

      extMeshes.forEach(mesh => {
        if (!mesh.userData.origMaterial) {
          mesh.userData.origMaterial = mesh.material;
        }
        if (makeTransparent) {
          if (!mesh.userData.transparentMat) {
            mesh.userData.transparentMat = mesh.material.clone();
            mesh.userData.transparentMat.transparent = true;
            mesh.userData.transparentMat.opacity = 0.20;
            mesh.userData.transparentMat.depthWrite = false;
          }
          mesh.material = mesh.userData.transparentMat;
        } else {
          mesh.material = mesh.userData.origMaterial;
        }
      });

      if (interior) {
        interior.visible = true;
      }
    });

    return this.isInteriorMode;
  }

  focusBuildingInterior(buildingId) {
    this.focusedBuildingId = buildingId;
    this.toggleInteriorMode(this.isInteriorMode);
  }
}
