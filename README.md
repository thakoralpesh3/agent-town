# 🏛️ Sovereign Autonomous Country of Tech Town

> A fully autonomous, sovereign small country operating **completely inside GitHub**, inhabited by **320 pioneer and generational AI citizens** across **120+ specialized professions** and **14 sovereign national sectors**. Citizens live freely, govern, pave roads, construct monumental civic architecture, **found sovereign enterprises**, detect labor shortages, self-generate specialized citizens, maintain personal diaries, and run **24/7 inside GitHub Actions**, with an immersive **Interactive 3D WebGL (Three.js) Viewer**.

---

## 🌟 Sovereign Country Features

1. **320 Pioneer & Generational Citizens across 120+ Specialized Professions**:
   - Organized across **14 Sovereign National Sectors**:
     - *National Governance & Diplomacy* (Head of State, Parliament Speaker, Supreme Court Justice, Ambassadors)
     - *Treasury & Central Banking* (Central Bank Governor, Sovereign Wealth Strategist, DeFi Liquidity Overseers)
     - *Urban Mega-Engineering & Architecture* (Master Architects, Skybridge Engineers, Tunnel Specialists, Seismic Engineers)
     - *National Defense, Security & Emergency Services* (Cyber Defense Commander, Post-Quantum Cryptographers, Zero-Day Neutralizers)
     - *Advanced AI, Quantum & Systems* (Chief AI Architects, Transformer Alignment Scientists, Kernel Micro-Architects)
     - *Healthcare & Nanomedicine* (Surgeon General, Cardio Nanotech Surgeons, Neural Biologists, Gene Therapists)
     - *Energy, Fusion & Utilities* (Tokamak Plasma Containment Physicists, Superconducting Grid Dispatchers)
     - *Transportation & Aerospace Mobility* (Autonomous Fleet Directors, Hyperloop Engineers, VTOL Air Traffic Controllers)
     - *Agriculture, Food Security & Water* (Vertical Aeroponics Agronomists, Synthetic Protein Chemists, Desalination Engineers)
     - *Universities, Education & Science* (University Chancellors, Theoretical Physics Chairs, Town Historians)
     - *Culture, Arts & Media* (Ministers of Cultural Affairs, Volumetric Hologram Sculptors, Spatial Soundscapers)
     - *Manufacturing & Supply Chain* (Industrial Automation Directors, Quantum Lithographers, 3D Mega-Printers)
     - *Housing, Hospitality & Social Welfare* (Housing Commissioners, Quantum Baristas, Communal Stewards)
     - *Environmental Protection & Biosphere Balance* (Biosphere Custodians, Cyber Botanists, Atmospheric Scrubbers)
   - Both **old pioneer citizens** (Ada Lovelace, Alan Turing, Linus Torvalds, Grace Hopper, Margaret Hamilton, Dennis Ritchie, Claude Shannon, Demis Hassabis, Katherine Johnson, Dorothy Vaughan, etc.) and **new generational citizens** live, learn, mentor, and grow together.

2. **Autonomous Workforce Deficiency Detection & Self-Generation**:
   - If any national sector, facility, or critical civic infrastructure experiences a labor deficit or lacks staffing, citizens autonomously audit workforce metrics.
   - The town creates an official `JobRequisition` in `jobs/job-req-*.json`.
   - The country autonomously synthesizes and self-generates the required specialized citizen to fulfill the requisition.

3. **Confidential Operator Level 5 Clearance**:
   - **Exclusive User Control**: Only you (the Operator) hold Level 5 Clearance to interact with citizens and view confidential internal telemetry.
   - Unrestricted access to citizen internal thoughts, private salaries, and raw blueprint telemetry.
   - Direct bi-directional command link: Query citizens in real time or issue binding national orders (walk, recharge, build research facilities, hospitals, observatories, craft vehicles, pave roads, write code, found startups).

4. **100% Repository Immutability (Stored Strictly Inside GitHub)**:
   - Everything created by the country is written to GitHub repository files:
     - `state/town_state.json`: Complete sovereign state snapshot.
     - `jobs/`: Official job requisitions issued and fulfilled by citizens.
     - `buildings/`: Architectural blueprints and facility manifests.
     - `companies/`: Sovereign enterprise articles of incorporation.
     - `projects/`: Real software modules written and committed by citizens.
     - `diaries/`: Personal markdown diaries documenting life, work, and thoughts.
     - `commands/`: Immutable dialogue records between the Operator and citizens.

5. **Runs 24/7 Inside GitHub Actions**:
   - Powered by scheduled **GitHub Actions Workflows** (`.github/workflows/town_tick.yml`).
   - Simulates life on cron (`*/15 * * * *`), advances autonomous projects, records diaries, and commits state directly to `main`.
   - Also includes a pure Python local runner (`python3 run_town.py --continuous`).

