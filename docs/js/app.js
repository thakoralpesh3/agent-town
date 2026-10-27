/**
 * App - Main 3D WebGL Application entry point.
 * Features realistic atmospheric daylight, ACES Filmic tone mapping, smooth camera controls,
 * real-time agent tracking, and live 24/7 world state synchronization.
 */
class TechTownApp {
  constructor() {
    this.container = document.getElementById("canvas-container");
    this.nameplateContainer = document.getElementById("nameplate-container");
    
    this.scene = null;
    this.camera = null;
    this.renderer = null;
    this.controls = null;
    
    this.townRenderer = null;
    this.agentManager = null;
    this.ui = null;
    this.interaction = null;

    this.isNightMode = false; // Realistic Daylight as primary mode
    this.dirLight = null;
    this.hemiLight = null;
    this.currentState = null;

    this.init();
  }

  init() {
    this._setupScene();
    this._setupLights();
    
    this.townRenderer = new TownRenderer(this.scene);
    this.agentManager = new AgentManager(this.scene, this.camera, this.nameplateContainer);
    this.ui = new UIController();
    this.interaction = new InteractionController(
      this.camera, 
      this.scene, 
      this.renderer, 
      this.controls, 
      this.agentManager, 
      this.townRenderer, 
      this.ui
    );
    this.ui.setControllers(this.interaction, this.agentManager, this.townRenderer);

    this._setupDayNightToggle();
    this._setupAutoRefresh();

    window.addEventListener("resize", () => this._onWindowResize());

    // Fetch initial world state
    this.fetchWorldState();

    // Start render loop
    this._animate();
  }

