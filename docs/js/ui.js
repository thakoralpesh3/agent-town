/**
 * UI - Handles HTML HUD, Search & Filter, Company Directory, Inspector Drawer, and Event Ticker.
 */
class UIController {
  constructor() {
    this.drawer = document.getElementById("inspector-drawer");
    this.currentSelectedAgent = null;
    this.agentsList = [];
    this.companiesList = [];
    this.buildingsList = [];
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

    // Search Drawer Mobile Toggle
    const searchHud = document.getElementById("search-hud");
    const btnToggleSearch = document.getElementById("btn-toggle-search");
    if (btnToggleSearch && searchHud) {
      btnToggleSearch.addEventListener("click", () => {
        searchHud.classList.toggle("mobile-open");
        if (searchHud.classList.contains("mobile-open")) {
          document.getElementById("agent-search-input")?.focus();
        }
      });
    }

    const btnCloseSearch = document.getElementById("btn-close-search");
    if (btnCloseSearch && searchHud) {
      btnCloseSearch.addEventListener("click", () => {
        searchHud.classList.remove("mobile-open");
      });
    }

    // Search Input
    const searchInput = document.getElementById("agent-search-input");
    searchInput.addEventListener("input", (e) => {
      this.filterAgents(e.target.value);
    });

    // District & Company Filter Tags
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

    // Zoom Controls
    document.getElementById("btn-zoom-in").addEventListener("click", () => {
      if (this.interaction) {
        this.interaction.controls.dollyIn(1.25);
        this.interaction.controls.update();
      }
    });

    document.getElementById("btn-zoom-out").addEventListener("click", () => {
      if (this.interaction) {
        this.interaction.controls.dollyOut(1.25);
        this.interaction.controls.update();
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

    // Locate Workplace Facility Button
    const btnLocateFacility = document.getElementById("btn-locate-facility");
    if (btnLocateFacility) {
      btnLocateFacility.addEventListener("click", () => {
        const bldgId = btnLocateFacility.getAttribute("data-bldg-id");
        if (bldgId && this.interaction) {
          const bldg = this.buildingsList.find(b => b.id === bldgId);
          if (bldg) {
            this.showBuildingInspector(bldg);
            this.interaction.focusOnPosition(bldg.position, 35);
          }
        }
      });
    }

    // Help Dialog
    document.getElementById("btn-help").addEventListener("click", () => {
      alert("🏙️ GitHub Autonomous Tech Town (Operator L5 Active)\n\n• 250 pioneer agents across 60+ specialized professions living 24/7 inside this GitHub repo.\n• All creations, blueprints, job requisitions, and diaries are stored in GitHub.\n• Autonomous Workforce Deficiency Detection: When labor deficits are identified, town agents autonomously post requisitions and self-generate specialized agents.\n• Confidential Operator Level 5 Clearance: Private telemetry, internal directives, token compensations, and thoughts are restricted to your operator HUD.\n• Interactive Inspection: Click any agent or building to view full specs, desk occupancy, departments, and interactive tenant rosters!\n• Use Zoom In/Out (+/-) or mouse wheel to navigate.");
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
    document.getElementById("stat-corps").textContent = state.companies ? state.companies.length : 0;
    document.getElementById("stat-bldg").textContent = state.buildings.length;
    document.getElementById("stat-roads").textContent = state.roads.length;
    document.getElementById("stat-vehs").textContent = state.vehicles.length;
    document.getElementById("stat-tick").textContent = state.tick;

    if (state.recent_events && state.recent_events.length > 0) {
      const latest = state.recent_events[state.recent_events.length - 1];
      document.getElementById("ticker-text").textContent = `[Tick ${latest.tick}] ${latest.message}`;
    }

    this.agentsList = state.agents;
    this.companiesList = state.companies || [];
    this.buildingsList = state.buildings || [];
    this.populateSearchResults(this.agentsList.slice(0, 30));
  }

  populateSearchResults(agents) {
    const container = document.getElementById("search-results-list");
    container.innerHTML = "";

    agents.forEach(agent => {
      const item = document.createElement("div");
      item.className = "agent-result-item";
      const compLabel = agent.company_name ? `<div style="font-size: 10px; color: #f472b6;">🏢 ${agent.company_name}</div>` : '';
      item.innerHTML = `
        <div>
          <div class="name" style="color: ${agent.color}">${agent.name}</div>
          <div class="role" style="color: #cbd5e1; font-size: 11px;">${agent.career_title || agent.role}</div>
          ${compLabel}
        </div>
        <div style="font-size: 11px; font-family: var(--font-mono); color: var(--cyan-neon); font-weight: bold;">Lv.${agent.level}</div>
      `;

      item.addEventListener("click", () => {
        document.getElementById("search-hud")?.classList.remove("mobile-open");
        if (this.interaction) {
          this.interaction.handleSelection(agent, 'agent');
        }
      });

      container.appendChild(item);
    });
  }

  populateCompanyResults(companies) {
    const container = document.getElementById("search-results-list");
    container.innerHTML = "";

    companies.forEach(comp => {
      const item = document.createElement("div");
      item.className = "agent-result-item";
      item.innerHTML = `
        <div>
          <div class="name" style="color: ${comp.color}; font-weight: bold;">🏢 ${comp.name}</div>
          <div class="role" style="color: #cbd5e1;">${comp.sector}</div>
          <div style="font-size: 10px; color: var(--text-secondary);">Founder: ${comp.founder_name} | ${comp.employees.length} agents</div>
        </div>
        <div style="font-size: 11px; font-family: var(--font-mono); color: var(--cyan-neon);">${Math.round(comp.valuation_tokens / 1000)}k 💎</div>
      `;

      item.addEventListener("click", () => {
        document.getElementById("search-hud")?.classList.remove("mobile-open");
        // Find company HQ building
        const hq = this.buildingsList.find(b => b.id === comp.headquarters_id || b.name.includes(comp.name));
        if (hq && this.interaction) {
          this.interaction.handleSelection(hq, 'building');
        } else if (this.interaction) {
          // Focus on founder
          const founder = this.agentsList.find(a => a.id === comp.founder_id);
          if (founder) this.interaction.handleSelection(founder, 'agent');
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
      a.name.toLowerCase().includes(q) || 
      a.role.toLowerCase().includes(q) ||
      (a.company_name && a.company_name.toLowerCase().includes(q))
    );
    this.populateSearchResults(matched);
  }

  filterByDistrict(district) {
    if (district === 'all') {
      this.populateSearchResults(this.agentsList.slice(0, 30));
      return;
    }
    if (district === 'companies') {
      this.populateCompanyResults(this.companiesList);
      return;
    }
    const matched = this.agentsList.filter(a => 
      a.category === district || 
      a.role.toLowerCase().includes(district.toLowerCase()) ||
      a.action.includes(district) || 
      a.desire.includes(district)
    );
    this.populateSearchResults(matched.length > 0 ? matched : this.agentsList.slice(0, 30));
  }

  showAgentInspector(agent) {
    this.currentSelectedAgent = agent;
    this.drawer.classList.add("open");

    // Operator Clearance Header
    const clearanceLabel = document.getElementById("insp-clearance-label");
    if (clearanceLabel) {
      clearanceLabel.textContent = `CONFIDENTIAL CITIZEN DOSSIER // OPERATOR CLEARANCE LEVEL 5 // ${agent.security_clearance || 'LEVEL 4'}`;
    }

    // Avatar and Profile
    document.getElementById("insp-name").textContent = agent.name;
    const title = agent.career_title || `${agent.role} (Lv. ${agent.level})`;
    document.getElementById("insp-role").textContent = title;
    document.getElementById("insp-role").style.color = agent.color;

    // Specialization Pill
    const specPill = document.getElementById("insp-specialization-pill");
    if (specPill) {
      specPill.style.display = "inline-flex";
      document.getElementById("insp-spec-text").textContent = agent.specialization || agent.category;
    }

    // Toggle Panels for Agent View
    const growthCard = document.getElementById("insp-growth-wrapper");
    if (growthCard) growthCard.style.display = "flex";
    const skillsSection = document.getElementById("insp-skills-section");
    if (skillsSection) skillsSection.style.display = "flex";
    const toolsSection = document.getElementById("insp-tools-section");
    if (toolsSection) toolsSection.style.display = "flex";

    const bldgSpecs = document.getElementById("insp-building-specs");
    if (bldgSpecs) bldgSpecs.style.display = "none";
    const deptsSection = document.getElementById("insp-departments-section");
    if (deptsSection) deptsSection.style.display = "none";
    const tenantsSection = document.getElementById("insp-tenants-section");
    if (tenantsSection) tenantsSection.style.display = "none";

    // Assigned Facility / Workplace Card
    const wpCard = document.getElementById("insp-workplace-card");
    const wpVal = document.getElementById("insp-workplace-val");
    const btnLocateFacility = document.getElementById("btn-locate-facility");
    if (wpCard && agent.workplace_name) {
      wpCard.style.display = "flex";
      wpVal.textContent = agent.workplace_name;
      if (btnLocateFacility) {
        btnLocateFacility.setAttribute("data-bldg-id", agent.workplace_id || "");
      }
    } else if (wpCard) {
      wpCard.style.display = "none";
    }

    // XP & Career Progression
    const careerTitleEl = document.getElementById("insp-career-title");
    if (careerTitleEl) careerTitleEl.textContent = agent.career_title || agent.role;
    const curXP = agent.experience || 0;
    const nextXP = agent.xp_to_next_level || (agent.level ** 2 * 100);
    const prevXP = (agent.level - 1) ** 2 * 100;
    const progressPct = Math.min(100, Math.max(5, Math.round(((curXP - prevXP) / Math.max(1, (nextXP - prevXP))) * 100)));
    
    document.getElementById("insp-xp-current").textContent = curXP;
    document.getElementById("insp-xp-next").textContent = nextXP;
    document.getElementById("insp-xp-fill").style.width = `${progressPct}%`;
    
    const genText = agent.generation ? `Gen ${agent.generation} Citizen` : "Gen 1 Pioneer";
    document.getElementById("insp-generation").innerHTML = `<i class="fa-solid fa-dna"></i> ${genText}`;
    const mentorText = agent.mentor_name ? `Mentor: ${agent.mentor_name}` : "Self-Taught / Founder";
    document.getElementById("insp-mentor-label").innerHTML = `<i class="fa-solid fa-user-graduate"></i> ${mentorText}`;

    // Mastered Skills Chips
    const skillsContainer = document.getElementById("insp-skills-chips");
    if (skillsContainer) {
      skillsContainer.innerHTML = "";
      const skills = (agent.skills && agent.skills.length > 0) ? agent.skills : ["Foundational Innovation", "Continuous Learning"];
      skills.forEach(skill => {
        const chip = document.createElement("span");
        chip.className = "skill-chip";
        chip.textContent = skill;
        skillsContainer.appendChild(chip);
      });
    }

    // Equipped Tools & Gear Chips
    const toolsContainer = document.getElementById("insp-tools-chips");
    if (toolsContainer) {
      toolsContainer.innerHTML = "";
      const tools = (agent.tools_equipped && agent.tools_equipped.length > 0) ? agent.tools_equipped : ["Neural Terminal", "Precision Diagnostics Scope"];
      tools.forEach(tool => {
        const chip = document.createElement("span");
        chip.className = "skill-chip";
        chip.style.borderColor = "rgba(245, 158, 11, 0.4)";
        chip.style.color = "#fbbf24";
        chip.style.background = "rgba(245, 158, 11, 0.12)";
        chip.innerHTML = `<i class="fa-solid fa-microchip" style="font-size: 9px; margin-right: 4px;"></i>${tool}`;
        toolsContainer.appendChild(chip);
      });
    }

    document.getElementById("insp-action").textContent = agent.action;
    document.getElementById("insp-thought").textContent = `"${agent.thoughts}"`;
    document.getElementById("insp-desire").textContent = agent.desire;
    document.getElementById("insp-coords").textContent = `[${agent.position[0]}, ${agent.position[2]}]`;
    document.getElementById("insp-energy").textContent = `${agent.energy}%`;
    document.getElementById("insp-id").textContent = `${agent.id} (${agent.category})`;

    // Operator Telemetry Fields
    const shiftEl = document.getElementById("insp-shift");
    if (shiftEl) shiftEl.textContent = agent.shift || "Morning Shift (08:00 - 16:00)";
    const salaryEl = document.getElementById("insp-salary");
    if (salaryEl) salaryEl.textContent = `${(agent.salary_tokens || 12500).toLocaleString()} Tokens / cycle`;
    const clearanceEl = document.getElementById("insp-clearance");
    if (clearanceEl) clearanceEl.textContent = agent.security_clearance || "Level 4 - Controlled";
    const contribsEl = document.getElementById("insp-contributions");
    if (contribsEl) contribsEl.textContent = `${agent.total_contributions || 1} Commits / Blueprints`;
    document.getElementById("insp-collabs").textContent = agent.collaborators && agent.collaborators.length > 0 ? agent.collaborators.join(", ") : "Independent";

    // Company Banner
    const compWrapper = document.getElementById("insp-company-wrapper");
    if (agent.company_name) {
      compWrapper.style.display = "block";
      document.getElementById("insp-company-text").textContent = `Enterprise: ${agent.company_name}`;
    } else {
      compWrapper.style.display = "none";
    }

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

    // Operator Clearance Header
    const clearanceLabel = document.getElementById("insp-clearance-label");
    if (clearanceLabel) {
      clearanceLabel.textContent = `CONFIDENTIAL FACILITY AUDIT // OPERATOR CLEARANCE LEVEL 5 // ${bldg.security_level || 'LEVEL 3'}`;
    }

    // Name & Title
    document.getElementById("insp-name").textContent = bldg.name;
    document.getElementById("insp-role").textContent = `${bldg.type} in ${bldg.district}`;
    document.getElementById("insp-role").style.color = bldg.color;

    // Specialization Pill
    const specPill = document.getElementById("insp-specialization-pill");
    if (specPill) {
      specPill.style.display = "inline-flex";
      document.getElementById("insp-spec-text").textContent = `${bldg.district} Sector`;
    }

    // Toggle Panels for Building View
    const growthCard = document.getElementById("insp-growth-wrapper");
    if (growthCard) growthCard.style.display = "none";
    const skillsSection = document.getElementById("insp-skills-section");
    if (skillsSection) skillsSection.style.display = "none";
    const toolsSection = document.getElementById("insp-tools-section");
    if (toolsSection) toolsSection.style.display = "none";
    const wpCard = document.getElementById("insp-workplace-card");
    if (wpCard) wpCard.style.display = "none";

    const bldgSpecs = document.getElementById("insp-building-specs");
    if (bldgSpecs) bldgSpecs.style.display = "block";
    const deptsSection = document.getElementById("insp-departments-section");
    if (deptsSection) deptsSection.style.display = "block";
    const tenantsSection = document.getElementById("insp-tenants-section");
    if (tenantsSection) tenantsSection.style.display = "block";

    // Building Specs
    const floors = bldg.floors || Math.max(2, Math.round(bldg.size[1] / 4));
    const capacity = bldg.capacity || (floors * 4);
    const occupants = bldg.occupants || [];
    const occupancyPct = Math.min(100, Math.round((occupants.length / Math.max(1, capacity)) * 100));

    document.getElementById("insp-bldg-floors").textContent = `${floors} Floors (${bldg.size[1]}m)`;
    document.getElementById("insp-bldg-cap").textContent = `${occupants.length} / ${capacity}`;
    document.getElementById("insp-bldg-power").textContent = `${bldg.power_consumption_mw || 3.5} MW`;
    document.getElementById("insp-bldg-sec").textContent = bldg.security_level || "Level 3";
    document.getElementById("insp-occupancy-pct").textContent = `${occupancyPct}%`;
    document.getElementById("insp-occupancy-fill").style.width = `${occupancyPct}%`;

    // Departments & Amenities Chips
    const deptsContainer = document.getElementById("insp-departments-chips");
    if (deptsContainer) {
      deptsContainer.innerHTML = "";
      const depts = bldg.departments || ["Operations Core", "Research Wing"];
      depts.forEach(dept => {
        const chip = document.createElement("span");
        chip.className = "skill-chip";
        chip.style.borderColor = "rgba(168, 85, 247, 0.4)";
        chip.style.color = "#d8b4fe";
        chip.style.background = "rgba(168, 85, 247, 0.12)";
        chip.innerHTML = `<i class="fa-solid fa-sitemap" style="font-size: 9px; margin-right: 4px;"></i>${dept}`;
        deptsContainer.appendChild(chip);
      });
      const amenities = bldg.amenities || [];
      amenities.forEach(amenity => {
        const chip = document.createElement("span");
        chip.className = "skill-chip";
        chip.style.borderColor = "rgba(0, 240, 255, 0.35)";
        chip.style.color = "var(--cyan-neon)";
        chip.style.background = "rgba(0, 240, 255, 0.1)";
        chip.innerHTML = `<i class="fa-solid fa-sparkles" style="font-size: 9px; margin-right: 4px;"></i>${amenity}`;
        deptsContainer.appendChild(chip);
      });
    }

    // Interactive Staff & Resident Roster
    const tenantsCountEl = document.getElementById("insp-tenants-count");
    if (tenantsCountEl) tenantsCountEl.textContent = occupants.length;
    const tenantsContainer = document.getElementById("insp-tenants-list");
    if (tenantsContainer) {
      tenantsContainer.innerHTML = "";
      if (occupants.length > 0) {
        occupants.forEach(occName => {
          const occAgent = this.agentsList.find(a => a.name === occName);
          const item = document.createElement("div");
          item.className = "tenant-item";
          const dotColor = occAgent ? occAgent.color : "var(--cyan-neon)";
          const occRole = occAgent ? occAgent.role : "Citizen Specialist";
          const occSpec = occAgent && occAgent.specialization ? ` • ${occAgent.specialization}` : "";
          
          item.innerHTML = `
            <div class="tenant-item-left">
              <span class="tenant-dot" style="background-color: ${dotColor}; box-shadow: 0 0 6px ${dotColor};"></span>
              <div>
                <div class="tenant-name">${occName}</div>
                <div class="tenant-role">${occRole}${occSpec}</div>
              </div>
            </div>
            <i class="fa-solid fa-chevron-right tenant-arrow"></i>
          `;

          item.addEventListener("click", () => {
            if (occAgent && this.interaction) {
              this.interaction.handleSelection(occAgent, "agent");
            }
          });
          tenantsContainer.appendChild(item);
        });
      } else {
        tenantsContainer.innerHTML = `<div style="font-size: 12px; color: var(--text-secondary); padding: 8px;">No citizens currently stationed. Space available for allocation.</div>`;
      }
    }

    document.getElementById("insp-action").textContent = `Purpose: ${bldg.purpose}`;
    document.getElementById("insp-thought").textContent = `"Built by ${bldg.builder_name} (${bldg.builder_id}). Grid Footprint: ${bldg.size[0]}m x ${bldg.size[1]}m x ${bldg.size[2]}m"`;
    document.getElementById("insp-desire").textContent = `Continuous 24/7 civic operations in ${bldg.district}.`;
    document.getElementById("insp-coords").textContent = `[${bldg.position[0]}, ${bldg.position[2]}]`;
    document.getElementById("insp-energy").textContent = "100% (Substation Linked)";
    document.getElementById("insp-id").textContent = `${bldg.id} (${bldg.type})`;

    // Building Telemetry Fields
    const shiftEl = document.getElementById("insp-shift");
    if (shiftEl) shiftEl.textContent = `${bldg.maintenance_status || 'Optimal'} (24/7 Grid)`;
    const salaryEl = document.getElementById("insp-salary");
    if (salaryEl) salaryEl.textContent = "N/A (Civic Facility)";
    const clearanceEl = document.getElementById("insp-clearance");
    if (clearanceEl) clearanceEl.textContent = bldg.security_level || "Level 3 - Monitored";
    const contribsEl = document.getElementById("insp-contributions");
    if (contribsEl) contribsEl.textContent = `${(bldg.active_projects || []).length} Hosted Projects`;
    document.getElementById("insp-collabs").textContent = bldg.builder_name;

    const compWrapper = document.getElementById("insp-company-wrapper");
    if (bldg.company_name) {
      compWrapper.style.display = "block";
      document.getElementById("insp-company-text").textContent = `🏢 Global Headquarters: ${bldg.company_name}`;
    } else {
      compWrapper.style.display = "none";
    }

    const creationsBox = document.getElementById("insp-creations");
    creationsBox.innerHTML = `<span class="creation-chip"><i class="fa-solid fa-file-code"></i> buildings/${bldg.id}.json</span>`;
    if (bldg.active_projects && bldg.active_projects.length > 0) {
      bldg.active_projects.forEach(p => {
        const chip = document.createElement("span");
        chip.className = "creation-chip";
        chip.innerHTML = `<i class="fa-solid fa-code"></i> projects/${p}`;
        creationsBox.appendChild(chip);
      });
    }
  }

  showVehicleInspector(veh) {
    this.drawer.classList.add("open");

    // Operator Clearance Header
    const clearanceLabel = document.getElementById("insp-clearance-label");
    if (clearanceLabel) {
      clearanceLabel.textContent = `CONFIDENTIAL VEHICLE TELEMETRY // OPERATOR CLEARANCE LEVEL 5`;
    }

    const growthCard = document.getElementById("insp-growth-wrapper");
    if (growthCard) growthCard.style.display = "none";
    const skillsSection = document.getElementById("insp-skills-section");
    if (skillsSection) skillsSection.style.display = "none";
    const toolsSection = document.getElementById("insp-tools-section");
    if (toolsSection) toolsSection.style.display = "none";
    const wpCard = document.getElementById("insp-workplace-card");
    if (wpCard) wpCard.style.display = "none";
    const bldgSpecs = document.getElementById("insp-building-specs");
    if (bldgSpecs) bldgSpecs.style.display = "none";
    const deptsSection = document.getElementById("insp-departments-section");
    if (deptsSection) deptsSection.style.display = "none";
    const tenantsSection = document.getElementById("insp-tenants-section");
    if (tenantsSection) tenantsSection.style.display = "none";

    document.getElementById("insp-name").textContent = veh.name;
    document.getElementById("insp-role").textContent = `${veh.type} | Speed: ${veh.speed}x`;
    document.getElementById("insp-role").style.color = veh.color;

    const specPill = document.getElementById("insp-specialization-pill");
    if (specPill) {
      specPill.style.display = "inline-flex";
      document.getElementById("insp-spec-text").textContent = "Autonomous Mobility";
    }

    document.getElementById("insp-action").textContent = `Cruising transit network towards destination.`;
    document.getElementById("insp-thought").textContent = `"Driver / Autopilot: ${veh.driver_name || 'Autonomous City AI'}. Built by: ${veh.builder_name}."`;
    document.getElementById("insp-desire").textContent = `Autonomous zero-emission transport across town.`;
    document.getElementById("insp-coords").textContent = `[${veh.position[0]}, ${veh.position[2]}]`;
    document.getElementById("insp-energy").textContent = "Induction Charged";
    document.getElementById("insp-id").textContent = `${veh.id} (Autonomous Vehicle)`;

    const shiftEl = document.getElementById("insp-shift");
    if (shiftEl) shiftEl.textContent = "Autonomous 24/7 Transit";
    const salaryEl = document.getElementById("insp-salary");
    if (salaryEl) salaryEl.textContent = "N/A (Autonomous Unit)";
    const clearanceEl = document.getElementById("insp-clearance");
    if (clearanceEl) clearanceEl.textContent = "Level 3 - Monitored Transit";
    const contribsEl = document.getElementById("insp-contributions");
    if (contribsEl) contribsEl.textContent = "Transit Routing Service";
    document.getElementById("insp-collabs").textContent = veh.driver_name || "Autonomous AI";

    document.getElementById("insp-company-wrapper").style.display = "none";

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
