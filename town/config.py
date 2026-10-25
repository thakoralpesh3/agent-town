"""Configuration settings for GitHub Autonomous Tech Town."""

TOWN_CONFIG = {
    "name": "GitHub Tech Town",
    "version": "1.2.0",
    "initial_agent_count": 200,
    "grid_size": 400,
    "districts": [
        {"name": "Silicon Central", "center": [0, 0], "radius": 50, "color": "#00f0ff"},
        {"name": "Innovation Matrix", "center": [100, 100], "radius": 60, "color": "#a855f7"},
        {"name": "Residential Quarter", "center": [-100, 80], "radius": 65, "color": "#22c55e"},
        {"name": "Cyber Commons", "center": [-80, -90], "radius": 55, "color": "#eab308"},
        {"name": "Industrial Sector", "center": [90, -100], "radius": 60, "color": "#f97316"},
    ],
    "roles": [
        # Construction & Architecture
        {"name": "Urban Architect", "category": "Construction", "color": "#3b82f6"},
        {"name": "Road & Infrastructure Engineer", "category": "Construction", "color": "#64748b"},
        {"name": "Structural Space Designer", "category": "Construction", "color": "#0284c7"},

        # Engineering & Robotics
        {"name": "Autonomous Vehicle Designer", "category": "Engineering", "color": "#f59e0b"},
        {"name": "Quantum Systems Engineer", "category": "Engineering", "color": "#8b5cf6"},
        {"name": "Robotics Mechanist", "category": "Engineering", "color": "#d97706"},
        {"name": "Drone Fleet Aviator", "category": "Engineering", "color": "#f97316"},

        # Research & Science
        {"name": "AI & Neural Researcher", "category": "Research", "color": "#ec4899"},
        {"name": "Astrophysics Modeler", "category": "Research", "color": "#c084fc"},
        {"name": "Material Scientist", "category": "Research", "color": "#f43f5e"},
        {"name": "NLP & Cognitive Scientist", "category": "Research", "color": "#db2777"},

        # Software & Security
        {"name": "Full-Stack Web Architect", "category": "Software", "color": "#10b981"},
        {"name": "Distributed Systems Engineer", "category": "Software", "color": "#059669"},
        {"name": "Firmware & IoT Hacker", "category": "Software", "color": "#14b8a6"},
        {"name": "Security & Cryptographer", "category": "Security", "color": "#0d9488"},

        # Infrastructure
        {"name": "DevOps & Cloud Sentinel", "category": "Infrastructure", "color": "#06b6d4"},
        {"name": "Decentralized Mesh Custodian", "category": "Infrastructure", "color": "#0891b2"},

        # Healthcare & Biotech
        {"name": "Cybernetic Physician", "category": "Healthcare", "color": "#ef4444"},
        {"name": "Neural Biologist", "category": "Healthcare", "color": "#f87171"},
        {"name": "Nanotech Medic", "category": "Healthcare", "color": "#fb7185"},

        # Ecology & Agriculture
        {"name": "Cyber Botanist", "category": "Ecology", "color": "#84cc16"},
        {"name": "Hydroponic Vertical Farmer", "category": "Ecology", "color": "#65a30d"},
        {"name": "Climate Systems Modeler", "category": "Ecology", "color": "#4d7c0f"},

        # Energy & Utilities
        {"name": "Energy & Fusion Specialist", "category": "Energy", "color": "#e11d48"},
        {"name": "Solar Grid Architect", "category": "Energy", "color": "#ea580c"},

        # Society, Education & Law
        {"name": "Academy Professor & Mentor", "category": "Education", "color": "#a855f7"},
        {"name": "Town Chronicler & Historian", "category": "Society", "color": "#d946ef"},
        {"name": "Community Organizer", "category": "Society", "color": "#c026d3"},
        {"name": "Cyber Justice & Smart Arbiter", "category": "Law & Ethics", "color": "#7c3aed"},
        {"name": "AI Ethics Counsel", "category": "Law & Ethics", "color": "#6d28d9"},

        # Commerce & Finance
        {"name": "DeFi Banker & Treasury Analyst", "category": "Finance", "color": "#eab308"},
        {"name": "Tokenomics Trader", "category": "Finance", "color": "#ca8a04"},

        # Arts, Hospitality & Culture
        {"name": "Cybernetics Artisan", "category": "Art", "color": "#f43f5e"},
        {"name": "Holo Musician & Soundscaper", "category": "Art", "color": "#fb923c"},
        {"name": "Culinary Artisan & Quantum Barista", "category": "Hospitality", "color": "#fbbf24"},
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
            "Geothermal Foundation Engineering", "Solar Facade Integration", "Rapid Modular Prefabrication"
        ],
        "Engineering": [
            "Autonomous Drive Guidance", "Quantum Entanglement Bus", "LiDAR Pointcloud Mapping",
            "Brushless Motor Telemetry", "Drone Fleet Coordination", "Micro-Hydraulic Articulation"
        ],
        "Research": [
            "Deep Mixture-of-Experts", "Diffusion Model Scheduling", "Astrophysical Warp Simulation",
            "Metamaterial Refraction", "Neural Latency Compression", "Emergent Swarm Dynamics"
        ],
        "Software": [
            "Distributed Paxos Consensus", "WebAssembly High-Perf Engine", "Microservices Zero-Trust Mesh",
            "Rust Kernel Concurrency", "Event Sourcing Pipeline", "Reactive 3D Spatial Audio"
        ],
        "Security": [
            "Zero-Knowledge Proofs", "Elliptic Curve Cryptography", "Buffer Overflow Neutralization",
            "Autonomous Threat Hunting", "Post-Quantum Lattice Encryption"
        ],
        "Infrastructure": [
            "Kubernetes Multi-Cluster GitOps", "Zero-Downtime Hot Swapping", "Edge Cache Invalidation",
            "InfiniBand Fabric Optimization", "Automated Disaster Recovery"
        ],
        "Healthcare": [
            "Neural Prosthetic Calibration", "Cellular Nanobot Diagnostics", "Cryo-Regenerative Therapy",
            "Bio-Telemetry Monitoring", "Genetic Sequence Optimization"
        ],
        "Ecology": [
            "Bioluminescent Flora Cultivation", "Atmospheric Carbon Scrubbing", "Closed-Loop Hydroponics",
            "Mycelial Network Routing", "Precision Nutrient Dosing"
        ],
        "Energy": [
            "Tokamak Magnetic Containment", "Superconducting Transmission Line", "Perovskite Solar Absorption",
            "Solid-State Battery Balancing", "District Thermal Energy Recirculation"
        ],
        "Education": [
            "Next-Gen Cognitive Tutoring", "Cross-Domain Skill Transfer", "Mentorship Pairing Heuristics",
            "Open Source Curriculum Design", "Peer Learning Guilds"
        ],
        "Society": [
            "GitHub Town Archival Scription", "Collaborative Build Coordination", "Civic Consensus Gathering",
            "Cultural Heritage Preservation", "Autonomous Festival Curation"
        ],
        "Law & Ethics": [
            "Smart Contract Formal Verification", "Algorithmic Fairness Auditing", "Decentralized Dispute Resolution",
            "Autonomous Rights Charters", "Data Provenance Verification"
        ],
        "Finance": [
            "Automated Market Maker Liquidity", "Treasury Bonding & Staking", "Algorithmic Risk Management",
            "Town Venture Capital Allocation", "Inflation Balancing Protocols"
        ],
        "Art": [
            "Holographic Light Sculpture", "Procedural Ambient Synthesis", "Volumetric Neon Murals",
            "Cyber-Chassis Aerodynamics", "Dynamic Particle Choreography"
        ],
        "Hospitality": [
            "Molecular Flavor Synthesis", "Quantum Foam Latte Art", "Community Micro-Brewing",
            "Nutritional Biomarker Customization", "Social Harmony Ambient Setting"
        ]
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
        "prefixes": ["Neuro", "Cyber", "Quantum", "Hyper", "Synapse", "Aero", "Stellar", "Apex", "Deep", "Vector", "Omni", "Nexus", "Bio", "Chrono", "Aether", "Solar"],
        "suffixes": ["Dynamics", "Systems", "Labs", "Robotics", "Matrix", "Technologies", "Networks", "Ventures", "Foundry", "Intell", "Genetics", "Synthetics"]
    },
    "building_types": [
        {"type": "Tech Tower", "base_size": [16, 45, 16], "color": "#0ea5e9", "district": "Silicon Central"},
        {"type": "AI Research Lab", "base_size": [20, 25, 20], "color": "#a855f7", "district": "Innovation Matrix"},
        {"type": "Residential Pod", "base_size": [12, 18, 12], "color": "#22c55e", "district": "Residential Quarter"},
        {"type": "Cyber Cafe", "base_size": [14, 10, 14], "color": "#eab308", "district": "Cyber Commons"},
        {"type": "Quantum Data Center", "base_size": [24, 20, 24], "color": "#6366f1", "district": "Industrial Sector"},
        {"type": "Solar Fusion Array", "base_size": [18, 8, 18], "color": "#f97316", "district": "Industrial Sector"},
        {"type": "Holo Park", "base_size": [25, 4, 25], "color": "#10b981", "district": "Cyber Commons"},
        {"type": "Vehicle Factory", "base_size": [22, 16, 22], "color": "#f59e0b", "district": "Industrial Sector"},
        {"type": "Company Headquarters", "base_size": [22, 50, 22], "color": "#ec4899", "district": "Silicon Central"},
        {"type": "Cybernetic Clinic", "base_size": [18, 22, 18], "color": "#ef4444", "district": "Residential Quarter"},
        {"type": "Academy of Sciences", "base_size": [26, 30, 26], "color": "#a855f7", "district": "Innovation Matrix"},
    ],
    "vehicle_types": [
        {"type": "Autonomous Cybercar", "speed": 1.4, "color": "#00f0ff"},
        {"type": "Hover Shuttle", "speed": 1.8, "color": "#a855f7"},
        {"type": "Cargo Drone Carrier", "speed": 1.1, "color": "#f59e0b"},
        {"type": "Surveyor Pod", "speed": 1.5, "color": "#10b981"},
        {"type": "Medical Rapid Response", "speed": 1.9, "color": "#ef4444"},
    ],
    "spawn_limits": {
        "max_agents": 500,
        "agent_reproduction_probability": 0.06,
        "company_founding_probability": 0.08,
        "building_construction_probability": 0.25,
        "road_construction_probability": 0.20,
        "vehicle_construction_probability": 0.15,
        "coding_probability": 0.35,
        "mentorship_probability": 0.40,
    }
}
