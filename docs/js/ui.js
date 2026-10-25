/**
 * UI - Handles HTML HUD, Search & Filter, Inspector Drawer, and Event Ticker.
 */
class UIController {
  constructor() {
    this.drawer = document.getElementById("inspector-drawer");
    this.currentSelectedAgent = null;
    this.agentsList = [];
    this.interaction = null;
    this.agentManager = null;

    this._bindElements();
  }

  setControllers(interaction, agentManager) {
    this.interaction = interaction;
    this.agentManager = agentManager;
  }

  _bindElements() {
    // Close Inspector
    document.getElementById("insp-close").addEventListener("click", () => {
      this.closeInspector();
    });

    // Search Input
    const searchInput = document.getElementById("agent-search-input");
    searchInput.addEventListener("input", (e) => {
      this.filterAgents(e.target.value);
    });

    // District Filter Tags
    const tags = document.querySelectorAll("#district-tags .tag-btn");
    tags.forEach(tag => {
      tag.addEventListener("click", () => {
        tags.forEach(t => t.classList.remove("active"));
        tag.classList.add("active");
        const filter = tag.getAttribute("data-filter");
        this.filterByDistrict(filter);
      });
    });

    // Inspector Action Buttons
    document.getElementById("btn-focus-agent").addEventListener("click", () => {
      if (this.currentSelectedAgent && this.interaction) {
        this.interaction.focusOnPosition(this.currentSelectedAgent.position, 20);
      }
    });

    document.getElementById("btn-follow-active").addEventListener("click", () => {
      if (this.interaction) {
        this.interaction.toggleFollow();
      }
    });

    // Follow Toggle in Toolbar
    document.getElementById("btn-follow-toggle").addEventListener("click", () => {
      if (this.interaction) {
        this.interaction.toggleFollow();
      }
    });

    // Nameplates Toggle
    const btnLabels = document.getElementById("btn-toggle-labels");
    btnLabels.addEventListener("click", () => {
      if (this.agentManager) {
        this.agentManager.showLabels = !this.agentManager.showLabels;
        btnLabels.classList.toggle("active", this.agentManager.showLabels);
      }
    });
    btnLabels.classList.add("active");

    // Camera Presets
    document.getElementById("cam-iso").addEventListener("click", (e) => {
      this._setActiveToolBtn(e.currentTarget);
      if (this.interaction) {
        this.interaction.stopFollowing();
        this.interaction.focusOnPosition([0, 0, 0], 220);
      }
    });

    document.getElementById("cam-top").addEventListener("click", (e) => {
      this._setActiveToolBtn(e.currentTarget);
      if (this.interaction) {
        this.interaction.stopFollowing();
        this.interaction.controls.target.set(0, 0, 0);
        this.interaction.camera.position.set(0, 320, 1);
        this.interaction.controls.update();
      }
    });

    document.getElementById("cam-street").addEventListener("click", (e) => {
      this._setActiveToolBtn(e.currentTarget);
      if (this.interaction) {
        this.interaction.stopFollowing();
        this.interaction.controls.target.set(0, 2, 0);
        this.interaction.camera.position.set(25, 4, 30);
        this.interaction.controls.update();
      }
    });

    // Help Dialog
    document.getElementById("btn-help").addEventListener("click", () => {
      alert("🏙️ GitHub Autonomous Tech Town\n\n• 200 agents live, work, and grow inside this GitHub repo.\n• Click any agent to inspect their live thoughts, work, and desires.\n• Click any building or car to see blueprints and builders.\n• Use mouse wheel to zoom in/out, right drag to pan, left drag to rotate.\n• Agents run 24/7 on GitHub Actions!");
    });
  }

  _setActiveToolBtn(btn) {
    document.querySelectorAll("#toolbar-hud .tool-btn").forEach(b => {
      if (b.id.startsWith("cam-")) b.classList.remove("active");
    });
    btn.classList.add("active");
  }

  updateFollowButton(isFollowing) {
    const btn = document.getElementById("btn-follow-active");
    const toolbarBtn = document.getElementById("btn-follow-toggle");
    if (isFollowing) {
      btn.innerHTML = `<i class="fa-solid fa-stop"></i> Stop Following`;
      btn.style.borderColor = "var(--rose-neon)";
      btn.style.color = "var(--rose-neon)";
      toolbarBtn.classList.add("active");
    } else {
      btn.innerHTML = `<i class="fa-solid fa-person-running"></i> Follow Live`;
      btn.style.borderColor = "var(--cyan-neon)";
      btn.style.color = "var(--cyan-neon)";
      toolbarBtn.classList.remove("active");
    }
  }

  updateHUD(state) {
    document.getElementById("stat-pop").textContent = state.population || state.agents.length;
    document.getElementById("stat-bldg").textContent = state.buildings.length;
    document.getElementById("stat-roads").textContent = state.roads.length;
    document.getElementById("stat-vehs").textContent = state.vehicles.length;
    document.getElementById("stat-tick").textContent = state.tick;

    if (state.recent_events && state.recent_events.length > 0) {
      const latest = state.recent_events[state.recent_events.length - 1];
      document.getElementById("ticker-text").textContent = `[Tick ${latest.tick}] ${latest.message}`;
    }

    this.agentsList = state.agents;
    this.populateSearchResults(this.agentsList.slice(0, 30));
  }

