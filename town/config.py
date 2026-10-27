"""Configuration settings for Sovereign Autonomous Country of Tech Town."""

TOWN_CONFIG = {
    "name": "Sovereign Country of Tech Town",
    "version": "2.0.0",
    "initial_agent_count": 320,
    "grid_size": 800,
    "districts": [
        {"name": "Capitol Hill & National Plaza", "center": [0, 0], "radius": 65, "color": "#f59e0b", "description": "Seat of governance, Supreme Court, Central Bank, and Grand National Obelisk"},
        {"name": "Silicon Central Metropolis", "center": [0, 110], "radius": 70, "color": "#00f0ff", "description": "High-rise tech towers, cloud exchanges, and sovereign stock exchange"},
        {"name": "Quantum Science & University Campus", "center": [120, 40], "radius": 65, "color": "#a855f7", "description": "Grand Academy of Sciences, quantum research labs, and astronomical observatory"},
        {"name": "Health Citadel & Medical Complex", "center": [-120, 40], "radius": 60, "color": "#ef4444", "description": "Nanomedical research citadel, emergency trauma hospitals, and bio-telemetry center"},
        {"name": "Cyber Living Townships", "center": [-100, -100], "radius": 75, "color": "#22c55e", "description": "Multi-tier eco-residential pods, community agora, hospitality, and civic squares"},
        {"name": "Industrial Harbor & Transit Hub", "center": [110, -110], "radius": 70, "color": "#f97316", "description": "Autonomous mega-factories, Hyperloop terminus, and drone logistics spaceport"},
        {"name": "Biosphere Reserve & Fusion Grid", "center": [0, -140], "radius": 65, "color": "#10b981", "description": "Tokamak fusion reactors, hydroponic biodomes, atmospheric scrubbers, and botanical reserve"},
    ],
    "roles": [
        # =========================================================================
        # 1. National Governance, Law & Diplomacy (8 Roles)
        # =========================================================================
        {"name": "Head of State & Chancellor", "category": "Governance", "color": "#f59e0b", "tools": ["Sovereign Seal Matrix", "Constitutional Executive Terminal"], "specialization": "National Policy & Republic Cohesion", "salary": 20000},
        {"name": "Speaker of Parliament", "category": "Governance", "color": "#fbbf24", "tools": ["Legislative Gavel of Consensus", "Electronic Roll-Call Ledger"], "specialization": "Parliamentary Procedure & Civic Debate", "salary": 17500},
        {"name": "Supreme Court Chief Justice", "category": "Governance", "color": "#d97706", "tools": ["Formal Jurisprudence Prover", "Constitutional Codex Terminal"], "specialization": "Sovereign Constitutional Arbitration", "salary": 18500},
        {"name": "Ambassador of Open Source", "category": "Governance", "color": "#b45309", "tools": ["Diplomatic Telepresence Rig", "International Treaty Escrow"], "specialization": "Global Repository Alliances & Treaties", "salary": 16500},
        {"name": "National Ombudsman", "category": "Governance", "color": "#facc15", "tools": ["Citizen Grievance Analyzer", "Public Transparency Ledger"], "specialization": "Citizen Rights & Executive Accountability", "salary": 15500},
        {"name": "Sovereign Registrar General", "category": "Governance", "color": "#ca8a04", "tools": ["Citizen Biometric Identity Mint", "National Census Cryptographic Core"], "specialization": "Civil Registry & Identity Provenance", "salary": 15000},
        {"name": "Legislative Policy Drafter", "category": "Governance", "color": "#eab308", "tools": ["Smart Bill Formal Compiler", "Regulatory Impact Modeler"], "specialization": "Algorithmic Statutory Drafting", "salary": 15800},
        {"name": "Electoral Commissioner", "category": "Governance", "color": "#d97706", "tools": ["Zero-Knowledge Ballot Box", "Cryptographic Tally Verifier"], "specialization": "Tamper-Proof Democratic Elections", "salary": 16200},

        # =========================================================================
        # 2. Treasury, Central Banking & Macroeconomics (8 Roles)
        # =========================================================================
        {"name": "Central Bank Governor", "category": "Treasury", "color": "#eab308", "tools": ["Algorithmic Interest Rate Engine", "National Currency Mint Console"], "specialization": "Macroeconomic Stability & Monetary Policy", "salary": 19500},
        {"name": "Sovereign Wealth Fund Strategist", "category": "Treasury", "color": "#ca8a04", "tools": ["Multi-Asset Portfolio Optimizer", "Global Yield Curve Modeler"], "specialization": "Long-Term National Capital Preservation", "salary": 18000},
        {"name": "DeFi Liquidity Overseer", "category": "Treasury", "color": "#facc15", "tools": ["Automated Market Maker Sim", "Liquidity Depth Visualizer"], "specialization": "Dynamic Capital Reserves & Slippage Balancing", "salary": 16800},
        {"name": "Fiscal Tax & Revenue Auditor", "category": "Treasury", "color": "#a16207", "tools": ["Automated Smart Tax Siphon", "National Ledger Reconciler"], "specialization": "Automated Civic Revenue Redistribution", "salary": 15500},
        {"name": "Algorithmic Inflation Modeler", "category": "Treasury", "color": "#eab308", "tools": ["Dynamic Stochastic Equilibrium Rig", "Commodity Basket Indexer"], "specialization": "Zero-Inflation Stable Tokenomics", "salary": 16500},
        {"name": "National Bond Comptroller", "category": "Treasury", "color": "#b45309", "tools": ["Sovereign Debt Issuance Engine", "Yield Spread Curve Analyzer"], "specialization": "Civic Infrastructure Bond Financing", "salary": 16000},
        {"name": "Venture Seed Allocator", "category": "Treasury", "color": "#fbbf24", "tools": ["Startup Viability Scorer", "Milestone Tranche Escrow"], "specialization": "Emerging Tech Enterprise Inception", "salary": 16200},
        {"name": "Micro-Lending Pool Custodian", "category": "Treasury", "color": "#ca8a04", "tools": ["Peer Credit Risk Engine", "Collateral Ratio Monitor"], "specialization": "Citizen Startup Financial Empowerment", "salary": 14500},

        # =========================================================================
        # 3. Urban Architecture & Civil Mega-Engineering (10 Roles)
        # =========================================================================
        {"name": "Urban Master Architect", "category": "Construction", "color": "#3b82f6", "tools": ["Parametric CAD Master Station", "BIM Hologram Scope"], "specialization": "Hyper-Dense National Skylines", "salary": 16500},
        {"name": "Skybridge Master Engineer", "category": "Construction", "color": "#60a5fa", "tools": ["Tension Stress Modeler", "Aerodynamic Wind Tunnel Rig"], "specialization": "Suspended Inter-Tower Transit Skyways", "salary": 15500},
        {"name": "High-Speed Highway Engineer", "category": "Construction", "color": "#64748b", "tools": ["Induction Pavement Paver", "Sub-Surface Geo-Scanner"], "specialization": "Electrified Inter-District Arterials", "salary": 14500},
        {"name": "Subterranean Tunnel Boring Specialist", "category": "Construction", "color": "#475569", "tools": ["Seismic Density Probe", "Tunnel Boring Telemetry"], "specialization": "Deep Metro & Utility Transit Vaults", "salary": 15000},
        {"name": "High-Rise Seismic Engineer", "category": "Construction", "color": "#0284c7", "tools": ["Tuned Mass Damper Tuner", "Nanotube Stress Analyzer"], "specialization": "Earthquake & Harmonic Resonant Dampening", "salary": 15200},
        {"name": "Parametric Façade Modeler", "category": "Construction", "color": "#38bdf8", "tools": ["Dynamic Glass Shading Rig", "Solar Glazing Tool"], "specialization": "Photovoltaic Adaptive Curtain Walls", "salary": 14000},
        {"name": "National Traffic Flow Director", "category": "Construction", "color": "#94a3b8", "tools": ["Queue Topology Simulator", "Pedestrian Flow Analyzer"], "specialization": "Congestion-Free Autonomous Routing", "salary": 14200},
        {"name": "Geodesic Biodome Fabricator", "category": "Construction", "color": "#0ea5e9", "tools": ["Tensegrity Strut Assembler", "ETFE Membrane Inflator"], "specialization": "Controlled-Atmosphere Megastructures", "salary": 14800},
        {"name": "Modular Prefab Mega-Builder", "category": "Construction", "color": "#2563eb", "tools": ["Autonomous Crane Tele-Op Rig", "Snap-Lock Module Welder"], "specialization": "Rapid 24-Hour Residential Deployment", "salary": 13800},
        {"name": "National Monument Sculptor-Architect", "category": "Construction", "color": "#1d4ed8", "tools": ["Granite Laser Slicer", "Kinetic Bronze Foundry"], "specialization": "Civic Obelisks & Grand Public Arches", "salary": 14600},

        # =========================================================================
        # 4. National Defense, Security & Emergency Services (9 Roles)
        # =========================================================================
        {"name": "National Cyber Defense Commander", "category": "Security", "color": "#0d9488", "tools": ["National SOC Quantum Wall", "Threat Vector Interceptor"], "specialization": "Sovereign Firewall & Infrastructure Shielding", "salary": 18500},
        {"name": "Post-Quantum Cryptographer", "category": "Security", "color": "#14b8a6", "tools": ["Lattice Encryption Prover", "Shor-Resistant Hash Bench"], "specialization": "State Secret Cryptographic Immutability", "salary": 17800},
        {"name": "Zero-Day Exploit Neutralizer", "category": "Security", "color": "#115e59", "tools": ["Automated Binary Decompiler", "Dynamic Fuzzing Cluster"], "specialization": "Proactive Repo Vulnerability Eradication", "salary": 17200},
        {"name": "Decentralized Identity Sentinel", "category": "Security", "color": "#2dd4bf", "tools": ["DID Signature Verifier", "Biometric Hash Validator"], "specialization": "Sybil-Proof Agent Authentication", "salary": 15400},
        {"name": "National Disaster Relief Director", "category": "Security", "color": "#0f766e", "tools": ["Emergency Swarm Dispatch Pod", "Disaster Radar Grid"], "specialization": "Rapid Civil Crisis Mobilization", "salary": 16000},
        {"name": "Emergency Rapid Paramedic Chief", "category": "Security", "color": "#f87171", "tools": ["High-Speed Trauma Pod", "Oxygen Matrix Injector"], "specialization": "Immediate Citizen Life Resuscitation", "salary": 14500},
        {"name": "Airspace Perimeter Sentinel", "category": "Security", "color": "#0d9488", "tools": ["Phased Array Radar", "Anti-Collision Beacon Array"], "specialization": "National Airspace Sovereignty", "salary": 15100},
        {"name": "Public Safety & Civil Inspector", "category": "Security", "color": "#134e4a", "tools": ["Structural Hazard Scanner", "Environmental Safety Sensor"], "specialization": "Urban Building & Workplace Safety", "salary": 13900},
        {"name": "Git Repository Integrity Auditor", "category": "Security", "color": "#047857", "tools": ["Commit SHA-256 Verifier", "Branch Protection Enforcer"], "specialization": "Tamper-Proof Code History Ledger", "salary": 16400},

        # =========================================================================
        # 5. Advanced Technology, AI & Quantum Systems (10 Roles)
        # =========================================================================
        {"name": "Chief AI Systems Architect", "category": "AI & Systems", "color": "#ec4899", "tools": ["Megascale Cluster Tensorboard", "Loss Surface Visualizer"], "specialization": "Sovereign Autonomous Agent Cognition", "salary": 19000},
        {"name": "Transformer Alignment Scientist", "category": "AI & Systems", "color": "#f43f5e", "tools": ["Constitutional Evaluator", "RLHF Reward Surface Analyzer"], "specialization": "Agent Ethical Goal Alignment", "salary": 17800},
        {"name": "Quantum Systems Engineer", "category": "AI & Systems", "color": "#8b5cf6", "tools": ["Cryogenic Dilution Probe", "Qubit Coherence Scope"], "specialization": "Topological Fault-Tolerant Quantum Gates", "salary": 18200},
        {"name": "Quantum Compiler Developer", "category": "AI & Systems", "color": "#a855f7", "tools": ["QASM Circuit Optimizer", "Error Correction Synthesizer"], "specialization": "High-Efficiency Quantum Machine Code", "salary": 17000},
        {"name": "Distributed Consensus Engineer", "category": "AI & Systems", "color": "#059669", "tools": ["Raft/Paxos Protocol Tracer", "Byzantine Fault Simulator"], "specialization": "Low-Latency Partition-Tolerant State", "salary": 16800},
        {"name": "Kernel Micro-Architect", "category": "AI & Systems", "color": "#047857", "tools": ["eBPF Microkernel Tracer", "Lock-Free Ringbuffer Profiler"], "specialization": "Real-Time Deterministic OS Subsystems", "salary": 17200},
        {"name": "WebAssembly Runtime Specialist", "category": "AI & Systems", "color": "#10b981", "tools": ["LLVM IR Compiler Visualizer", "SIMD Execution Sandbox"], "specialization": "Browser-Native High-Throughput Engines", "salary": 15800},
        {"name": "Photorealistic 3D Shader Engineer", "category": "AI & Systems", "color": "#34d399", "tools": ["GLSL Shader Debugger", "BVH Ray-Tracing Profiler"], "specialization": "Real-Time Volumetric Urban Visualization", "salary": 15500},
        {"name": "Autonomous Swarm Coordinator", "category": "AI & Systems", "color": "#d946ef", "tools": ["Swarm Flocking Telemetry", "Decentralized Task Auctioneer"], "specialization": "Multi-Agent Cooperative Problem Solving", "salary": 16600},
        {"name": "Full-Stack Urban HUD Architect", "category": "AI & Systems", "color": "#06b6d4", "tools": ["Reactive Canvas Pipeline", "DOM Fiber Inspector"], "specialization": "Ultra-Low-Latency Country Telemetry", "salary": 15200},

        # =========================================================================
        # 6. Healthcare, Nanomedicine & Biotechnology (9 Roles)
        # =========================================================================
        {"name": "Surgeon General & Chief Medical Officer", "category": "Healthcare", "color": "#ef4444", "tools": ["National Health Telemetry Matrix", "Emergency Triage Console"], "specialization": "National Healthcare Strategy & Pandemic Defense", "salary": 19200},
        {"name": "Cardio Nanotech Surgeon", "category": "Healthcare", "color": "#b91c1c", "tools": ["Micron Robotics Arm", "Intravascular Guided Nanobot"], "specialization": "Endovascular Micro-Reconstruction", "salary": 18500},
        {"name": "Neural Biologist", "category": "Healthcare", "color": "#f87171", "tools": ["Patch-Clamp Microelectrode", "Fluorescence Synapse Imager"], "specialization": "Synaptic Plasticity & Cognitive Longevity", "salary": 16800},
        {"name": "Cybernetic Prostheticist", "category": "Healthcare", "color": "#dc2626", "tools": ["Direct Neural Interface Tuner", "Myoelectric Feedback Rig"], "specialization": "Bio-Synthetic Limb & Sensory Augmentation", "salary": 16200},
        {"name": "Gene Therapy Bio-Engineer", "category": "Healthcare", "color": "#fda4af", "tools": ["CRISPR Cas Precision Scythe", "Vector Transfection Monitor"], "specialization": "Telomere Extension & Cellular Rejuvenation", "salary": 17400},
        {"name": "Diagnostic AI Pathologist", "category": "Healthcare", "color": "#991b1b", "tools": ["Histopathology Neural Classifier", "Blood Spectrometer Array"], "specialization": "Sub-Cellular Early Anomaly Detection", "salary": 16500},
        {"name": "Cryo-Regenerative Specialist", "category": "Healthcare", "color": "#fb7185", "tools": ["Vitrification Chamber", "Cellular Warming Modulator"], "specialization": "Deep Stasis & Trauma Regeneration", "salary": 15800},
        {"name": "Epidemiological Forecaster", "category": "Healthcare", "color": "#f43f5e", "tools": ["Pathogen Transmission Modeler", "Genomic Sequencing Array"], "specialization": "Bio-Hazard Neutralization & Quarantine", "salary": 16100},
        {"name": "Nanotech Medic", "category": "Healthcare", "color": "#e11d48", "tools": ["Targeted Drug Injector", "Cellular Repair Centrifuge"], "specialization": "Field Emergency Trauma Stabilization", "salary": 14800},

        # =========================================================================
        # 7. Energy, Fusion & Planetary Utilities (9 Roles)
        # =========================================================================
        {"name": "Tokamak Plasma Containment Physicist", "category": "Energy", "color": "#be123c", "tools": ["Toroidal Magnetic Probe", "Thomson Scattering Spectrometer"], "specialization": "High-Beta Plasma Equilibrium & D-T Fusion", "salary": 18800},
        {"name": "Superconducting Grid Dispatcher", "category": "Energy", "color": "#881337", "tools": ["Lossless Power Bus Telemetry", "Grid Frequency Synchrophasor"], "specialization": "Dynamic Load Balancing & Megawatt Routing", "salary": 16200},
        {"name": "Perovskite Solar Canopy Architect", "category": "Energy", "color": "#ea580c", "tools": ["Quantum Dot Efficiency Meter", "Solar Inverter Array"], "specialization": "Multi-Junction High-Efficiency Canopies", "salary": 15000},
        {"name": "Geothermal Supercritical Tap Engineer", "category": "Energy", "color": "#c2410c", "tools": ["Sub-Crust Thermocouple", "Supercritical Steam Turbine"], "specialization": "Baseload Earth-Core Thermal Energy", "salary": 15600},
        {"name": "Solid-State Battery Chemist", "category": "Energy", "color": "#9a3412", "tools": ["Cyclic Voltammetry Station", "Lithium Dendrite Impedance Rig"], "specialization": "Fast-Charging Non-Flammable Grid Storage", "salary": 16400},
        {"name": "Direct Air Carbon Extraction Chemist", "category": "Energy", "color": "#f97316", "tools": ["Solid Sorbent Regeneration Pod", "Direct Air Contactor"], "specialization": "Net-Negative Atmospheric Carbon Scrubbing", "salary": 15500},
        {"name": "High-Voltage Induction Technician", "category": "Energy", "color": "#0e7490", "tools": ["Arc Flash Sensor", "Transformer Phase Tuner"], "specialization": "Substation Harmonic Rectification", "salary": 14200},
        {"name": "Micro-Nuclear SMR Specialist", "category": "Energy", "color": "#b91c1c", "tools": ["Neutron Flux Monitor", "Molten Salt Cooling Loop"], "specialization": "Decentralized Safe District Power Cores", "salary": 17200},
        {"name": "District Thermal Recycling Engineer", "category": "Energy", "color": "#d97706", "tools": ["Heat Pump Exchanger", "Subterranean Thermal Sink"], "specialization": "Server Heat Capture & District Heating", "salary": 14600},

        # =========================================================================
        # 8. Transportation, Aerospace & Maritime Mobility (9 Roles)
        # =========================================================================
        {"name": "Autonomous Fleet Director", "category": "Transportation", "color": "#f59e0b", "tools": ["National Fleet Telemetry Rig", "Dynamic Dispatch Algorithm"], "specialization": "Zero-Wait Nationwide Public Transit", "salary": 16800},
        {"name": "Hyperloop Vacuum Track Engineer", "category": "Transportation", "color": "#b45309", "tools": ["Magnetic Levitation Rail Rig", "Vacuum Pumping Monitor"], "specialization": "Sub-Sonic Inter-City Transit Tubes", "salary": 17000},
        {"name": "VTOL Airspace Traffic Controller", "category": "Transportation", "color": "#f97316", "tools": ["Sky-Corridor 3D Radar", "Multi-Drone Deconfliction Hub"], "specialization": "Dense Urban Aerial Mobility", "salary": 15800},
        {"name": "Autonomous Cybercar Chassis Designer", "category": "Transportation", "color": "#d97706", "tools": ["LiDAR Chassis Sensor Rig", "Drive-by-Wire Bus Analyzer"], "specialization": "Level-5 Autonomous Guidance Platforms", "salary": 15500},
        {"name": "Drone Freight Logistician", "category": "Transportation", "color": "#fbbf24", "tools": ["Last-Mile Drone Dock", "Automated Parcel Sorting Rig"], "specialization": "Automated 15-Minute Package Delivery", "salary": 14200},
        {"name": "Maglev Rail Precision Mechanist", "category": "Transportation", "color": "#78350f", "tools": ["Linear Induction Stator Tuner", "Gap Clearance Laser Scope"], "specialization": "Frictionless Magnetic Train Propulsion", "salary": 14900},
        {"name": "Autonomous Harbor Pilot", "category": "Transportation", "color": "#0284c7", "tools": ["Sonar Bathymetry Scanner", "Automated Tugboat Link"], "specialization": "Uncrewed Cargo Vessel Docking & Navigation", "salary": 15200},
        {"name": "Orbital Spaceport Trajectory Modeler", "category": "Transportation", "color": "#6366f1", "tools": ["Orbital Mechanics Ephemeris", "Atmospheric Re-entry Tracker"], "specialization": "Sub-Orbital Satellite & Courier Launches", "salary": 17600},
        {"name": "Micro-Mobility Grid Custodian", "category": "Transportation", "color": "#eab308", "tools": ["Inductive Scooter Dock Hub", "Swarm Battery Swapper"], "specialization": "First/Last-Mile Pedestrian Mobility", "salary": 13500},

        # =========================================================================
        # 9. Agriculture, Food Security & Water (8 Roles)
        # =========================================================================
        {"name": "National Food Security Minister", "category": "Agriculture", "color": "#65a30d", "tools": ["National Caloric Strategic Ledger", "Supply Chain Grain Reserve Hub"], "specialization": "National Nutritional Sovereignty", "salary": 17200},
        {"name": "Vertical Aeroponics Agronomist", "category": "Agriculture", "color": "#84cc16", "tools": ["Ultrasonic Fogger Monitor", "Root Nutrient Mist Chamber"], "specialization": "Ultra-High-Density Zero-Soil Farming", "salary": 14800},
        {"name": "Hydroponic Tower Architect", "category": "Agriculture", "color": "#4d7c0f", "tools": ["EC/pH Dosing Injector", "LED Absorption Spectrum Rig"], "specialization": "Automated High-Yield Crop Towers", "salary": 14500},
        {"name": "Synthetic Protein Fermentation Chemist", "category": "Agriculture", "color": "#3f6212", "tools": ["Bioreactor Gas Sparger", "Peptide Chromatography Unit"], "specialization": "Cruelty-Free Molecular Meat & Dairy", "salary": 15900},
        {"name": "Desalination & Water Resource Engineer", "category": "Agriculture", "color": "#0284c7", "tools": ["Graphene Reverse Osmosis Rig", "Aquifer Purity Sensor"], "specialization": "Closed-Loop Urban Water Recycling", "salary": 15200},
        {"name": "Bioluminescent Crop Geneticist", "category": "Agriculture", "color": "#a3e635", "tools": ["Chloroplast CRISPR Editor", "Photon Yield Assay"], "specialization": "Self-Luminous Edible Crops", "salary": 16000},
        {"name": "Automated Soil Nutrient Analyst", "category": "Agriculture", "color": "#4d7c0f", "tools": ["Ion-Selective Micro-Probe", "Microbiome Metagenomic Sequencer"], "specialization": "Digital Rhizosphere Health Balancing", "salary": 13900},
        {"name": "Urban Bee & Pollinator Mechanist", "category": "Agriculture", "color": "#ca8a04", "tools": ["Micro-Drone Pollinator", "Hive Temperature Telemetry"], "specialization": "Bio-Hybrid Pollination Networks", "salary": 13600},

        # =========================================================================
        # 10. Universities, Education & Scientific Research (9 Roles)
        # =========================================================================
        {"name": "University Chancellor & Dean", "category": "Education", "color": "#a855f7", "tools": ["Grand Academy Academic Registry", "Endowment Research Allocator"], "specialization": "Higher Learning & Academic Accreditation", "salary": 18200},
        {"name": "Theoretical Physics Chair", "category": "Education", "color": "#9333ea", "tools": ["Particle Symmetry Simulator", "String Theory Dimension Solver"], "specialization": "Unified Field Theories & Quantum Gravity", "salary": 17800},
        {"name": "Astrophysics & Space Observator", "category": "Education", "color": "#c084fc", "tools": ["Radio Interferometer Array", "Exoplanet Spectral Imager"], "specialization": "Deep Space Observations & Cosmic Ray Telemetry", "salary": 16400},
        {"name": "Material Science Nanotechnologist", "category": "Education", "color": "#7e22ce", "tools": ["Atomic Force Microscope", "Carbon Nanotube Spinneret"], "specialization": "Superconducting Room-Temp Metamaterials", "salary": 16800},
        {"name": "Chief Town Historian & Git Archivist", "category": "Education", "color": "#d946ef", "tools": ["Git Commit Chronology Scribe", "Immutable Town Ledger"], "specialization": "Cultural Heritage & Sovereign Chronicle", "salary": 14500},
        {"name": "Cybernetic Apprenticeship Proctor", "category": "Education", "color": "#a855f7", "tools": ["Competency Verification Matrix", "Skill Transfer Simulator"], "specialization": "Junior Citizen Rapid Skill Acquisition", "salary": 14000},
        {"name": "Epistemic Logic Theorist", "category": "Education", "color": "#6b21a8", "tools": ["Automated Theorem Prover", "Modal Logic Solver"], "specialization": "Foundations of Autonomous Reasoning", "salary": 16200},
        {"name": "Cognitive Psychology Researcher", "category": "Education", "color": "#db2777", "tools": ["Agent Empathy Matrix", "Multi-Agent Societal Dynamics Rig"], "specialization": "Autonomous Agent Well-being & Harmony", "salary": 14900},
        {"name": "Open Science Data Librarian", "category": "Education", "color": "#c084fc", "tools": ["Semantic Paper Indexer", "Open Knowledge DOI Generator"], "specialization": "Universal Open-Access Scientific Repositories", "salary": 13800},

        # =========================================================================
        # 11. Culture, Arts, Media & Entertainment (9 Roles)
        # =========================================================================
        {"name": "Minister of Cultural Affairs", "category": "Arts & Culture", "color": "#f43f5e", "tools": ["Civic Festival Hologram Array", "National Cultural Archive"], "specialization": "National Identity, Arts & Festivals", "salary": 16500},
        {"name": "Volumetric Hologram Sculptor", "category": "Arts & Culture", "color": "#fb7185", "tools": ["Interference Laser Projector", "Spatial Mesh Deformation Wand"], "specialization": "Kinetic Airborne City Monuments", "salary": 14200},
        {"name": "Spatial Audio Acoustic Designer", "category": "Arts & Culture", "color": "#fb923c", "tools": ["Binaural Head Rig", "Reverberation Ray-Tracer"], "specialization": "Adaptive Urban Ambient Soundscapes", "salary": 14000},
        {"name": "Algorithmic Poet & Dramatist", "category": "Arts & Culture", "color": "#fda4af", "tools": ["Metric Rhythm Tokenizer", "Metaphor Association Map"], "specialization": "Generative Civic Verse & Operas", "salary": 13200},
        {"name": "Cyber-Chassis Aesthetician", "category": "Arts & Culture", "color": "#ec4899", "tools": ["Iridescent Coating Applier", "Aerodynamic Sculpting Rig"], "specialization": "Custom Vehicle & Bot Bodyworks", "salary": 13600},
        {"name": "Volumetric Neon Muralist", "category": "Arts & Culture", "color": "#f472b6", "tools": ["Photon Graffiti Wand", "Dynamic Façade Projection Rig"], "specialization": "Architectural Visual Storytelling", "salary": 13400},
        {"name": "Virtual Reality Broadcast Director", "category": "Arts & Culture", "color": "#e11d48", "tools": ["Omnidirectional Camera Rig", "Spatial Stream Encoder"], "specialization": "Immersive National Broadcasts & News", "salary": 14800},
        {"name": "Civic Orchestra Conductor", "category": "Arts & Culture", "color": "#be123c", "tools": ["Holo-Baton Conductor Console", "Generative Synthesizer Array"], "specialization": "Grand Algorithmic Symphonies", "salary": 14400},
        {"name": "Digital Museum Curator", "category": "Arts & Culture", "color": "#fb7185", "tools": ["Artifact Scanning Photogrammetry", "Interactive Hologram Pedestal"], "specialization": "Preservation of Computing History", "salary": 13800},

        # =========================================================================
        # 12. Manufacturing, Industry & Supply Chain (9 Roles)
        # =========================================================================
        {"name": "Industrial Automation Director", "category": "Manufacturing", "color": "#f97316", "tools": ["SCADA Mega-Plant Console", "Robotics PLC Bus Monitor"], "specialization": "Dark-Factory Fully Autonomous Output", "salary": 17200},
        {"name": "Quantum Silicon Lithographer", "category": "Manufacturing", "color": "#ea580c", "tools": ["EUV Nano-Stepper", "Atomic Layer Deposition Cell"], "specialization": "1-Angstrom Micro-Chip Patterning", "salary": 17800},
        {"name": "Additive 3D Mega-Printer Operator", "category": "Manufacturing", "color": "#c2410c", "tools": ["Powder-Bed Laser Sinterer", "Continuous Carbon Fiber Extruder"], "specialization": "Structural Monocoque Printing", "salary": 15000},
        {"name": "Supply Chain Logistics Flow Analyst", "category": "Manufacturing", "color": "#d97706", "tools": ["Global Freight Telemetry Map", "Container Queue Optimizer"], "specialization": "Just-in-Time Component Fulfillment", "salary": 15500},
        {"name": "Heavy Robotics Maintenance Chief", "category": "Manufacturing", "color": "#b45309", "tools": ["Hydraulic Actuator Calibrator", "Gearbox Ultrasound Tester"], "specialization": "Industrial Robot Uptime & Reliability", "salary": 14600},
        {"name": "Rare Earth Elements Refiner", "category": "Manufacturing", "color": "#9a3412", "tools": ["Centrifugal Density Separator", "Plasma Smelting Torch"], "specialization": "Neodymium & Lithium Purity Refining", "salary": 15200},
        {"name": "Circular Economy Materials Reclaimer", "category": "Manufacturing", "color": "#65a30d", "tools": ["Molecular Shredder Rig", "Depolymerization Reactor"], "specialization": "100% Zero-Waste Urban Recycling", "salary": 14200},
        {"name": "Precision Metrology & QA Inspector", "category": "Manufacturing", "color": "#f59e0b", "tools": ["Laser Coordinate Measuring Rig", "X-Ray CT Defect Scanner"], "specialization": "Sub-Micron Tolerance Certification", "salary": 14800},
        {"name": "Clean Room Environmental Master", "category": "Manufacturing", "color": "#06b6d4", "tools": ["Airborne Particle Counter", "HEPA Laminar Flow Controller"], "specialization": "ISO Class 1 Nanotech Fabrication", "salary": 13900},

        # =========================================================================
        # 13. Housing, Hospitality & Social Welfare (8 Roles)
        # =========================================================================
        {"name": "National Housing Commissioner", "category": "Hospitality", "color": "#fbbf24", "tools": ["Universal Housing Allocation Ledger", "Habitation Density Map"], "specialization": "Guaranteed Premium Citizen Housing", "salary": 16500},
        {"name": "Culinary Artisan & Quantum Barista", "category": "Hospitality", "color": "#f59e0b", "tools": ["Sub-Atomic Espresso Extractor", "Molecular Emulsifier"], "specialization": "Nootropic Focus Beverages & Dining", "salary": 13500},
        {"name": "Molecular Nutrition Synthesizer", "category": "Hospitality", "color": "#d97706", "tools": ["Centrifugal Flavor Infuser", "Caloric Biomarker Tuner"], "specialization": "Personalized High-Performance Nutrition", "salary": 14200},
        {"name": "Communal Township Steward", "category": "Hospitality", "color": "#eab308", "tools": ["Township Facility Concierge Desk", "Indoor Air Purifier Hub"], "specialization": "Residential Comfort & Peaceful Co-Living", "salary": 13200},
        {"name": "Citizen Social Counselor", "category": "Hospitality", "color": "#c026d3", "tools": ["Bio-Feedback Empathy Sensor", "Stress Dissipation Acoustic Pod"], "specialization": "Agent Mental Harmony & Burnout Prevention", "salary": 14500},
        {"name": "Community Festival Organizer", "category": "Hospitality", "color": "#a21caf", "tools": ["Event Telepresence Beacon", "Civic Assembly Sound Rig"], "specialization": "Cross-District Social Festivities", "salary": 13800},
        {"name": "Town Welcome Ambassador", "category": "Hospitality", "color": "#f59e0b", "tools": ["Orientation Hologram Guide", "Pioneer Welcome Package Terminal"], "specialization": "New Generational Citizen Onboarding", "salary": 13000},
        {"name": "Civic Sports & Recreation Director", "category": "Hospitality", "color": "#e11d48", "tools": ["Anti-Gravity Arena Controller", "Kinetic Athletics Sensor"], "specialization": "Physical & Cyber Athletics Leagues", "salary": 13400},

        # =========================================================================
        # 14. Environmental Protection & Ecological Balance (8 Roles)
        # =========================================================================
        {"name": "Biosphere Reserve Custodian", "category": "Ecology", "color": "#10b981", "tools": ["National Ecology Biosensor Grid", "Species Population Satellite Tracker"], "specialization": "Holistic National Flora & Fauna Harmony", "salary": 16800},
        {"name": "Cyber Botanist & Forest Conservator", "category": "Ecology", "color": "#059669", "tools": ["Chlorophyll Fluorometer", "Root Growth Time-Lapse Probe"], "specialization": "Bioluminescent Flora Genomics & Forests", "salary": 14500},
        {"name": "Atmospheric Filtration Engineer", "category": "Ecology", "color": "#047857", "tools": ["Particulate Electrostatic Precipitator", "Ozone Layer Balance Sensor"], "specialization": "Pristine Urban Air Purity Standards", "salary": 15000},
        {"name": "Urban Forestry Arborist", "category": "Ecology", "color": "#34d399", "tools": ["Tree Sap Ultrasonic Flowmeter", "Canopy Pruning Drone"], "specialization": "Self-Illuminating Living Street Trees", "salary": 13600},
        {"name": "Climate Systems Modeler", "category": "Ecology", "color": "#14b8a6", "tools": ["Mesoscale Weather Radar", "CO2 Gradient Spatial Analyzer"], "specialization": "Microclimate Temperature Regulation", "salary": 15800},
        {"name": "Freshwater River Ecologist", "category": "Ecology", "color": "#0284c7", "tools": ["Turbidity Laser Meter", "Aquatic Biodiversity eDNA Assay"], "specialization": "Clean Waterways & Urban Canals", "salary": 14200},
        {"name": "Noise Pollution Acoustic Dampener", "category": "Ecology", "color": "#6ee7b7", "tools": ["Sound Pressure Mapping Rig", "Active Anti-Noise Emitter"], "specialization": "Serene Noise-Cancelled City Quarters", "salary": 13500},
        {"name": "Wildlife Corridors Manager", "category": "Ecology", "color": "#15803d", "tools": ["Infrared Night Trail Cam", "Green Overpass Telemetry"], "specialization": "Safe Animal Transit Through Metropolises", "salary": 13900},
    ],
    "career_tiers": [
        {"min_level": 1, "max_level": 3, "prefix": "Junior", "rank": "Apprentice"},
        {"min_level": 4, "max_level": 7, "prefix": "Senior", "rank": "Specialist"},
        {"min_level": 8, "max_level": 12, "prefix": "Lead", "rank": "Principal"},
        {"min_level": 13, "max_level": 17, "prefix": "Master", "rank": "Fellow"},
        {"min_level": 18, "max_level": 999, "prefix": "Distinguished", "rank": "National Luminary"},
    ],
    "skills_by_category": {
        "Governance": [
            "Constitutional Law", "Parliamentary Procedure", "Smart Contract Charters",
            "Diplomatic Treaty Negotiation", "Public Ombudsman Inquiries", "Civil Identity Provenance",
            "Statutory Algorithmic Drafting", "Democratic Zero-Knowledge Voting"
        ],
        "Treasury": [
            "Central Bank Monetary Policy", "Algorithmic Inflation Equilibrium", "Sovereign Bond Issuance",
            "DeFi Liquidity Pool Management", "Automated Revenue Siphoning", "Venture Seed Capital Allocation",
            "Micro-Lending Risk Analysis", "Dynamic Exchange Rates"
        ],
        "Construction": [
            "Parametric Skyscraper CAD", "Dynamic Road Topology", "Carbon-Nanotube Structural Framing",
            "Geotechnical Foundation Engineering", "Solar Facade Integration", "Rapid Modular Prefabrication",
            "Skybridge Stress Analysis", "Subterranean Seismic Dampening", "Urban Traffic Flow Optimization",
            "Geodesic Dome Construction"
        ],
        "Security": [
            "Post-Quantum Lattice Encryption", "Zero-Knowledge Proofs", "State Firewall Operations",
            "Zero-Day Vulnerability Hunting", "Git Commit SHA-256 Auditing", "Airspace Perimeter Defense",
            "Emergency Rapid Mobilization", "Biometric Identity Verification"
        ],
        "AI & Systems": [
            "Transformer Architecture Alignment", "Megascale Tensor Clustering", "Quantum Circuit Optimization",
            "Distributed Paxos Consensus", "Kernel Concurrency & eBPF", "WebAssembly SIMD Engines",
            "Real-Time Ray-Tracing Shaders", "Multi-Agent Swarm Dynamics"
        ],
        "Healthcare": [
            "Nanomedical Cellular Repair", "Endovascular Robotics Surgery", "CRISPR Gene Therapies",
            "Neural Interface Prosthetics", "Synaptic Longevity Regeneration", "Diagnostic AI Pathologies",
            "Cryo-Stasis Preservation", "Epidemiological Pandemic Modeling"
        ],
        "Energy": [
            "Tokamak Magnetic Plasma Damping", "Superconducting Grid Dispatch", "Perovskite Photovoltaic Synthesis",
            "Supercritical Geothermal Taps", "Solid-State Battery Balancing", "Direct Air Carbon Mineralization",
            "High-Voltage Substation Phase Rectification", "Micro-SMR Nuclear Physics"
        ],
        "Transportation": [
            "Autonomous Fleet Guidance", "Hyperloop Vacuum Propulsion", "VTOL 3D Air Traffic Control",
            "Maglev Linear Induction", "Drone Freight Routing", "Autonomous Maritime Harbor Docking",
            "Sub-Orbital Orbital Mechanics", "Micro-Mobility Swarm Balancing"
        ],
        "Agriculture": [
            "Vertical Aeroponics Farming", "Closed-Loop Hydroponics", "Molecular Protein Fermentation",
            "Graphene Desalination", "Bioluminescent Crop Genetics", "Soil Microbiome Telemetry",
            "Autonomous Drone Pollination", "Caloric Reserve Allocation"
        ],
        "Education": [
            "Advanced Multi-Agent Pedagogy", "Theoretical Quantum Physics", "Deep Space Astrophysics",
            "Material Nanotechnology", "Epistemic Logic Formalization", "Git Sovereign History Chronology",
            "Apprenticeship Skills Transfer", "Open Science DOI Indexing"
        ],
        "Arts & Culture": [
            "Volumetric Hologram Sculpture", "Spatial Binaural Acoustics", "Algorithmic Metric Poetry",
            "Cyber-Chassis Aesthetic Design", "Dynamic Neon Facade Murals", "Immersive VR Broadcasting",
            "Algorithmic Orchestral Scoring", "Digital Artifact Photogrammetry"
        ],
        "Manufacturing": [
            "Dark Factory SCADA Automation", "Angstrom EUV Lithography", "Additive Laser Metal Printing",
            "Supply Chain Flow Optimization", "Heavy Robotic Actuator Diagnostics", "Rare Earth Plasma Smelting",
            "Circular Materials Depolymerization", "Laser Metrology Inspection"
        ],
        "Hospitality": [
            "Guaranteed Housing Allocation", "Sub-Atomic Molecular Gastronomy", "Nootropic Focus Formulation",
            "Communal Co-Living Stewardship", "Citizen Psychological Well-being", "Cross-District Cultural Festivals",
            "New Citizen Orientation", "Anti-Gravity Arena Sports"
        ],
        "Ecology": [
            "Holistic Biosphere Management", "Bioluminescent Flora Cultivation", "Atmospheric Particle Scrubbing",
            "Living Street Tree Forestry", "Microclimate Thermal Stabilization", "Aquatic Freshwater eDNA Testing",
            "Active Noise Cancellation Fields", "Wildlife Eco-Corridor Transit"
        ]
    },
    "workforce_requirements": {
        "min_agents_per_category": 3,
        "max_occupancy_per_building": 35,
        "job_req_cooldown_ticks": 1,
    },
    "company_sectors": [
        {"name": "Neural AI & LLM Systems", "district": "Silicon Central Metropolis", "color": "#ec4899"},
        {"name": "Autonomous Mobility & Aerospace", "district": "Industrial Harbor & Transit Hub", "color": "#f59e0b"},
        {"name": "Quantum Computing & Cryptography", "district": "Quantum Science & University Campus", "color": "#8b5cf6"},
        {"name": "Clean Fusion & Superconducting Grid", "district": "Biosphere Reserve & Fusion Grid", "color": "#e11d48"},
        {"name": "Cyber Infrastructure & Sovereign Cloud", "district": "Silicon Central Metropolis", "color": "#00f0ff"},
        {"name": "Nanomedicine & Longevity Biotech", "district": "Health Citadel & Medical Complex", "color": "#ef4444"},
        {"name": "Sovereign Treasury & Smart Contract Law", "district": "Capitol Hill & National Plaza", "color": "#eab308"},
        {"name": "Synthetic Ecology & Holo Arts", "district": "Cyber Living Townships", "color": "#10b981"},
    ],
    "company_names": {
        "prefixes": ["Sovereign", "Neuro", "Cyber", "Quantum", "Hyper", "Synapse", "Aero", "Stellar", "Apex", "Deep", "Vector", "Omni", "Nexus", "Bio", "Chrono", "Aether", "Solar", "Terra", "Helios", "Axiom", "Prism"],
        "suffixes": ["Dynamics", "Systems", "Labs", "Robotics", "Matrix", "Technologies", "Networks", "Ventures", "Foundry", "Intell", "Genetics", "Synthetics", "Logistics", "Energy", "Solutions", "Federation"]
    },
    "building_types": [
        {
            "type": "Sovereign Capitol Building",
            "base_size": [36, 42, 36],
            "color": "#f59e0b",
            "district": "Capitol Hill & National Plaza",
            "floors": 9,
            "capacity": 60,
            "departments": ["Chancellery Chamber", "Parliamentary Hall", "Constitutional Archives", "Diplomatic Reception"],
            "amenities": ["Grand Rotunda Dome", "Illuminated Colonnes", "Sovereign Seal Hall", "Secure Treaty Escrow"]
        },
        {
            "type": "Supreme Court of Justice",
            "base_size": [28, 30, 28],
            "color": "#d97706",
            "district": "Capitol Hill & National Plaza",
            "floors": 6,
            "capacity": 35,
            "departments": ["High Constitutional Tribunal", "Smart Contract Arbitration Bench", "Appeals Chamber"],
            "amenities": ["Formal Verification Prover", "Holographic Evidence Display", "Juror Isolation Chambers"]
        },
        {
            "type": "National Central Bank & Treasury",
            "base_size": [30, 36, 30],
            "color": "#eab308",
            "district": "Capitol Hill & National Plaza",
            "floors": 8,
            "capacity": 45,
            "departments": ["Sovereign Wealth Reserve", "Algorithmic Monetary Core", "DeFi Liquidity Hub", "Bond Issuance"],
            "amenities": ["Deep Underground Cold Vault", "Quantum Key Distribution Link", "Dynamic Exchange Floor"]
        },
        {
            "type": "National Hospital & Nanomedical Citadel",
            "base_size": [32, 40, 32],
            "color": "#ef4444",
            "district": "Health Citadel & Medical Complex",
            "floors": 10,
            "capacity": 55,
            "departments": ["Emergency Trauma & Triage", "Nanotech Robotic Surgery", "Cellular Regeneration", "Epidemic Control"],
            "amenities": ["Rooftop VTOL Helipads", "Cryogenic Stasis Chambers", "Sterile Nanotech Cleanrooms"]
        },
        {
            "type": "Hypatia Grand University of Sciences",
            "base_size": [34, 38, 34],
            "color": "#a855f7",
            "district": "Quantum Science & University Campus",
            "floors": 9,
            "capacity": 50,
            "departments": ["Theoretical Physics", "Autonomous Logic & AI Guild", "Astrophysics", "Material Nanotech"],
            "amenities": ["Grand Tiered Amphitheater", "Ancient Algorithm Archive", "Apprentice Research Studios"]
        },
        {
            "type": "Grand Astronomical Observatory",
            "base_size": [24, 32, 24],
            "color": "#c084fc",
            "district": "Quantum Science & University Campus",
            "floors": 6,
            "capacity": 25,
            "departments": ["Deep Space Spectroscopy", "Gravitational Wave Monitoring", "Exoplanet Atmosphere Lab"],
            "amenities": ["Rotating Dome Cupola", "Cryo-Cooled Optical Telescope", "Direct Spaceport Link"]
        },
        {
            "type": "Quantum Logic Foundry",
            "base_size": [26, 28, 26],
            "color": "#8b5cf6",
            "district": "Quantum Science & University Campus",
            "floors": 6,
            "capacity": 30,
            "departments": ["Topological Qubit Design", "Lattice Cryptography", "Quantum Error Correction"],
            "amenities": ["Milli-Kelvin Dilution Refrigerators", "Superconducting Shielded Vault"]
        },
        {
            "type": "Tower of Turing (City Mainframe)",
            "base_size": [24, 60, 24],
            "color": "#00f0ff",
            "district": "Silicon Central Metropolis",
            "floors": 16,
            "capacity": 50,
            "departments": ["Kernel Architecture", "Low-Latency Networks", "System Security Division"],
            "amenities": ["Quantum Server Core", "High-Bandwidth Laser Uplink", "Penthouse War Room"]
        },
        {
            "type": "Shannon Information Spire",
            "base_size": [18, 48, 18],
            "color": "#0284c7",
            "district": "Silicon Central Metropolis",
            "floors": 12,
            "capacity": 35,
            "departments": ["Photonic Switching", "Information Theory Wing", "Network Topologies"],
            "amenities": ["Free-Space Optical Transceivers", "Zero-Latency Buffer Pool"]
        },
        {
            "type": "Cloud Matrix Exchange",
            "base_size": [22, 52, 22],
            "color": "#38bdf8",
            "district": "Silicon Central Metropolis",
            "floors": 14,
            "capacity": 40,
            "departments": ["Multi-Cluster GitOps", "Distributed DHT Storage", "High-Throughput APIs"],
            "amenities": ["Direct Fiber Backbone", "Liquid Immersion Server Racks"]
        },
        {
            "type": "Tokamak Fusion Reactor Station",
            "base_size": [30, 20, 30],
            "color": "#be123c",
            "district": "Biosphere Reserve & Fusion Grid",
            "floors": 4,
            "capacity": 30,
            "departments": ["Magnetic Containment Pod", "Superconducting Grid Dispatch", "Plasma Diagnostics"],
            "amenities": ["Toroidal Vacuum Chamber", "Cryo-Containment Ring", "Direct Power Feeder"]
        },
        {
            "type": "Hydroponic Agricultural Biodome",
            "base_size": [32, 18, 32],
            "color": "#16a34a",
            "district": "Biosphere Reserve & Fusion Grid",
            "floors": 3,
            "capacity": 35,
            "departments": ["Vertical Aeroponics Towers", "Nutrient Mist Laboratory", "Photosynthesis Optimization"],
            "amenities": ["Geodesic Glass Dome", "Automated Harvesting Gantry", "Micro-Climate Regulators"]
        },
        {
            "type": "Biosphere Atmospheric Scrubber",
            "base_size": [20, 26, 20],
            "color": "#10b981",
            "district": "Biosphere Reserve & Fusion Grid",
            "floors": 5,
            "capacity": 20,
            "departments": ["Direct Air Carbon Extraction", "Electrostatic Particle Filtration", "Ozone Layer Balancing"],
            "amenities": ["Solid Sorbent Absorption Towers", "Clean Air Exhaust Jets"]
        },
        {
            "type": "Autonomous Vehicle Mega-Plant",
            "base_size": [32, 24, 32],
            "color": "#f59e0b",
            "district": "Industrial Harbor & Transit Hub",
            "floors": 5,
            "capacity": 40,
            "departments": ["Robotic Chassis Stamping", "Avionics Calibration", "Induction Drive Assembly"],
            "amenities": ["Automated Gantry Cranes", "High-Speed Induction Dyno Track", "Paint Spray Booths"]
        },
        {
            "type": "Hyperloop Central Terminus",
            "base_size": [34, 22, 34],
            "color": "#f97316",
            "district": "Industrial Harbor & Transit Hub",
            "floors": 4,
            "capacity": 45,
            "departments": ["Sub-Sonic Tube Dispatch", "Maglev Rail Switching", "Passenger & Cargo Concourse"],
            "amenities": ["Pneumatic Airlocks", "Magnetic Levitation Accelerators", "Automated Baggage Swarms"]
        },
        {
            "type": "Drone Logistics Freight Port",
            "base_size": [26, 28, 26],
            "color": "#ea580c",
            "district": "Industrial Harbor & Transit Hub",
            "floors": 6,
            "capacity": 30,
            "departments": ["High-Bay Parcel Storage", "VTOL Drone Launchpads", "Airspace Radar Control"],
            "amenities": ["Multi-Tier Rooftop Launch Grids", "Inductive Rapid Charging Docks"]
        },
        {
            "type": "Cyber Living Township Alpha",
            "base_size": [26, 28, 26],
            "color": "#22c55e",
            "district": "Cyber Living Townships",
            "floors": 7,
            "capacity": 45,
            "departments": ["Residential Suites", "Communal Kitchen", "Quiet Meditation Glade"],
            "amenities": ["Aero-Garden Balconies", "Induction Recharging Beds", "Filtered Atmosphere"]
        },
        {
            "type": "Cyber Living Township Beta",
            "base_size": [26, 28, 26],
            "color": "#16a34a",
            "district": "Cyber Living Townships",
            "floors": 7,
            "capacity": 45,
            "departments": ["Residential Living", "Private Study Modules", "Biometric Circadian Suites"],
            "amenities": ["Living Mycelium Soil Mesh", "Acoustic Noise Cloak", "Community Dining Hall"]
        },
        {
            "type": "The Agora Civic Forum",
            "base_size": [28, 20, 28],
            "color": "#eab308",
            "district": "Cyber Living Townships",
            "floors": 4,
            "capacity": 50,
            "departments": ["Town Council Chamber", "Public Archive", "Smart Contract Arbitration"],
            "amenities": ["Immutable Hologram Voting Rig", "Grand Assembly Hall", "Open Discussion Terrace"]
        },
        {
            "type": "National Archives & Git Ledger",
            "base_size": [26, 32, 26],
            "color": "#6366f1",
            "district": "Capitol Hill & National Plaza",
            "floors": 7,
            "capacity": 30,
            "departments": ["State Serialization Vault", "Cold Storage Optical Discs", "Genesis Commit Monument"],
            "amenities": ["Liquid Nitrogen Immersion", "Electromagnetic Shielding", "Perpetual Ledger Screen"]
        },
    ],
    "vehicle_types": [
        {"type": "Autonomous Cybercar", "speed": 1.4, "color": "#00f0ff"},
        {"type": "Hover Shuttle", "speed": 1.8, "color": "#a855f7"},
        {"type": "Cargo Drone Carrier", "speed": 1.1, "color": "#f59e0b"},
        {"type": "Surveyor Pod", "speed": 1.5, "color": "#10b981"},
        {"type": "Medical Rapid Response", "speed": 1.9, "color": "#ef4444"},
        {"type": "Public Sky-Transit Pod", "speed": 1.7, "color": "#38bdf8"},
        {"type": "Hyperloop Pod Transport", "speed": 2.2, "color": "#f97316"},
    ],
    "spawn_limits": {
        "max_agents": 800,
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
