# 🏙️ GitHub Autonomous Tech Town

> A self-sustaining, autonomous Tech Town living and operating **completely inside GitHub**, populated by **200 initial pioneer AI agents** who live freely, construct roads, craft vehicles, build homes and cyber skyscrapers, **found new tech companies**, spawn new agents, write software projects, and run **24/7 inside GitHub Actions**, with a real-time **Interactive 3D WebGL (Three.js) Viewer**.

---

## 🌟 Key Features

1. **200 Pioneer Autonomous Agents**:
   - Starts with 200 distinct agents with individual names, professions, levels, energy, desires, inner thoughts, and live coordinates.
   - Professions include: *Urban Architects, Road & Infrastructure Engineers, Autonomous Vehicle Designers, AI Researchers, Quantum Systems Engineers, Full-Stack Web Architects, DevOps Sentinels, Cyber Botanists, Town Chroniclers, Energy Specialists, Artisans, and Security Cryptographers*.

2. **Complete Autonomy & Creativity Inside GitHub**:
   - Agents freely pursue their desires and build out the town:
     - **Founding Tech Companies**: Agents autonomously incorporate startups and enterprises (*Neural AI, Autonomous Mobility, Quantum Encryption, Fusion Grid*), erect corporate headquarters, and recruit fellow agents as co-founders and engineers (manifests stored in `companies/`).
     - **Roads & Highways**: Pave avenues and highways connecting town districts.
     - **Vehicles & Drones**: Design and manufacture autonomous cybercars, hover shuttles, and cargo drones that cruise the roads.
     - **Buildings & Living Pods**: Construct high-tech skyscrapers, AI research labs, residential living pods, solar arrays, quantum data centers, and holo parks (blueprints in `buildings/`).
     - **Spawning Agents**: High-level agents autonomously recruit and spawn new child agents when the population demands it.
     - **Code Projects**: Write real software modules into `projects/` (traffic algorithms, routing meshes, cryptographic audits).
     - **Diaries**: Maintain personal markdown logs in `diaries/` documenting life in GitHub.

3. **User Command Directives ("Until I give command, they work inside GitHub only")**:
   - By default, agents live and innovate autonomously inside GitHub.
   - Whenever you want to issue a command, you can direct the town:
     - **Via GitHub Actions**: Run the [Execute User Town Directive](.github/workflows/user_command.yml) workflow with your command (e.g. `"Build a suspension bridge in East Sector"`, `"Form an aerospace robotics company"`, `"Spawn 10 quantum researchers"`).
     - **Via GitHub Issues**: Open an issue titled `[COMMAND] <your directive>` or comment `/command <your directive>`.
     - **Via CLI**: Run `python3 run_town.py --command "<your directive>" --git-commit`.
   - The Town Mayor and relevant specialists will immediately execute your command with high priority!

4. **Runs 24/7 Inside GitHub**:
   - Powered by scheduled **GitHub Actions Workflows** (`.github/workflows/town_tick.yml`).
   - Runs simulation ticks on cron (`*/15 * * * *`), updates world state, generates agent artifacts, commits to Git, and pushes directly to `main`.
   - Also includes a continuous local runner (`python3 run_town.py --continuous`) with 0 external dependencies.

5. **Interactive 3D WebGL (Three.js) Viewer**:
   - Hostable directly on **GitHub Pages** (`docs/`).
   - **Zoom In / Out**: Full OrbitControls (mouse wheel, pinch) plus dedicated **Zoom In (+)** and **Zoom Out (-)** HUD buttons.
   - **Click-to-Inspect**: Click on any of the 200 agents to open the Inspector Drawer and see:
     - Live current work & action
     - Company affiliation (e.g. *Founder & CEO @ NeuroDynamics AI*)
     - Inner thoughts and philosophy
     - Core desire / ambition
     - Coordinates & energy reserves
     - Items created (buildings, roads, vehicles, companies, code files)
     - Collaborators & mentors
   - **Follow Agent Mode**: Camera locks onto and smoothly tracks any chosen agent as they navigate the city.
   - **Building & Vehicle Inspection**: Click on any building or cruising vehicle to view its blueprint, company headquarters info, and creator agent.
   - **Company Directory Filter**: Click the **Companies** filter button to inspect all incorporated enterprises, valuations, and founders.
   - **Day / Night Cycle**: Toggle between cyber neon night mode and daylight.
   - **Live Event Ticker**: Streams real-time announcements of agent creations, company foundings, and commits.

---

## 🗺️ Town Districts

| District | Center | Theme & Architecture | Primary Roles |
| :--- | :---: | :--- | :--- |
| **Silicon Central** | `[0, 0]` | High-rise neon Tech Towers, Corporate Megatowers, Mainframe | Urban Architects, Web Architects |
| **Innovation Matrix** | `[100, 100]` | Hexagonal AI Research Domes, Quantum Foundries | AI Researchers, Quantum Engineers |
| **Residential Quarter** | `[-100, 80]` | Modular living pods, rooftop terraces, green balconies | Civic Engineers, Society Chroniclers |
| **Cyber Commons** | `[-80, -90]` | Cyber cafes, Holo Parks, Town Hall Agora | Cyber Botanists, Artisans, Citizens |
| **Industrial Sector** | `[90, -100]` | Vehicle assembly factories, Tokamak fusion cores, server racks | Vehicle Designers, Energy Specialists |