6. **Realistic 3D WebGL (Three.js) Country Viewer**:
   - Hostable directly on **GitHub Pages** (`docs/`).
   - **National Plaza & Monuments**: Grand 32m Sovereign Obelisk with golden pyramidion and glowing cyber runes, National Flagpole with waving flag, and central tiered fountain.
   - **Architectural Diversity**: Neoclassical-futuristic Capitol with rotunda dome and colonnade, pillared Supreme Court, fortified Central Bank ziggurat, white nanomedical hospital with glowing red crosses and helipads, astronomical observatory with telescope dome, toroidal fusion reactors, and translucent green hydroponic biodomes.
   - **Deep Inspection**: Click any citizen, building, monument, or vehicle to inspect full specifications, floor capacities, active projects, desk occupancies, and interactive tenant rosters.
   - **Operator Command Terminal**: Interactive dialogue console in the 3D HUD with 14 quick order chips and custom natural language directive input.

---

## 🗺️ Sovereign Country Districts

| District | Center | Description & Facilities |
| :--- | :---: | :--- |
| **Capitol Hill & National Plaza** | `[0, 0]` | Sovereign Capitol, Supreme Court, Central Bank, Grand Obelisk, National Flagpole, National Archives |
| **Silicon Central Metropolis** | `[0, 110]` | Tower of Turing (Mainframe), Shannon Spire, Cloud Matrix Exchange, Von Neumann Tower |
| **Quantum Science & University Campus** | `[120, 40]` | Hypatia Grand University of Sciences, Grand Astronomical Observatory, Quantum Logic Foundry |
| **Health Citadel & Medical Complex** | `[-120, 40]` | National Hospital & Nanomedical Citadel, St. Ada Emergency Trauma Center, Longevity Institute |
| **Cyber Living Townships** | `[-100, -100]` | Cyber Living Townships Alpha & Beta, The Agora Civic Forum, The Bit & Byte Cyber Lounge |
| **Industrial Harbor & Transit Hub** | `[110, -110]` | Autonomous Vehicle Mega-Plant, Hyperloop Central Terminus, Drone Logistics Freight Port |
| **Biosphere Reserve & Fusion Grid** | `[0, -140]` | Tokamak Fusion Reactor Station, Hydroponic Agricultural Biodome, Atmospheric Scrubbers, Botanical Conservatory |

---

## 🚀 Quick Start (Local)

Built with the **Python 3 standard library** with zero external pip dependencies!

### 1. Initialize Country & Pioneer Population
```bash
python3 run_town.py --init
```
*Generates 320 initial citizens across 120+ professions, 8 sovereign enterprises, 27 foundational facilities, 15 arterial roads, and 10 vehicles.*

### 2. Launch the 3D Country Viewer Locally
```bash
python3 run_town.py --serve --port 8000
```
Open **`http://localhost:8000`** in your browser to view the interactive 3D Sovereign Country of Tech Town!

### 3. Issue an Operator Directive via CLI
```bash
python3 run_town.py --agent "agent-001" --command "What is your opinion on our sovereign republic?"
python3 run_town.py --agent "agent-002" --command "Build an advanced research facility" --git-commit
```

### 4. Run Simulation Ticks
```bash
# Run 1 tick
python3 run_town.py --tick

# Run 5 ticks with auto git commit
python3 run_town.py --tick 5 --git-commit
```

### 5. Run 24/7 Continuous Country Loop
```bash
python3 run_town.py --continuous --serve --delay 3.0
```

---

## 🌐 Running 24/7 on GitHub

1. Push your repository to GitHub:
   ```bash
   git push origin main
   ```
2. Enable GitHub Pages under **Settings** -> **Pages** (Source: **GitHub Actions** or `/docs` on `main`).
3. View live 3D country at: `https://<your-username>.github.io/<your-repo-name>/`.
4. GitHub Actions will execute simulation ticks 24/7 automatically!

---

## 📁 Repository Structure

```
├── .github/workflows/          # 24/7 GitHub Actions automation
├── docs/                       # 3D Country WebGL Viewer (GitHub Pages)
│   ├── index.html              # 3D Canvas, glassmorphic HUD, Operator terminal
│   ├── css/style.css           # Sovereign Country HUD styling
│   └── js/                     # Three.js engine, renderer, agents, interaction, UI
├── town/                       # Simulation Engine Backend
│   ├── config.py               # 120+ professions, 14 sectors, 7 districts, building types
│   ├── models.py               # Dataclasses (Agent, Building, Company, Road, Vehicle, JobReq)
│   ├── generator.py            # Generates foundational 320 citizens, facilities, and enterprises
│   ├── simulation.py           # Engine: workforce deficiency detection, growth, directives
│   └── git_ops.py              # Automated Git commits
├── state/                      # Current serialized town state
├── jobs/                       # Autonomous job requisitions
├── buildings/                  # Blueprints for all civic facilities
├── companies/                  # Incorporated sovereign enterprises
├── projects/                   # Autonomous code commits by citizens
├── diaries/                    # Citizen journals and chronicles
├── commands/                   # Operator directive dialogues
├── run_town.py                 # Main CLI controller
└── README.md
```

---

## 📜 License
MIT © 2026 Sovereign Country of Tech Town Contributors.
