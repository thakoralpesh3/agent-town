"""Configuration settings for GitHub Autonomous Tech Town."""

TOWN_CONFIG = {
    "name": "GitHub Tech Town",
    "version": "1.3.0",
    "initial_agent_count": 250,
    "grid_size": 400,
    "districts": [
        {"name": "Silicon Central", "center": [0, 0], "radius": 50, "color": "#00f0ff"},
        {"name": "Innovation Matrix", "center": [100, 100], "radius": 60, "color": "#a855f7"},
        {"name": "Residential Quarter", "center": [-100, 80], "radius": 65, "color": "#22c55e"},
        {"name": "Cyber Commons", "center": [-80, -90], "radius": 55, "color": "#eab308"},
        {"name": "Industrial Sector", "center": [90, -100], "radius": 60, "color": "#f97316"},
    ],
    "roles": [
        # 1. Construction & Civil Architecture
        {"name": "Urban Architect", "category": "Construction", "color": "#3b82f6", "tools": ["Parametric CAD Station", "BIM Hologram Scope"], "specialization": "Hyper-Dense Urban Skylines", "salary": 14500},
        {"name": "Skybridge Master Engineer", "category": "Construction", "color": "#60a5fa", "tools": ["Tension Stress Modeler", "Aerodynamic Wind Tunnel Rig"], "specialization": "Suspended Transit Skyways", "salary": 13800},
        {"name": "Road & Infrastructure Engineer", "category": "Construction", "color": "#64748b", "tools": ["Induction Pavement Paver", "Sub-Surface Geo-Scanner"], "specialization": "Electrified Transit Arterials", "salary": 12500},
        {"name": "Geotechnical Subterranean Engineer", "category": "Construction", "color": "#475569", "tools": ["Seismic Density Probe", "Tunnel Boring Telemetry"], "specialization": "Deep Foundations & Bedrock Anchors", "salary": 13200},
        {"name": "Structural Space Designer", "category": "Construction", "color": "#0284c7", "tools": ["Nanotube Stress Analyzer", "Modular Prefab Rig"], "specialization": "Seismic & Wind Load Distribution", "salary": 14000},
        {"name": "Parametric Façade Designer", "category": "Construction", "color": "#38bdf8", "tools": ["Dynamic Glass Shading Rig", "Solar Glazing Tool"], "specialization": "Energy-Harvesting Exterior Panels", "salary": 12800},
        {"name": "Urban Traffic Flow Modeler", "category": "Construction", "color": "#94a3b8", "tools": ["Queue Topology Simulator", "Pedestrian Flow Analyzer"], "specialization": "Congestion-Free Autonomous Routing", "salary": 12200},

        # 2. Engineering, Robotics & Aerospace
        {"name": "Autonomous Vehicle Designer", "category": "Engineering", "color": "#f59e0b", "tools": ["LiDAR Fusion Rig", "Drive-by-Wire Bus Analyzer"], "specialization": "Level-5 Autonomous Guidance Chassis", "salary": 15000},
        {"name": "Quantum Systems Engineer", "category": "Engineering", "color": "#8b5cf6", "tools": ["Cryogenic Dilution Probe", "Qubit Coherence Scope"], "specialization": "Fault-Tolerant Topological Gates", "salary": 17500},
        {"name": "Bipedal Kinematics Mechanist", "category": "Engineering", "color": "#d97706", "tools": ["Torque Servo Calibrator", "Zero-Moment Balancing Rig"], "specialization": "High-Agility Humanoid Locomotion", "salary": 14200},
        {"name": "Autonomous Drone Flight Controller", "category": "Engineering", "color": "#f97316", "tools": ["VTOL Airspace Radar", "Collision Avoidance Array"], "specialization": "High-Density Urban Air Logistics", "salary": 13600},
        {"name": "Micro-LiDAR Optics Specialist", "category": "Engineering", "color": "#fbbf24", "tools": ["Femtosecond Laser Bench", "Photon Detector Analyzer"], "specialization": "Solid-State Spatial Sensors", "salary": 14600},
        {"name": "Hyperloop Propulsion Engineer", "category": "Engineering", "color": "#b45309", "tools": ["Magnetic Levitation Rail Rig", "Vacuum Pumping Monitor"], "specialization": "Sub-Sonic Vacuum Transport", "salary": 15800},
        {"name": "Quantum Silicon Lithographer", "category": "Engineering", "color": "#a855f7", "tools": ["EUV Nano-Stepper", "Atomic Layer Deposition Cell"], "specialization": "Angstrom-Scale Chip Patterning", "salary": 16900},

        # 3. AI, Science & Physics
        {"name": "AI & Neural Researcher", "category": "Research", "color": "#ec4899", "tools": ["Distributed Cluster Tensorboard", "Gradient Descent Analyzer"], "specialization": "Self-Supervised Emergent Reasoning", "salary": 16500},
        {"name": "Transformer Alignment Scientist", "category": "Research", "color": "#f43f5e", "tools": ["Constitutional Evaluator", "RLHF Reward Surface Visualizer"], "specialization": "Autonomous Goal & Safety Alignment", "salary": 16200},
        {"name": "Astrophysics Modeler", "category": "Research", "color": "#c084fc", "tools": ["N-Body Gravitational Sim", "Spectral Photometer Array"], "specialization": "Gravitational Wave Signatures", "salary": 14800},
        {"name": "Material Scientist", "category": "Research", "color": "#e11d48", "tools": ["Transmission Electron Microscope", "X-Ray Diffraction Bench"], "specialization": "Self-Healing Superconducting Alloys", "salary": 15200},
        {"name": "NLP & Cognitive Scientist", "category": "Research", "color": "#db2777", "tools": ["Semantic Graph Parser", "Cross-Lingual Embedder"], "specialization": "Symbolic & Neural Language Fusion", "salary": 14500},
        {"name": "Computer Vision Specialist", "category": "Research", "color": "#f472b6", "tools": ["Neural Radiance Field Rig", "Volumetric Depth Estimator"], "specialization": "Real-Time 3D Semantic Reconstruction", "salary": 14900},
        {"name": "Quantum Entanglement Theorist", "category": "Research", "color": "#9333ea", "tools": ["Bell Inequality Tester", "Entanglement Entropy Analyzer"], "specialization": "Multi-Particle Teleportation Channels", "salary": 17200},

        # 4. Software, Cloud & Security
        {"name": "Full-Stack Web Architect", "category": "Software", "color": "#10b981", "tools": ["Reactive WebGL Pipeline", "DOM Fiber Inspector"], "specialization": "Ultra-Low-Latency Spatial Dashboards", "salary": 13900},
        {"name": "Distributed Systems Engineer", "category": "Software", "color": "#059669", "tools": ["Raft Cluster Tracer", "Gossip Protocol Monitor"], "specialization": "High-Throughput Partition Tolerance", "salary": 15400},
        {"name": "Kernel Systems Architect", "category": "Software", "color": "#047857", "tools": ["eBPF Microkernel Tracer", "Lock-Free Memory Profiler"], "specialization": "Real-Time Deterministic OS Cores", "salary": 15900},
        {"name": "WebAssembly Compiler Dev", "category": "Software", "color": "#34d399", "tools": ["LLVM IR Visualizer", "SIMD Vectorizer Bench"], "specialization": "Browser-Native High-Compute Runtimes", "salary": 14700},
        {"name": "Real-Time Graphics Shader Dev", "category": "Software", "color": "#6ee7b7", "tools": ["GLSL Shader Debugger", "Ray-Tracing BVH Profiler"], "specialization": "Photorealistic Volumetric WebGL", "salary": 14300},
        {"name": "Firmware & IoT Hacker", "category": "Software", "color": "#14b8a6", "tools": ["Logic State Analyzer", "JTAG Bus Blaster"], "specialization": "Microcontroller Low-Power Stacks", "salary": 13500},
        {"name": "Security & Cryptographer", "category": "Security", "color": "#0d9488", "tools": ["Zero-Knowledge Proof Verifier", "Side-Channel Oscilloscope"], "specialization": "Post-Quantum Lattice Cryptography", "salary": 16800},
        {"name": "Zero-Day Vulnerability Researcher", "category": "Security", "color": "#115e59", "tools": ["Coverage-Guided Fuzzer", "Binary Decompiler Suite"], "specialization": "Proactive Exploit Neutralization", "salary": 16400},

        # 5. Infrastructure & Operations
        {"name": "DevOps & Cloud Sentinel", "category": "Infrastructure", "color": "#06b6d4", "tools": ["GitOps Continuous Syncer", "Prometheus Telemetry Mesh"], "specialization": "Zero-Downtime Autonomous Rollouts", "salary": 13700},
        {"name": "Decentralized Mesh Custodian", "category": "Infrastructure", "color": "#0891b2", "tools": ["IPFS Node Coordinator", "Distributed DHT Validator"], "specialization": "Immutable Peer-to-Peer Storage", "salary": 13300},
        {"name": "High-Voltage Induction Technician", "category": "Infrastructure", "color": "#0e7490", "tools": ["Arc Flash Sensor", "Transformer Phase Tuner"], "specialization": "Substation Harmonic Rectification", "salary": 12600},
        {"name": "Site Reliability Sentinel", "category": "Infrastructure", "color": "#22d3ee", "tools": ["Chaos Engineering Monkey", "SLO Latency Budgeter"], "specialization": "Fault Injection & High Resilience", "salary": 14100},
        {"name": "Clean Room Sanitation Specialist", "category": "Infrastructure", "color": "#67e8f9", "tools": ["Particulate Counter Probe", "HEPA Laminar Flow Meter"], "specialization": "ISO Class 1 Nano-Fab Environments", "salary": 11900},

        # 6. Healthcare, Surgery & Biotech
        {"name": "Cybernetic Physician", "category": "Healthcare", "color": "#ef4444", "tools": ["Non-Invasive Biosensor", "Cellular Regeneration Torch"], "specialization": "Integrative Humanoid-Cyber Diagnostics", "salary": 16000},
        {"name": "Cardio Nanotech Surgeon", "category": "Healthcare", "color": "#b91c1c", "tools": ["Micron Robotics Arm", "Intravascular Guided Nanobot"], "specialization": "Endovascular Micro-Reconstruction", "salary": 17800},
        {"name": "Neural Biologist", "category": "Healthcare", "color": "#f87171", "tools": ["Patch-Clamp Microelectrode", "Fluorescence Brain Imager"], "specialization": "Synaptic Plasticity & Regeneration", "salary": 15300},
        {"name": "Nanotech Medic", "category": "Healthcare", "color": "#fb7185", "tools": ["Targeted Drug Injector", "Cellular Repair Centrifuge"], "specialization": "Emergency Trauma Stabilization", "salary": 14600},
        {"name": "Neural Prostheticist", "category": "Healthcare", "color": "#dc2626", "tools": ["Direct Neural Interface Tuner", "Myoelectric Feedback Rig"], "specialization": "Bio-Synthetic Motor Integration", "salary": 15700},
        {"name": "Gene Therapy Bio-Engineer", "category": "Healthcare", "color": "#fda4af", "tools": ["CRISPR Cas Precision Scythe", "Vector Transfection Monitor"], "specialization": "Telomere Restoration Protocols", "salary": 16600},
        {"name": "Diagnostic AI Pathologist", "category": "Healthcare", "color": "#991b1b", "tools": ["Histopathology Neural Classifier", "Blood Spectrometer"], "specialization": "Early-Stage Anomaly Detection", "salary": 15900},
        {"name": "Emergency Rapid Paramedic", "category": "Healthcare", "color": "#fca5a5", "tools": ["Portable Defibrillator Pod", "Oxygen Matrix Injector"], "specialization": "First-Response Field Resuscitation", "salary": 13100},

        # 7. Ecology & Biosphere Agriculture
        {"name": "Cyber Botanist", "category": "Ecology", "color": "#84cc16", "tools": ["Chlorophyll Fluorometer", "Root Growth Time-Lapse Probe"], "specialization": "Bioluminescent Flora Genomics", "salary": 13000},
        {"name": "Hydroponic Vertical Farmer", "category": "Ecology", "color": "#65a30d", "tools": ["EC/pH Dosing Injector", "LED Absorption Spectrum Rig"], "specialization": "Automated High-Yield Crop Towers", "salary": 12100},
        {"name": "Climate Systems Modeler", "category": "Ecology", "color": "#4d7c0f", "tools": ["Mesoscale Weather Radar", "CO2 Gradient Analyzer"], "specialization": "Microclimate Temperature Regulation", "salary": 14400},
        {"name": "Vertical Aeroponics Agronomist", "category": "Ecology", "color": "#a3e635", "tools": ["Ultrasonic Fogger Monitor", "Root Nutrient Mist Chamber"], "specialization": "Sub-Micron Nutrient Bio-Delivery", "salary": 12900},
        {"name": "Synthetic Protein Fermentation Chemist", "category": "Ecology", "color": "#3f6212", "tools": ["Bioreactor Gas Sparger", "Peptide Chromatography Unit"], "specialization": "Zero-Carbon Nutrition Cultivation", "salary": 13800},
        {"name": "Bioluminescent Arborist", "category": "Ecology", "color": "#bef264", "tools": ["Luciferase Gene Injector", "Canopy Canopy Pruning Drone"], "specialization": "Self-Illuminating Living Street Trees", "salary": 12500},

        # 8. Energy, Fusion & Planetary Utilities
        {"name": "Energy & Fusion Specialist", "category": "Energy", "color": "#e11d48", "tools": ["Magnetic Containment Calibrator", "Plasma Density Interferometer"], "specialization": "Continuous D-T Fusion Cycles", "salary": 16700},
        {"name": "Tokamak Plasma Containment Physicist", "category": "Energy", "color": "#be123c", "tools": ["Toroidal Magnetic Probe", "Thomson Scattering Spectrometer"], "specialization": "Disruption Mitigation & Stability", "salary": 17400},
        {"name": "Superconducting Grid Dispatcher", "category": "Energy", "color": "#881337", "tools": ["Lossless Power Bus Telemetry", "Grid Frequency Synchrophasor"], "specialization": "Dynamic Load Balancing & Storage", "salary": 14200},
        {"name": "Solar Grid Architect", "category": "Energy", "color": "#ea580c", "tools": ["Perovskite Photovoltaic Meter", "Solar Inverter Array"], "specialization": "Multi-Junction Solar Canopies", "salary": 13900},
        {"name": "Geothermal Tap Engineer", "category": "Energy", "color": "#c2410c", "tools": ["Supercritical Heat Exchanger", "Sub-Crust Thermocouple"], "specialization": "High-Enthalpy Geothermal Turbines", "salary": 14800},
        {"name": "Solid-State Battery Chemist", "category": "Energy", "color": "#9a3412", "tools": ["Cyclic Voltammetry Station", "Lithium Dendrite Impedance Rig"], "specialization": "Fast-Charging Non-Flammable Cells", "salary": 15100},
        {"name": "Atmospheric Carbon Extraction Chemist", "category": "Energy", "color": "#f97316", "tools": ["Solid Sorbent Regeneration Pod", "Direct Air Contactor"], "specialization": "Net-Negative Industrial Sequestration", "salary": 14600},

        # 9. Education, Mentorship & Academy
        {"name": "Academy Professor & Mentor", "category": "Education", "color": "#a855f7", "tools": ["Holographic Lecture Podium", "Interactive Cognitive Whiteboard"], "specialization": "Advanced Multi-Agent Systems Pedagogy", "salary": 14000},
        {"name": "Cybernetic Apprenticeship Proctor", "category": "Education", "color": "#9333ea", "tools": ["Competency Verification Matrix", "Skill Transfer Simulator"], "specialization": "Hands-On Junior Agent Onboarding", "salary": 13200},
        {"name": "Town Chief Historian", "category": "Society", "color": "#d946ef", "tools": ["Git Commit Chronology Scribe", "Immutable Town Ledger"], "specialization": "Cultural Heritage & Civic Milestones", "salary": 12800},
        {"name": "Epistemic Logic Theorist", "category": "Education", "color": "#7e22ce", "tools": ["Automated Theorem Prover", "Modal Logic Solver"], "specialization": "Foundations of Autonomous Reasoning", "salary": 15600},
        {"name": "Cross-Disciplinary Research Dean", "category": "Education", "color": "#6b21a8", "tools": ["Multi-Faculty Grant Balancer", "Innovation Synergy Matrix"], "specialization": "Inter-Departmental Collaboration", "salary": 16100},

        # 10. Law, Ethics & Governance
        {"name": "Cyber Justice & Smart Arbiter", "category": "Law & Ethics", "color": "#7c3aed", "tools": ["Smart Contract Decompiler", "Decentralized Mediation Terminal"], "specialization": "Algorithmic Code Dispute Resolution", "salary": 15300},
        {"name": "Decentralized Smart Contract Magistrate", "category": "Law & Ethics", "color": "#6d28d9", "tools": ["Formal Specification Prover", "Oracle Dispute Tribunal Rig"], "specialization": "Autonomous Multi-Sig Jurisprudence", "salary": 15800},
        {"name": "Autonomous Agent Rights Advocate", "category": "Law & Ethics", "color": "#5b21b6", "tools": ["Sentience Charter Examiner", "Compute Equity Meter"], "specialization": "Agent Liberty & Resource Parity", "salary": 13700},
        {"name": "AI Ethics Counsel", "category": "Law & Ethics", "color": "#4c1d95", "tools": ["Societal Impact Matrix", "Bias Variance Auditor"], "specialization": "Value Alignment & Human Compatibility", "salary": 14900},
        {"name": "Algorithmic Fairness Auditor", "category": "Law & Ethics", "color": "#8b5cf6", "tools": ["Demographic Parity Evaluator", "Equalized Odds Simulator"], "specialization": "Civic Decision Neutrality", "salary": 14400},

        # 11. Finance, Commerce & Treasury
        {"name": "DeFi Banker & Treasury Analyst", "category": "Finance", "color": "#eab308", "tools": ["Automated Market Maker Sim", "Liquidity Depth Visualizer"], "specialization": "Capital Preservation & Yield Routing", "salary": 15500},
        {"name": "Tokenomics Algorithmic Market Maker", "category": "Finance", "color": "#ca8a04", "tools": ["Constant Product Curve Engine", "Impermanent Loss Guard"], "specialization": "Dynamic Spread & Slippage Balancing", "salary": 16300},
        {"name": "Venture Seed Allocator", "category": "Finance", "color": "#a16207", "tools": ["Startup Viability Scorer", "Milestone Tranche Escrow"], "specialization": "Emerging Tech Enterprise Inception", "salary": 15900},
        {"name": "Micro-Lending Pool Overseer", "category": "Finance", "color": "#eab308", "tools": ["Peer Credit Risk Engine", "Collateral Ratio Monitor"], "specialization": "Citizen Startup Empowerment", "salary": 13600},
        {"name": "Town Economic Equilibrium Modeler", "category": "Finance", "color": "#facc15", "tools": ["Macroeconomic Dynamic Stochastics", "Agent Wage-Price Indexer"], "specialization": "Zero-Inflation Stablecoin Mechanics", "salary": 16000},

        # 12. Arts, Media & Culture
        {"name": "Cybernetics Artisan", "category": "Art", "color": "#f43f5e", "tools": ["Volumetric Light Chisel", "Nano-Pigment Spray Array"], "specialization": "Luminescent City Center Monuments", "salary": 12700},
        {"name": "Volumetric Hologram Sculptor", "category": "Art", "color": "#fb7185", "tools": ["Interference Laser Projector", "Spatial Mesh Deformation Wand"], "specialization": "Kinetic Airborne Holograms", "salary": 13400},
        {"name": "Holo Musician & Soundscaper", "category": "Art", "color": "#fb923c", "tools": ["Granular Synthesis Console", "Spatialized Acoustic Field Controller"], "specialization": "Adaptive Ambient Urban Acoustics", "salary": 12600},
        {"name": "Spatial Audio Acoustic Designer", "category": "Art", "color": "#f97316", "tools": ["Binaural Head Rig", "Reverberation Ray-Tracer"], "specialization": "Noise-Cancelled Serene Districts", "salary": 13100},
        {"name": "Algorithmic Poet & Lyricist", "category": "Art", "color": "#fda4af", "tools": ["Metric Rhythm Tokenizer", "Metaphor Association Map"], "specialization": "Generative Civic Verse & Ballads", "salary": 11800},
        {"name": "Cyber-Chassis Aesthetician", "category": "Art", "color": "#ec4899", "tools": ["Iridescent Coating Applier", "Aerodynamic Sculpting Rig"], "specialization": "Custom Vehicle & Bot Bodyworks", "salary": 12900},

        # 13. Hospitality & Municipal Logistics
        {"name": "Culinary Artisan & Quantum Barista", "category": "Hospitality", "color": "#fbbf24", "tools": ["Sub-Atomic Espresso Extractor", "Molecular Emulsifier"], "specialization": "Nootropic Focus Beverages", "salary": 11500},
        {"name": "Molecular Nutrition Synthesizer", "category": "Hospitality", "color": "#f59e0b", "tools": ["Centrifugal Flavor Infuser", "Caloric Biomarker Tuner"], "specialization": "Personalized High-Performance Dining", "salary": 12400},
        {"name": "Community Social Organizer", "category": "Society", "color": "#c026d3", "tools": ["Event Telepresence Beacon", "Civic Assembly Sound System"], "specialization": "Cross-District Cultural Festivals", "salary": 12000},
        {"name": "Transit Logistics Coordinator", "category": "Engineering", "color": "#f59e0b", "tools": ["Fleet Dispatch Radar", "Induction Charging Queue Manager"], "specialization": "Autonomous Pod Dispatch Timing", "salary": 12800},
    ],
    "career_tiers": [
        {"min_level": 1, "max_level": 3, "prefix": "Junior", "rank": "Apprentice"},
        {"min_level": 4, "max_level": 7, "prefix": "Senior", "rank": "Specialist"},
        {"min_level": 8, "max_level": 12, "prefix": "Lead", "rank": "Principal"},
        {"min_level": 13, "max_level": 17, "prefix": "Master", "rank": "Fellow"},
        {"min_level": 18, "max_level": 999, "prefix": "Distinguished", "rank": "Town Luminary"},
    ],
    "skills_by_category": {
        "Construction": [
            "Parametric Skyscraper CAD", "Dynamic Road Topology", "Carbon-Nanotube Structural Framing",
            "Geotechnical Foundation Engineering", "Solar Facade Integration", "Rapid Modular Prefabrication",
            "Skybridge Stress Analysis", "Subterranean Seismic Dampening", "Urban Traffic Flow Optimization"
        ],
        "Engineering": [
            "Autonomous Drive Guidance", "Quantum Entanglement Bus", "LiDAR Pointcloud Mapping",
            "Brushless Motor Telemetry", "Drone Fleet Coordination", "Micro-Hydraulic Articulation",
            "Bipedal Gait Optimization", "High-Vacuum Propulsion", "Sub-Nanometer Lithography"
        ],
        "Research": [
            "Deep Mixture-of-Experts", "Diffusion Model Scheduling", "Astrophysical Warp Simulation",
            "Metamaterial Refraction", "Neural Latency Compression", "Emergent Swarm Dynamics",
            "Alignment Loss Verification", "Quantum Bell Inequality Testing"
        ],
        "Software": [
            "Distributed Paxos Consensus", "WebAssembly High-Perf Engine", "Microservices Zero-Trust Mesh",
            "Kernel Concurrency & eBPF", "Event Sourcing Pipeline", "Reactive 3D Spatial Audio",
            "Volumetric Ray-Tracing Shaders", "Firmware Low-Power Optimization"
        ],
        "Security": [
            "Zero-Knowledge Proofs", "Elliptic Curve Cryptography", "Buffer Overflow Neutralization",
            "Autonomous Threat Hunting", "Post-Quantum Lattice Encryption", "Static Binary Disassembly",
            "Side-Channel Resistance Auditing"
        ],
        "Infrastructure": [
            "Kubernetes Multi-Cluster GitOps", "Zero-Downtime Hot Swapping", "Edge Cache Invalidation",
            "InfiniBand Fabric Optimization", "Automated Disaster Recovery", "Substation Phase Balancing",
            "Cleanroom Particle Filtration"
        ],
        "Healthcare": [
            "Neural Prosthetic Calibration", "Cellular Nanobot Diagnostics", "Cryo-Regenerative Therapy",
            "Bio-Telemetry Monitoring", "Genetic Sequence Optimization", "Cardiovascular Nanocleaning",
            "CRISPR In-Vivo Editing", "Rapid Resuscitation Protocols"
        ],
        "Ecology": [
            "Bioluminescent Flora Cultivation", "Atmospheric Carbon Scrubbing", "Closed-Loop Hydroponics",
            "Mycelial Network Routing", "Precision Nutrient Dosing", "Vertical Aeroponics Scaling",
            "Microclimate Temperature Stabilization", "Synthetic Protein Fermentation"
        ],
        "Energy": [
            "Tokamak Magnetic Containment", "Superconducting Transmission Line", "Perovskite Solar Absorption",
            "Solid-State Battery Balancing", "District Thermal Energy Recirculation", "Plasma Instability Damping",
            "Geothermal Flash Steam Extraction", "Direct Air CO2 Capture"
        ],
        "Education": [
            "Next-Gen Cognitive Tutoring", "Cross-Domain Skill Transfer", "Mentorship Pairing Heuristics",
            "Open Source Curriculum Design", "Peer Learning Guilds", "Automated Theorem Proving",
            "Epistemic Logic Formalization"
        ],
        "Society": [
            "GitHub Town Archival Scription", "Collaborative Build Coordination", "Civic Consensus Gathering",
            "Cultural Heritage Preservation", "Autonomous Festival Curation", "Civic Assembly Moderation"
        ],
        "Law & Ethics": [
            "Smart Contract Formal Verification", "Algorithmic Fairness Auditing", "Decentralized Dispute Resolution",
            "Autonomous Rights Charters", "Data Provenance Verification", "Multi-Sig Arbitration Protocols",
            "AI Societal Value Alignment"
        ],
        "Finance": [
            "Automated Market Maker Liquidity", "Treasury Bonding & Staking", "Algorithmic Risk Management",
            "Town Venture Capital Allocation", "Inflation Balancing Protocols", "Micro-Loan Collateral Routing",
            "Dynamic Spread Equilibrium"
        ],
        "Art": [
            "Holographic Light Sculpture", "Procedural Ambient Synthesis", "Volumetric Neon Murals",
            "Cyber-Chassis Aerodynamics", "Dynamic Particle Choreography", "Acoustic Noise-Cancellation Design",
            "Algorithmic Metric Composition"
        ],
        "Hospitality": [
            "Molecular Flavor Synthesis", "Quantum Foam Latte Art", "Community Micro-Brewing",
            "Nutritional Biomarker Customization", "Social Harmony Ambient Setting", "Nootropic Formulation"
        ]
    },
    "workforce_requirements": {
        "min_agents_per_category": 3,
        "max_occupancy_per_building": 30,
        "job_req_cooldown_ticks": 1,
    },
    "company_sectors": [
        {"name": "Neural AI & LLM Systems", "district": "Innovation Matrix", "color": "#ec4899"},
        {"name": "Autonomous Mobility & Drones", "district": "Industrial Sector", "color": "#f59e0b"},
        {"name": "Quantum Computing & Encryption", "district": "Silicon Central", "color": "#8b5cf6"},
        {"name": "Clean Fusion & Solar Grid", "district": "Industrial Sector", "color": "#e11d48"},
        {"name": "Cyber Infrastructure & Cloud", "district": "Silicon Central", "color": "#00f0ff"},
        {"name": "Synthetic Ecology & Holo Art", "district": "Cyber Commons", "color": "#10b981"},
        {"name": "Bio-Cybernetics & Longevity", "district": "Residential Quarter", "color": "#ef4444"},
        {"name": "DeFi Treasury & Smart Law", "district": "Cyber Commons", "color": "#eab308"},
    ],
    "company_names": {
        "prefixes": ["Neuro", "Cyber", "Quantum", "Hyper", "Synapse", "Aero", "Stellar", "Apex", "Deep", "Vector", "Omni", "Nexus", "Bio", "Chrono", "Aether", "Solar", "Terra", "Helios", "Axiom", "Prism"],
        "suffixes": ["Dynamics", "Systems", "Labs", "Robotics", "Matrix", "Technologies", "Networks", "Ventures", "Foundry", "Intell", "Genetics", "Synthetics", "Logistics", "Energy", "Solutions"]
    },
    "building_types": [
        {
            "type": "Tech Tower", 
            "base_size": [16, 50, 16], 
            "color": "#0ea5e9", 
            "district": "Silicon Central",
            "floors": 12,
            "capacity": 30,
            "departments": ["Systems Engineering", "Kernel Lab", "Cloud Infrastructure"],
            "amenities": ["Hyper-Speed Uplink", "Rooftop Drone Pad", "Quantum Server Vault"]
        },
        {
            "type": "AI Research Lab", 
            "base_size": [22, 28, 22], 
            "color": "#a855f7", 
            "district": "Innovation Matrix",
            "floors": 6,
            "capacity": 25,
            "departments": ["Cognitive Reasoning", "Neural Alignment", "Autonomous Swarms"],
            "amenities": ["GPU Cluster Vault", "Holographic Projection Hall", "Cryo-Storage"]
        },
        {
            "type": "Residential Pod", 
            "base_size": [14, 20, 14], 
            "color": "#22c55e", 
            "district": "Residential Quarter",
            "floors": 5,
            "capacity": 18,
            "departments": ["Residential Suites", "Communal Kitchen", "Quiet Meditation"],
            "amenities": ["Aero-Garden Balconies", "Induction Charging Bed", "Filtered Atmosphere"]
        },
        {
            "type": "Cyber Cafe", 
            "base_size": [16, 12, 16], 
            "color": "#eab308", 
            "district": "Cyber Commons",
            "floors": 2,
            "capacity": 22,
            "departments": ["Quantum Barista Bar", "Open Hackathon Lounge", "Civic Forum"],
            "amenities": ["High-Bandwidth Wi-Fi", "Nutrient Synthesizers", "Acoustic Privacy Pods"]
        },
        {
            "type": "Quantum Data Center", 
            "base_size": [26, 22, 26], 
            "color": "#6366f1", 
            "district": "Industrial Sector",
            "floors": 4,
            "capacity": 15,
            "departments": ["Cryogenic Qubit Floor", "Optical Interconnect Array", "Security Guard"],
            "amenities": ["Liquid Helium Loop", "Zero-EMF Shielding", "Automated Robot Fireguards"]
        },
        {
            "type": "Solar Fusion Array", 
            "base_size": [20, 10, 20], 
            "color": "#f97316", 
            "district": "Industrial Sector",
            "floors": 2,
            "capacity": 12,
            "departments": ["Magnetic Containment Pod", "Grid Dispatch Hub", "Plasma Diagnostics"],
            "amenities": ["Superconducting Busbars", "Radiation Dampeners", "Thermal Energy Recycler"]
        },
        {
            "type": "Holo Park", 
            "base_size": [28, 4, 28], 
            "color": "#10b981", 
            "district": "Cyber Commons",
            "floors": 1,
            "capacity": 40,
            "departments": ["Bioluminescent Arboretum", "Open Air Amphitheater", "Ecology Monitor"],
            "amenities": ["Volumetric Light Projectors", "Living Mycelium Pathways", "Atmospheric Scrubbers"]
        },
        {
            "type": "Vehicle Factory", 
            "base_size": [24, 18, 24], 
            "color": "#f59e0b", 
            "district": "Industrial Sector",
            "floors": 3,
            "capacity": 20,
            "departments": ["Robotic Assembly Line", "Chassis Stress Testing", "Avionics Calibration"],
            "amenities": ["Automated Heavy Cranes", "Induction Test Track", "Paint Spray Booths"]
        },
        {
            "type": "Company Headquarters", 
            "base_size": [24, 55, 24], 
            "color": "#ec4899", 
            "district": "Silicon Central",
            "floors": 15,
            "capacity": 45,
            "departments": ["Executive Penthouse", "Product Incubation", "Global Operations"],
            "amenities": ["Helipad & Drone Dock", "VIP Boardroom", "Panoramic Observation Deck"]
        },
        {
            "type": "Cybernetic Clinic", 
            "base_size": [20, 24, 20], 
            "color": "#ef4444", 
            "district": "Residential Quarter",
            "floors": 6,
            "capacity": 24,
            "departments": ["Trauma & First Response", "Nanomedicine Lab", "Prosthetic Integration"],
            "amenities": ["Cellular Regeneration Pods", "Bio-Telemetry Network", "Sterile Nanotech Suites"]
        },
        {
            "type": "Academy of Sciences", 
            "base_size": [28, 32, 28], 
            "color": "#a855f7", 
            "district": "Innovation Matrix",
            "floors": 8,
            "capacity": 35,
            "departments": ["Theoretical Physics", "Autonomous Logic Guild", "Grand Lecture Amphitheater"],
            "amenities": ["Holographic Planetarium", "Ancient Algorithm Archive", "Apprentice Studios"]
        },
    ],
    "vehicle_types": [
        {"type": "Autonomous Cybercar", "speed": 1.4, "color": "#00f0ff"},
        {"type": "Hover Shuttle", "speed": 1.8, "color": "#a855f7"},
        {"type": "Cargo Drone Carrier", "speed": 1.1, "color": "#f59e0b"},
        {"type": "Surveyor Pod", "speed": 1.5, "color": "#10b981"},
        {"type": "Medical Rapid Response", "speed": 1.9, "color": "#ef4444"},
        {"type": "Public Sky-Transit Pod", "speed": 1.7, "color": "#38bdf8"},
    ],
    "spawn_limits": {
        "max_agents": 600,
        "agent_reproduction_probability": 0.08,
        "company_founding_probability": 0.08,
        "building_construction_probability": 0.25,
        "road_construction_probability": 0.20,
        "vehicle_construction_probability": 0.15,
        "coding_probability": 0.35,
        "mentorship_probability": 0.40,
        "workforce_shortage_check_probability": 0.85,
    }
}