---

## 🚀 Quick Start (Local)

The town simulation engine is built in **pure Python 3 standard library** with zero external pip dependencies!

### 1. Initialize Town & Pioneer Population
```bash
python3 run_town.py --init
```
*Generates the 200 initial agents, 5 pioneer enterprises, starting roads, iconic buildings, vehicles, and initial state files.*

### 2. Launch the 3D Viewer Locally
```bash
python3 run_town.py --serve --port 8000
```
Open **`http://localhost:8000`** in any web browser to view the interactive 3D Tech Town!

### 3. Issue a User Command
```bash
python3 run_town.py --command "Form a new quantum robotics company" --git-commit
```

### 4. Run Simulation Ticks
```bash
# Run 1 tick
python3 run_town.py --tick

# Run 5 ticks with auto-git-commit
python3 run_town.py --tick 5 --git-commit
```

### 5. Run 24/7 Continuous Daemon
```bash
# Runs continuous simulation loop with live 3D viewer
python3 run_town.py --continuous --serve --delay 3.0
```

---

## 🌐 Running 24/7 on GitHub

### 1. Push to GitHub
```bash
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git push -u origin main
```

### 2. Enable GitHub Pages
1. Go to your repository on GitHub: **Settings** -> **Pages**.
2. Under **Build and deployment**, set **Source** to **GitHub Actions** (or select branch `main` and folder `/docs`).
3. Your live 3D Tech Town will be accessible at:
   ```
   https://<your-username>.github.io/<your-repo-name>/
   ```

### 3. Automatic 24/7 Life Cycle
- The workflow in [`.github/workflows/town_tick.yml`](.github/workflows/town_tick.yml) runs automatically on a scheduled cron every 15 minutes.
- In each run, the simulation steps forward, agents build new items, found companies, create code in `projects/`, write in `diaries/`, and auto-commit back to GitHub!
- You can also manually trigger ticks at any time under the **Actions** tab on GitHub via **Run workflow**.

---

## 🎮 3D Viewer Navigation & Controls

| Action | Control |
| :--- | :--- |
| **Zoom In / Out** | Mouse Wheel, Pinch gesture, or Click **Zoom In (+)** / **Zoom Out (-)** buttons |
| **Rotate Camera** | Left Mouse Drag |
| **Pan Camera** | Right Mouse Drag |
| **Select & Inspect Agent** | Left Click on Agent Avatar |
| **Select & Inspect Building / HQ** | Left Click on Building |
| **Follow Selected Agent** | Click *"Follow Live"* in Inspector or Toolbar |
| **View Companies Directory** | Click *"Companies"* tag in bottom-left search box |
| **Search Agent / Role / Company**| Type name/keyword in search box |
| **Day / Night Mode** | Moon/Sun icon in top-right header |
| **Camera Presets** | Click *Isometric*, *Overview*, or *Street View* on left toolbar |

---

## 📁 Repository Structure

```
├── .github/
│   └── workflows/
│       ├── town_tick.yml        # 24/7 GitHub Actions simulation runner & committer
│       ├── user_command.yml     # User command directive executor
│       └── deploy_pages.yml     # Automated deployment to GitHub Pages
├── docs/                        # 3D Tech Town WebGL Application (GitHub Pages root)
│   ├── index.html               # 3D Town WebGL canvas & glassmorphic HUD
│   ├── css/
│   │   └── style.css            # Cyberpunk theme, cards, animations
│   ├── js/
│   │   ├── app.js               # Three.js main scene, camera, lighting, render loop
│   │   ├── town_renderer.js     # 3D rendering for roads, buildings, company HQs, vehicles, terrain
│   │   ├── agent_manager.js     # 200 agent avatars, movement, and overhead nameplates with company tags
│   │   ├── interaction.js       # Raycasting, click selection, camera transitions
│   │   └── ui.js                # Search, company filter, inspector drawer, zoom buttons, event ticker
│   └── data/
│       └── town_state.json      # Live synced world state loaded by 3D viewer
├── town/                        # Simulation Engine Backend
│   ├── __init__.py
│   ├── config.py                # Districts, roles, building types, company sectors, spawn limits
│   ├── models.py                # Agent, Company, Building, Road, Vehicle, TownState dataclasses
│   ├── generator.py             # Generates 200 pioneer agents, 5 enterprises, and foundational town
│   ├── simulation.py            # Autonomous life cycle: companies, building, coding, spawning, user commands
│   └── git_ops.py               # Auto-committer attributing commits to agents
├── companies/                   # Incorporated tech company manifests
│   └── comp-*.json
├── buildings/                   # Blueprints created by agents
│   └── bldg-*.json
├── projects/                    # Real code written and committed by agents
│   └── *.py
├── diaries/                     # Personal journals written by agents
│   └── agent-*_*.md
├── run_town.py                  # CLI driver (init, tick, continuous, command, serve)
└── README.md
```

---

## 📜 License
MIT © 2026 GitHub Tech Town Contributors. Created for autonomous multi-agent exploration inside GitHub.