  populateSearchResults(agents) {
    const container = document.getElementById("search-results-list");
    container.innerHTML = "";

    agents.forEach(agent => {
      const item = document.createElement("div");
      item.className = "agent-result-item";
      item.innerHTML = `
        <div>
          <div class="name" style="color: ${agent.color}">${agent.name}</div>
          <div class="role">${agent.role}</div>
        </div>
        <div style="font-size: 11px; font-family: var(--font-mono); color: var(--text-secondary);">Lv.${agent.level}</div>
      `;

      item.addEventListener("click", () => {
        if (this.interaction) {
          this.interaction.handleSelection(agent, 'agent');
        }
      });

      container.appendChild(item);
    });
  }

  filterAgents(query) {
    const q = query.toLowerCase().trim();
    if (!q) {
      this.populateSearchResults(this.agentsList.slice(0, 30));
      return;
    }
    const matched = this.agentsList.filter(a => 
      a.name.toLowerCase().includes(q) || a.role.toLowerCase().includes(q)
    );
    this.populateSearchResults(matched);
  }

  filterByDistrict(district) {
    if (district === 'all') {
      this.populateSearchResults(this.agentsList.slice(0, 30));
      return;
    }
    // Filter agents currently positioned inside district bounds
    const matched = this.agentsList.filter(a => a.action.includes(district) || a.desire.includes(district));
    this.populateSearchResults(matched.length > 0 ? matched : this.agentsList.slice(0, 30));
  }

  showAgentInspector(agent) {
    this.currentSelectedAgent = agent;
    this.drawer.classList.add("open");

    document.getElementById("insp-name").textContent = agent.name;
    document.getElementById("insp-role").textContent = `${agent.role} (Level ${agent.level})`;
    document.getElementById("insp-role").style.color = agent.color;
    document.getElementById("insp-action").textContent = agent.action;
    document.getElementById("insp-thought").textContent = `"${agent.thoughts}"`;
    document.getElementById("insp-desire").textContent = agent.desire;
    document.getElementById("insp-coords").textContent = `[${agent.position[0]}, ${agent.position[2]}]`;
    document.getElementById("insp-energy").textContent = `${agent.energy}%`;
    document.getElementById("insp-id").textContent = `${agent.id} (${agent.category})`;
    document.getElementById("insp-collabs").textContent = agent.collaborators && agent.collaborators.length > 0 ? agent.collaborators.join(", ") : "Solo Researcher";

    // Creations chips
    const creationsBox = document.getElementById("insp-creations");
    creationsBox.innerHTML = "";
    if (agent.creations && agent.creations.length > 0) {
      agent.creations.forEach(c => {
        const chip = document.createElement("span");
        chip.className = "creation-chip";
        chip.textContent = c.name || c.file || c.type;
        creationsBox.appendChild(chip);
      });
    } else {
      creationsBox.innerHTML = "<span style='font-size: 12px; color: var(--text-secondary);'>Surveying and designing starter projects...</span>";
    }
  }

  showBuildingInspector(bldg) {
    this.drawer.classList.add("open");
    document.getElementById("insp-name").textContent = bldg.name;
    document.getElementById("insp-role").textContent = `${bldg.type} in ${bldg.district}`;
    document.getElementById("insp-role").style.color = bldg.color;
    document.getElementById("insp-action").textContent = `Purpose: ${bldg.purpose}`;
    document.getElementById("insp-thought").textContent = `"Built by ${bldg.builder_name} (${bldg.builder_id}). Dimensions: ${bldg.size[0]}m x ${bldg.size[1]}m x ${bldg.size[2]}m"`;
    document.getElementById("insp-desire").textContent = `Operational in ${bldg.district} sector.`;
    document.getElementById("insp-coords").textContent = `[${bldg.position[0]}, ${bldg.position[2]}]`;
    document.getElementById("insp-energy").textContent = "100% (Grid Online)";
    document.getElementById("insp-id").textContent = `${bldg.id} (Infrastructure)`;
    document.getElementById("insp-collabs").textContent = bldg.builder_name;

    const creationsBox = document.getElementById("insp-creations");
    creationsBox.innerHTML = `<span class="creation-chip">Blueprint: buildings/${bldg.id}.json</span>`;
  }

  showVehicleInspector(veh) {
    this.drawer.classList.add("open");
    document.getElementById("insp-name").textContent = veh.name;
    document.getElementById("insp-role").textContent = `${veh.type} | Speed: ${veh.speed}x`;
    document.getElementById("insp-role").style.color = veh.color;
    document.getElementById("insp-action").textContent = `Cruising transit network towards destination.`;
    document.getElementById("insp-thought").textContent = `"Driver / Autopilot: ${veh.driver_name || 'Autonomous City AI'}. Built by: ${veh.builder_name}."`;
    document.getElementById("insp-desire").textContent = `Autonomous zero-emission transport across town.`;
    document.getElementById("insp-coords").textContent = `[${veh.position[0]}, ${veh.position[2]}]`;
    document.getElementById("insp-energy").textContent = "Induction Charged";
    document.getElementById("insp-id").textContent = `${veh.id} (Autonomous Vehicle)`;
    document.getElementById("insp-collabs").textContent = veh.driver_name || "Autonomous AI";

    const creationsBox = document.getElementById("insp-creations");
    creationsBox.innerHTML = `<span class="creation-chip">Vehicle ID: ${veh.id}</span>`;
  }

  closeInspector() {
    this.drawer.classList.remove("open");
    if (this.agentManager) {
      this.agentManager.selectAgent(null);
    }
    if (this.interaction) {
      this.interaction.stopFollowing();
    }
  }
}
