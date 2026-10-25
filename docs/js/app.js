/**
 * App - Main 3D WebGL Application entry point.
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

    this.isNightMode = true;
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
    this.ui.setControllers(this.interaction, this.agentManager);

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
    this.scene.background = new THREE.Color(0x060913);
    this.scene.fog = new THREE.FogExp2(0x060913, 0.002);

    this.camera = new THREE.PerspectiveCamera(
      45,
      window.innerWidth / window.innerHeight,
      1,
      1000
    );
    // Initial Isometric Vantage Point
    this.camera.position.set(160, 140, 160);

    this.renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: "high-performance" });
    this.renderer.setSize(window.innerWidth, window.innerHeight);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    this.renderer.shadowMap.enabled = true;
    this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    this.container.appendChild(this.renderer.domElement);

    this.controls = new THREE.OrbitControls(this.camera, this.renderer.domElement);
    this.controls.enableDamping = true;
    this.controls.dampingFactor = 0.05;
    this.controls.maxPolarAngle = Math.PI / 2 - 0.05; // Prevent camera from slipping under floor
    this.controls.minDistance = 8;
    this.controls.maxDistance = 450;
    this.controls.target.set(0, 0, 0);
  }

  _setupLights() {
    this.hemiLight = new THREE.HemisphereLight(0x00f0ff, 0x091428, 0.6);
    this.scene.add(this.hemiLight);

    this.dirLight = new THREE.DirectionalLight(0xffffff, 0.8);
    this.dirLight.position.set(100, 150, 80);
    this.dirLight.castShadow = true;
    this.dirLight.shadow.mapSize.width = 2048;
    this.dirLight.shadow.mapSize.height = 2048;
    this.dirLight.shadow.camera.near = 10;
    this.dirLight.shadow.camera.far = 400;
    const d = 160;
    this.dirLight.shadow.camera.left = -d;
    this.dirLight.shadow.camera.right = d;
    this.dirLight.shadow.camera.top = d;
    this.dirLight.shadow.camera.bottom = -d;
    this.scene.add(this.dirLight);

    // Accent Point Lights in City Hubs
    const cyanPoint = new THREE.PointLight(0x00f0ff, 1.2, 120);
    cyanPoint.position.set(0, 30, 0);
    this.scene.add(cyanPoint);

    const purplePoint = new THREE.PointLight(0xa855f7, 1.0, 100);
    purplePoint.position.set(100, 20, 100);
    this.scene.add(purplePoint);
  }

  _setupDayNightToggle() {
    const btn = document.getElementById("btn-day-night");
    btn.addEventListener("click", () => {
      this.isNightMode = !this.isNightMode;
      if (this.isNightMode) {
        this.scene.background.setHex(0x060913);
        this.scene.fog.color.setHex(0x060913);
        this.hemiLight.intensity = 0.6;
        this.dirLight.intensity = 0.8;
        this.dirLight.color.setHex(0xffffff);
        btn.innerHTML = `<i class="fa-solid fa-moon"></i>`;
      } else {
        this.scene.background.setHex(0x93c5fd);
        this.scene.fog.color.setHex(0x93c5fd);
        this.hemiLight.intensity = 1.1;
        this.dirLight.intensity = 1.4;
        this.dirLight.color.setHex(0xffedd5);
        btn.innerHTML = `<i class="fa-solid fa-sun"></i>`;
      }
    });

    // Refresh button
    document.getElementById("btn-refresh").addEventListener("click", () => {
      this.fetchWorldState();
    });
  }

  _setupAutoRefresh() {
    // Poll for new town state every 4 seconds
    setInterval(() => {
      this.fetchWorldState(true);
    }, 4000);
  }

  async fetchWorldState(isPolling = false) {
    try {
      // Add cache buster to always fetch live git state
      const res = await fetch(`data/town_state.json?t=${Date.now()}`);
      if (!res.ok) throw new Error("Could not load town_state.json");
      const state = await res.json();
      this.currentState = state;

      this.townRenderer.renderRoads(state.roads);
      this.townRenderer.renderBuildings(state.buildings);
      this.townRenderer.renderVehicles(state.vehicles);
      this.agentManager.updateAgents(state.agents);
      this.ui.updateHUD(state);

      if (!isPolling) {
        console.log(`🏙️ Tech Town State loaded. Population: ${state.agents.length}, Tick: ${state.tick}`);
      }
    } catch (err) {
      if (!isPolling) {
        console.warn("Could not load town_state.json automatically, using fallback.", err);
      }
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

// Boot application when DOM is ready
window.addEventListener("DOMContentLoaded", () => {
  window.app = new TechTownApp();
});