  _setupScene() {
    this.scene = new THREE.Scene();
    
    // Realistic Atmospheric Daylight Sky
    this.scene.background = new THREE.Color(0x93c5fd);
    this.scene.fog = new THREE.FogExp2(0xbae6fd, 0.0018);

    this.camera = new THREE.PerspectiveCamera(
      45,
      window.innerWidth / window.innerHeight,
      0.5,
      1200
    );
    // Cinematic Isometric Vantage Point
    this.camera.position.set(130, 95, 130);

    this.renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: "high-performance" });
    this.renderer.setSize(window.innerWidth, window.innerHeight);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    
    // Photorealistic Filmic Tone Mapping & Soft Shadows
    this.renderer.toneMapping = THREE.ACESFilmicToneMapping;
    this.renderer.toneMappingExposure = 1.1;
    this.renderer.shadowMap.enabled = true;
    this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    this.container.appendChild(this.renderer.domElement);

    this.controls = new THREE.OrbitControls(this.camera, this.renderer.domElement);
    this.controls.enableDamping = true;
    this.controls.dampingFactor = 0.05;
    this.controls.maxPolarAngle = Math.PI / 2 - 0.04;
    this.controls.minDistance = 4;
    this.controls.maxDistance = 450;
    this.controls.target.set(0, 2, 0);
  }

  _setupLights() {
    // Natural Hemisphere Light (Sky Blue / Ground Slate)
    this.hemiLight = new THREE.HemisphereLight(0xe0f2fe, 0x334155, 0.95);
    this.scene.add(this.hemiLight);

    // Warm Natural Sunlight
    this.dirLight = new THREE.DirectionalLight(0xfffbeb, 1.3);
    this.dirLight.position.set(120, 180, 90);
    this.dirLight.castShadow = true;
    this.dirLight.shadow.mapSize.width = 2048;
    this.dirLight.shadow.mapSize.height = 2048;
    this.dirLight.shadow.camera.near = 10;
    this.dirLight.shadow.camera.far = 450;
    const d = 180;
    this.dirLight.shadow.camera.left = -d;
    this.dirLight.shadow.camera.right = d;
    this.dirLight.shadow.camera.top = d;
    this.dirLight.shadow.camera.bottom = -d;
    this.dirLight.shadow.bias = -0.0005;
    this.scene.add(this.dirLight);

    // Soft Ambient Fill Light
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.25);
    this.scene.add(ambientLight);
  }

  setNightMode(isNight) {
    this.isNightMode = isNight;
    const btn = document.getElementById("btn-day-night");
    if (this.isNightMode) {
      // Deep Atmospheric Night
      this.scene.background.setHex(0x060913);
      this.scene.fog.color.setHex(0x060913);
      this.hemiLight.intensity = 0.45;
      this.hemiLight.color.setHex(0x38bdf8);
      this.hemiLight.groundColor.setHex(0x091428);
      this.dirLight.intensity = 0.55;
      this.dirLight.color.setHex(0x93c5fd);
      if (btn) btn.innerHTML = `<i class="fa-solid fa-moon"></i>`;
    } else {
      // Crisp Natural Daylight
      this.scene.background.setHex(0x93c5fd);
      this.scene.fog.color.setHex(0xbae6fd);
      this.hemiLight.intensity = 0.95;
      this.hemiLight.color.setHex(0xe0f2fe);
      this.hemiLight.groundColor.setHex(0x334155);
      this.dirLight.intensity = 1.3;
      this.dirLight.color.setHex(0xfffbeb);
      if (btn) btn.innerHTML = `<i class="fa-solid fa-sun"></i>`;
    }
  }

  _setupDayNightToggle() {
    const btn = document.getElementById("btn-day-night");
    this.manualNightOverride = false;
    this.setNightMode(false); // Day mode active by default

    btn.addEventListener("click", () => {
      this.manualNightOverride = true;
      this.setNightMode(!this.isNightMode);
    });

    document.getElementById("btn-refresh").addEventListener("click", () => {
      this.fetchWorldState();
    });
  }

  _setupAutoRefresh() {
    setInterval(() => {
      this.fetchWorldState(true);
    }, 4000);
  }

  async fetchWorldState(isPolling = false) {
    try {
      const res = await fetch(`data/town_state.json?t=${Date.now()}`);
      if (!res.ok) throw new Error("Could not load town_state.json");
      const state = await res.json();
      this.applyWorldState(state, isPolling);
    } catch (err) {
      if (!this.currentState && window.FALLBACK_TOWN_STATE) {
        console.info("Using embedded world state fallback (CORS / local file mode active).");
        this.applyWorldState(window.FALLBACK_TOWN_STATE, isPolling);
      } else if (!isPolling) {
        console.warn("Could not load town_state.json automatically, using fallback.", err);
      }
    }
  }

  applyWorldState(state, isPolling = false) {
    this.currentState = state;

    if (state.circadian_cycle && !this.manualNightOverride) {
      const isNight = (state.circadian_cycle === "NIGHT");
      if (this.isNightMode !== isNight) {
        this.setNightMode(isNight);
      }
    }

    this.townRenderer.renderRoads(state.roads);
    this.townRenderer.renderBuildings(state.buildings);
    this.townRenderer.renderVehicles(state.vehicles);
    this.agentManager.updateAgents(state.agents);
    this.ui.updateHUD(state);

    if (!isPolling) {
      console.log(`🏙️ Tech Town State loaded. Population: ${state.agents.length}, Tick: ${state.tick}`);
    }
  }

  _onWindowResize() {
    this.camera.aspect = window.innerWidth / window.innerHeight;
    this.camera.updateProjectionMatrix();
    this.renderer.setSize(window.innerWidth, window.innerHeight);
  }

  _animate() {
    requestAnimationFrame(() => this._animate());

    this.controls.update();
    this.agentManager.animate();
    
    if (this.currentState && this.currentState.vehicles) {
      this.townRenderer.renderVehicles(this.currentState.vehicles);
    }
    
    this.interaction.updateFollowCam();

    this.renderer.render(this.scene, this.camera);
  }
}

window.addEventListener("DOMContentLoaded", () => {
  window.app = new TechTownApp();
});
