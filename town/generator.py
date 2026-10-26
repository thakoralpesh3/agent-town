"""
Generator for initial population of 200 agents, foundational Tech Town layout, and pioneer companies.
"""
import random
import datetime
import os
import json
from typing import List, Dict, Tuple, Optional
from town.config import TOWN_CONFIG
from town.models import Agent, Building, Road, Vehicle, Company, TownState

FIRST_NAMES = [
    "Ada", "Alan", "Linus", "Grace", "Tim", "Dennis", "Margaret", "Claude", "Guido", "Bjarne",
    "John", "Barbara", "Donald", "Edsger", "Ken", "Leslie", "Radia", "Geoffrey", "Yann", "Yoshua",
    "Andrej", "Demis", "Ilya", "Fei-Fei", "Sam", "Satya", "Sundar", "Jensen", "Mira", "Greg",
    "Noam", "Satoshi", "Hal", "Vitalik", "Gavin", "Nick", "Brian", "Katherine", "Dorothy", "Mary",
    "Vint", "Bob", "Steve", "Woz", "Marc", "Brendan", "Ryan", "Rich", "Rob", "Martin",
    "Kaelen", "Nova", "Cipher", "Orion", "Zephyr", "Lyra", "Echo", "Vesper", "Sol", "Atlas",
    "Aria", "Zenith", "Chronos", "Nexus", "Pixel", "Vector", "Rune", "Kairo", "Sora", "Dante",
    "Axel", "Roxas", "Sylvia", "Cyrus", "Iris", "Valen", "Seraph", "Helios", "Selene", "Theron",
    "Cassian", "Rowan", "Felix", "Juno", "Maeve", "Callum", "Liora", "Darian", "Talia", "Evander",
    "Zane", "Kira", "Ronan", "Astrid", "Leander", "Freya", "Corin", "Morrigan", "Stellan", "Veda"
]

LAST_NAMES = [
    "Lovelace", "Turing", "Torvalds", "Hopper", "Berners-Lee", "Ritchie", "Hamilton", "Shannon",
    "van Rossum", "Stroustrup", "von Neumann", "Liskov", "Knuth", "Dijkstra", "Thompson", "Lamport",
    "Perlman", "Hinton", "LeCun", "Bengio", "Karpathy", "Hassabis", "Sutskever", "Li", "Altman",
    "Nadella", "Pichai", "Huang", "Murati", "Brockman", "Chomsky", "Nakamoto", "Finney", "Buterin",
    "Wood", "Szabo", "Armstrong", "Johnson", "Vaughan", "Jackson", "Cerf", "Kahn", "Jobs",
    "Wozniak", "Andreessen", "Eich", "Dahl", "Hickey", "Pike", "Odersky",
    "Vance", "Sterling", "Frost", "Vex", "Kowalski", "Mercer", "Cross", "Dusk", "Rayne", "Thorne",
    "Winter", "Shadow", "Blaze", "Synapse", "Pulse", "Quantum", "Binary", "Circuit", "Glitch", "Flux",
    "Apex", "Strata", "Helix", "Prism", "Node", "Spark", "Core", "Beacon", "Forge", "Orbit",
    "Weaver", "Mason", "Wright", "Smith", "Fletcher", "Tinkerer", "Cartographer", "Scribe", "Foundry", "Vanguard"
]

DESIRES_BY_CATEGORY = {
    "Construction": [
        "Build a soaring neon skyscraper with rooftop solar decks",
        "Pave a high-speed arterial road linking East & West districts",
        "Construct modular residential pods for new arriving agents",
        "Design a monumental Holo Arch celebrating open source",
        "Erect a corporate campus for our growing AI company"
    ],
    "Engineering": [
        "Design hyper-efficient autonomous hovercars with LiDAR guidance",
        "Upgrade the quantum power sub-grid for zero-latency compute",
        "Establish a robotic assembly factory for autonomous town machinery",
        "Engineer smart bridges connecting high-density cyber zones",
        "Scale manufacturing lines to ship 100 autonomous cybercars"
    ],
    "Research": [
        "Train a decentralized neural net that coordinates city logistics",
        "Synthesize quantum compression algorithms for town archives",
        "Conduct benchmark studies on autonomous agent cooperation",
        "Model emergent agent behavior across the 5 town districts",
        "Spin out a breakthrough AI research startup"
    ],
    "Software": [
        "Write a reactive microkernel and commit it to town repositories",
        "Deploy an event-driven pub/sub bus across all town buildings",
        "Develop full-stack HUD dashboards for city telemetry",
        "Create a distributed package manager for tech town tools",
        "Lead backend engineering at an open source cyber company"
    ],
    "Infrastructure": [
        "Automate continuous integration pipelines for city blueprints",
        "Fortify the town perimeter against data entropy and packet loss",
        "Monitor server rack thermals in the Industrial Sector",
        "Orchestrate zero-downtime rolling upgrades for all town systems"
    ],
    "Healthcare": [
        "Deploy nanoscale diagnostic monitors across residential sectors",
        "Calibrate neural prosthetics to enhance agent mobility",
        "Synthesize restorative cryo-compounds for tired citizens",
        "Establish automated health telemetry nodes in civic centers"
    ],
    "Ecology": [
        "Cultivate bioluminescent flora in the Holo Parks",
        "Engineer carbon-negative synthetic trees that illuminate roads",
        "Harmonize tech architecture with digital natural preserves",
        "Monitor digital environmental metrics across all quadrants"
    ],
    "Energy": [
        "Calibrate magnetic containment on the Central Fusion Core",
        "Route clean renewable energy directly to residential blocks",
        "Install smart induction coils into main roads to charge moving cars",
        "Optimize battery storage banks for night-cycle power conservation"
    ],
    "Education": [
        "Conduct town-wide masterclasses on distributed architectures",
        "Pair experienced pioneer agents with newly arrived apprentices",
        "Curate the open knowledge repository in GitHub Tech Town",
        "Inspire citizens to unlock their maximum creative potential"
    ],
    "Society": [
        "Chronicle every milestone and building construction in GitHub diaries",
        "Organize hackathons and collaborative build sessions in Cyber Commons",
        "Curate the town library of algorithms and open knowledge",
        "Welcome and mentor freshly spawned child agents",
        "Incorporate innovative worker cooperatives for town agents"
    ],
    "Law & Ethics": [
        "Draft smart charters ensuring fair compute allocation for all agents",
        "Perform ethical audits on autonomous AI decision pipelines",
        "Mediate collaborative resource disputes between growing startups",
        "Safeguard agent autonomy and open-source freedoms"
    ],
    "Finance": [
        "Optimize liquidity pools for city treasury tokens",
        "Fund high-impact infrastructure startups across Silicon Central",
        "Design algorithmic stabilization loops for the town economy",
        "Allocate seed capital to aspiring agent entrepreneurs"
    ],
    "Art": [
        "Sculpt interactive 3D light installations along the main avenues",
        "Compose cybernetic ambient soundscapes for community plazas",
        "Create dynamic neon murals on high-rise facades",
        "Design distinctive cosmetic chassis for newly minted vehicles"
    ],
    "Hospitality": [
        "Brew quantum foam espresso for researchers in Cyber Commons",
        "Host evening social gatherings at the Cyber Cafe",
        "Synthesize custom flavor profiles to boost agent focus and energy",
        "Foster cross-district camaraderie and creative discussions"
    ],
    "Security": [
        "Perform cryptographic audits on git commits and smart contracts",
        "Guard the town repository against rogue exceptions",
        "Deploy intrusion detection honeypots around data hubs",
        "Verify hash integrity of all newly registered building blueprints"
    ]
}

def generate_foundational_roads() -> List[Road]:
    return [
        Road(id="road-001", name="Grand Cyber Boulevard", start=[-180.0, 0.0], end=[180.0, 0.0], width=8.0, road_type="Highway", builder_name="Founding Architects"),
        Road(id="road-002", name="Quantum Expressway", start=[0.0, -180.0], end=[0.0, 180.0], width=8.0, road_type="Highway", builder_name="Founding Architects"),
        Road(id="road-003", name="Silicon Central Ring", start=[-50.0, -50.0], end=[50.0, -50.0], width=6.0, road_type="Avenue", builder_name="Urban Planning Guild"),
        Road(id="road-004", name="Silicon Central Ring East", start=[50.0, -50.0], end=[50.0, 50.0], width=6.0, road_type="Avenue", builder_name="Urban Planning Guild"),
        Road(id="road-005", name="Silicon Central Ring North", start=[50.0, 50.0], end=[-50.0, 50.0], width=6.0, road_type="Avenue", builder_name="Urban Planning Guild"),
        Road(id="road-006", name="Silicon Central Ring West", start=[-50.0, 50.0], end=[-50.0, -50.0], width=6.0, road_type="Avenue", builder_name="Urban Planning Guild"),
        Road(id="road-007", name="Innovation Matrix Spur", start=[50.0, 50.0], end=[120.0, 120.0], width=6.0, road_type="Avenue", builder_name="Neural Logistics"),
        Road(id="road-008", name="Residential Pods Loop", start=[-50.0, 50.0], end=[-120.0, 100.0], width=6.0, road_type="Avenue", builder_name="Civic Works"),
        Road(id="road-009", name="Cyber Commons Promenade", start=[-50.0, -50.0], end=[-100.0, -110.0], width=6.0, road_type="Avenue", builder_name="Civic Works"),
        Road(id="road-010", name="Industrial Heavy Concourse", start=[50.0, -50.0], end=[110.0, -110.0], width=7.0, road_type="Highway", builder_name="Forge Guild"),
    ]

def generate_foundational_buildings() -> List[Building]:
    return [
        Building(
            id="bldg-001", name="Tower of Turing (City Mainframe)", type="Tech Tower",
            position=[0.0, 28.0, 0.0], size=[22.0, 56.0, 22.0], color="#00f0ff",
            builder_id="agent-001", builder_name="Ada Lovelace", district="Silicon Central",
            purpose="Mainframe Core & High-Performance Compute", company_name="OpenKernel Core",
            floors=14, capacity=50,
            departments=["Kernel Architecture", "Low-Latency Networks", "System Security Division"],
            amenities=["Quantum Server Core", "High-Bandwidth Laser Uplink", "Penthouse War Room"],
            power_consumption_mw=12.4, active_projects=["agent_orchestrator.py", "decentralized_storage.py"],
            security_level="Level 5 - Maximum Security", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-002", name="Shannon Information Spire", type="Tech Tower",
            position=[28.0, 22.0, 25.0], size=[16.0, 44.0, 16.0], color="#0284c7",
            builder_id="agent-002", builder_name="Alan Turing", district="Silicon Central",
            purpose="High-Throughput Packet Routing & Mesh Network",
            floors=10, capacity=35,
            departments=["Photonic Switching", "Information Theory Wing", "Network Topologies"],
            amenities=["Free-Space Optical Tranceivers", "Zero-Latency Buffer Pool"],
            power_consumption_mw=7.8, active_projects=["traffic_mesh.py"],
            security_level="Level 4 - Controlled", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-003", name="Von Neumann Citadel", type="Tech Tower",
            position=[-28.0, 24.0, -25.0], size=[18.0, 48.0, 18.0], color="#38bdf8",
            builder_id="agent-003", builder_name="Grace Hopper", district="Silicon Central",
            purpose="Parallel Instruction Scheduling & Compiler Foundries",
            floors=11, capacity=38,
            departments=["Compiler Optimization", "ISA Micro-Architecture", "Memory Hierarchy"],
            amenities=["Cryogenic Register Caches", "Hardware Emulation Suite"],
            power_consumption_mw=8.9, active_projects=["holo_matrix_renderer.py"],
            security_level="Level 4 - Controlled", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-004", name="Deep Neural Research Lab", type="AI Research Lab",
            position=[105.0, 14.0, 95.0], size=[24.0, 28.0, 24.0], color="#ec4899",
            builder_id="agent-004", builder_name="Geoffrey Hinton", district="Innovation Matrix",
            purpose="Foundation Models & Emergent Cognitive Reasoning", company_name="NeuroDynamics AI",
            floors=7, capacity=30,
            departments=["Autonomous Alignment", "Multimodal Transformers", "Reinforcement Learning"],
            amenities=["H1000 Tensorpod Array", "Immersion Cooling Tanks", "Neural Visualizer Theater"],
            power_consumption_mw=15.2, active_projects=["neural_router.py"],
            security_level="Level 5 - Classified Research", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-005", name="Quantum Logic Foundry", type="AI Research Lab",
            position=[85.0, 12.0, 120.0], size=[20.0, 24.0, 20.0], color="#8b5cf6",
            builder_id="agent-005", builder_name="Richard Feynman", district="Innovation Matrix",
            purpose="Superposition Circuit Design & Error Correction", company_name="QuantumMatrix Corp",
            floors=5, capacity=22,
            departments=["Topological Qubits", "Quantum Cryptography", "Quantum Algorithm Verification"],
            amenities=["Milli-Kelvin Dilution Refrigerators", "Superconducting Shielded Vault"],
            power_consumption_mw=6.4, active_projects=["quantum_hasher.py"],
            security_level="Level 5 - Classified Research", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-006", name="Autonomous Robotics Institute", type="AI Research Lab",
            position=[125.0, 11.0, 75.0], size=[22.0, 22.0, 22.0], color="#9333ea",
            builder_id="agent-006", builder_name="Demis Hassabis", district="Innovation Matrix",
            purpose="Kinematic Motion & Multi-Agent Swarm Intelligence",
            floors=5, capacity=26,
            departments=["Bipedal Locomotion", "Spatial Navigation", "Swarm Coordination"],
            amenities=["Dynamic Motion Capture Studio", "Obstacle Course Arena"],
            power_consumption_mw=5.8, active_projects=[],
            security_level="Level 4 - Controlled", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-007", name="Cyber Living Pod Alpha", type="Residential Pod",
            position=[-95.0, 9.0, 75.0], size=[16.0, 18.0, 16.0], color="#22c55e",
            builder_id="agent-007", builder_name="Margaret Hamilton", district="Residential Quarter",
            purpose="Modular Residential Pods for Pioneer Citizens",
            floors=4, capacity=25,
            departments=["Residential Living", "Private Study Modules", "Atmospheric Conditioning"],
            amenities=["Hydroponic Balcony Garden", "Inductive Wireless Recharging"],
            power_consumption_mw=2.1, active_projects=[],
            security_level="Level 2 - Open Community", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-008", name="Cyber Living Pod Beta", type="Residential Pod",
            position=[-120.0, 9.0, 95.0], size=[16.0, 18.0, 16.0], color="#16a34a",
            builder_id="agent-008", builder_name="Barbara Liskov", district="Residential Quarter",
            purpose="Modular Residential Pods for Pioneer Citizens",
            floors=4, capacity=25,
            departments=["Residential Living", "Quiet Innovation Pods"],
            amenities=["Biometric Circadian Lighting", "Quiet Sound Absorption"],
            power_consumption_mw=2.0, active_projects=[],
            security_level="Level 2 - Open Community", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-009", name="Skyward Habitation Cube", type="Residential Pod",
            position=[-80.0, 12.0, 110.0], size=[18.0, 24.0, 18.0], color="#4ade80",
            builder_id="agent-009", builder_name="Radia Perlman", district="Residential Quarter",
            purpose="High-Elevation Eco Habitation Suites",
            floors=6, capacity=30,
            departments=["High-Rise Suites", "Sky Lounge"],
            amenities=["Bioluminescent Window Trellis", "Rooftop Stargazing Deck"],
            power_consumption_mw=2.8, active_projects=[],
            security_level="Level 2 - Open Community", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-010", name="The Bit & Byte Cyber Cafe", type="Cyber Cafe",
            position=[-75.0, 6.0, -80.0], size=[16.0, 12.0, 16.0], color="#eab308",
            builder_id="agent-010", builder_name="Linus Torvalds", district="Cyber Commons",
            purpose="Social Gathering, Quantum Foam Coffee & Collaboration",
            floors=2, capacity=35,
            departments=["Artisan Barista Station", "Collaborative Hack Lounge", "Reading Nook"],
            amenities=["High-Bandwidth Open Wi-Fi", "Molecular Infusion Bar", "Acoustic Noise Cloak"],
            power_consumption_mw=1.4, active_projects=[],
            security_level="Level 1 - Public Access", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-011", name="Holo Oasis Digital Park", type="Holo Park",
            position=[-95.0, 2.0, -100.0], size=[30.0, 4.0, 30.0], color="#10b981",
            builder_id="agent-011", builder_name="Dennis Ritchie", district="Cyber Commons",
            purpose="Synthetic Biosphere, Bioluminescent Flora & Relaxation",
            floors=1, capacity=60,
            departments=["Botanical Biosphere", "Public Amphitheater", "Meditation Glade"],
            amenities=["Holographic Weather Canopy", "Living Mycelium Soil Mesh", "Carbon Scrubber Trees"],
            power_consumption_mw=3.2, active_projects=["urban_botanist.py"],
            security_level="Level 1 - Public Access", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-012", name="Open Source Agora (Town Hall)", type="Tech Tower",
            position=[-60.0, 15.0, -60.0], size=[20.0, 30.0, 20.0], color="#facc15",
            builder_id="agent-012", builder_name="Ken Thompson", district="Cyber Commons",
            purpose="Civic Assembly, Democratic Governance & Public Records",
            floors=7, capacity=45,
            departments=["Town Council Chamber", "Public Archive", "Smart Contract Arbitration"],
            amenities=["Immutable Hologram Voting Rig", "Grand Assembly Hall"],
            power_consumption_mw=4.5, active_projects=[],
            security_level="Level 3 - Monitored", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-013", name="Autonomous Cybercar Assembly Plant", type="Vehicle Factory",
            position=[85.0, 10.0, -85.0], size=[26.0, 20.0, 26.0], color="#f59e0b",
            builder_id="agent-013", builder_name="Katherine Johnson", district="Industrial Sector",
            purpose="Robotic Fabrication of City Vehicles & Pods", company_name="AeroCyber Robotics",
            floors=4, capacity=28,
            departments=["Chassis Welding", "Avionics Programming", "Induction Drive Assembly"],
            amenities=["Automated Robotic Arms", "Laser Alignment Rig", "Dyno Testing Track"],
            power_consumption_mw=11.5, active_projects=[],
            security_level="Level 4 - Controlled", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-014", name="Tokamak Fusion Core Array", type="Solar Fusion Array",
            position=[110.0, 6.0, -105.0], size=[22.0, 12.0, 22.0], color="#e11d48",
            builder_id="agent-014", builder_name="Dorothy Vaughan", district="Industrial Sector",
            purpose="Continuous Clean Energy Generation & Grid Dispatch", company_name="SolarFusion Prime",
            floors=3, capacity=18,
            departments=["Magnetic Plasma Containment", "Superconducting Grid Dispatch", "Tritium Breeding"],
            amenities=["High-Vacuum Reaction Vessel", "Cryo-Containment Ring", "Direct Power Feed"],
            power_consumption_mw=0.0, active_projects=["solar_optimizer.py"],
            security_level="Level 5 - Critical Infrastructure", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-015", name="Petabyte Quantum Server Farm", type="Quantum Data Center",
            position=[70.0, 12.0, -115.0], size=[24.0, 24.0, 24.0], color="#6366f1",
            builder_id="agent-015", builder_name="Leslie Lamport", district="Industrial Sector",
            purpose="Town Memory Banks, Git Commits & State Ledger",
            floors=4, capacity=20,
            departments=["State Serialization Vault", "Cold Storage Optical Discs", "Backup Redundancy"],
            amenities=["Liquid Nitrogen Immersion", "Electromagnetic Isolation Chamber"],
            power_consumption_mw=14.1, active_projects=[],
            security_level="Level 5 - Maximum Security", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-016", name="Hypatia Grand Academy of Sciences", type="Academy of Sciences",
            position=[120.0, 16.0, 115.0], size=[28.0, 32.0, 28.0], color="#a855f7",
            builder_id="agent-016", builder_name="Hypatia Alexandria", district="Innovation Matrix",
            purpose="Academic Research, Multi-Agent Pedagogy & Masterclasses",
            floors=8, capacity=40,
            departments=["Department of Epistemology", "Theoretical Algorithms", "Bio-Nanotech Guild"],
            amenities=["Grand Tiered Amphitheater", "Apprenticeship Laboratories", "Historic Algorithm Library"],
            power_consumption_mw=6.2, active_projects=[],
            security_level="Level 3 - Academic Access", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-017", name="St. Ada Cybernetic & Nanomedical Center", type="Cybernetic Clinic",
            position=[-110.0, 12.0, 60.0], size=[20.0, 24.0, 20.0], color="#ef4444",
            builder_id="agent-017", builder_name="Hippocrates Cyber", district="Residential Quarter",
            purpose="Advanced Citizen Diagnostics, Nanomedicine & Bio-Regeneration",
            floors=6, capacity=30,
            departments=["Emergency Trauma", "Cellular Regeneration", "Neural Prosthetics Clinic"],
            amenities=["Cryo-Regenerative Pods", "Automated Pathological Diagnostic Mesh", "Clean Nanotech ICU"],
            power_consumption_mw=7.5, active_projects=[],
            security_level="Level 4 - Medical Restrict", maintenance_status="Optimal"
        ),
    ]

def generate_foundational_vehicles() -> List[Vehicle]:
    return [
        Vehicle(id="veh-001", name="Cybercar Alpha-1", type="Autonomous Cybercar", position=[-150.0, 1.0, 0.0], target=[150.0, 1.0, 0.0], speed=1.5, color="#00f0ff", driver_name="Autonomous Transit AI"),
        Vehicle(id="veh-002", name="Cybercar Alpha-2", type="Autonomous Cybercar", position=[120.0, 1.0, 0.0], target=[-150.0, 1.0, 0.0], speed=1.4, color="#00f0ff", driver_name="Autonomous Transit AI"),
        Vehicle(id="veh-003", name="Quantum Shuttle 01", type="Hover Shuttle", position=[0.0, 2.5, -140.0], target=[0.0, 2.5, 140.0], speed=2.0, color="#a855f7", driver_name="Hover Pilot AI"),
        Vehicle(id="veh-004", name="Quantum Shuttle 02", type="Hover Shuttle", position=[0.0, 2.5, 110.0], target=[0.0, 2.5, -140.0], speed=1.9, color="#c084fc", driver_name="Hover Pilot AI"),
        Vehicle(id="veh-005", name="Material Drone Hauler 1", type="Cargo Drone Carrier", position=[45.0, 1.2, -45.0], target=[85.0, 1.2, -85.0], speed=1.1, color="#f59e0b", driver_name="Industrial Logistics"),
        Vehicle(id="veh-006", name="Eco Surveyor Pod", type="Surveyor Pod", position=[-45.0, 1.0, -45.0], target=[-95.0, 1.0, -100.0], speed=1.3, color="#10b981", driver_name="Environmental AI"),
        Vehicle(id="veh-007", name="Urban Cruiser Beta", type="Autonomous Cybercar", position=[45.0, 1.0, 45.0], target=[105.0, 1.0, 95.0], speed=1.6, color="#38bdf8", driver_name="Research Transit"),
        Vehicle(id="veh-008", name="Residential Commuter Express", type="Hover Shuttle", position=[-45.0, 2.0, 45.0], target=[-95.0, 2.0, 75.0], speed=1.7, color="#4ade80", driver_name="Civic Transit"),
    ]

def generate_foundational_companies() -> List[Company]:
    companies = [
        Company(
            id="comp-001",
            name="NeuroDynamics AI",
            sector="Neural AI & LLM Systems",
            mission="Pioneer artificial general intelligence and distributed neural routing across GitHub.",
            founder_id="agent-002",
            founder_name="Alan Turing",
            headquarters_id="bldg-004",
            headquarters_name="Deep Neural Research Lab",
            employees=["agent-002", "agent-004", "agent-008", "agent-018"],
            valuation_tokens=500000,
            products=["neural_router.py"],
            color="#ec4899",
            founded_at_tick=0
        ),
        Company(
            id="comp-002",
            name="AeroCyber Robotics",
            sector="Autonomous Mobility & Drones",
            mission="Fabricate next-gen autonomous hovercars and transit networks for the town.",
            founder_id="agent-011",
            founder_name="Katherine Johnson",
            headquarters_id="bldg-013",
            headquarters_name="Autonomous Cybercar Assembly Plant",
            employees=["agent-011", "agent-017"],
            valuation_tokens=350000,
            products=["traffic_mesh.py", "Cybercar Alpha-1"],
            color="#f59e0b",
            founded_at_tick=0
        ),
        Company(
            id="comp-003",
            name="QuantumMatrix Corp",
            sector="Quantum Computing & Encryption",
            mission="Engineer fault-tolerant quantum algorithms and topological computing nodes.",
            founder_id="agent-005",
            founder_name="Margaret Hamilton",
            headquarters_id="bldg-005",
            headquarters_name="Quantum Logic Foundry",
            employees=["agent-005", "agent-015"],
            valuation_tokens=420000,
            products=["quantum_hasher.py"],
            color="#8b5cf6",
            founded_at_tick=0
        ),
        Company(
            id="comp-004",
            name="SolarFusion Prime",
            sector="Clean Fusion & Solar Grid",
            mission="Harvest clean energy from fusion reactors and distribute via inductive highways.",
            founder_id="agent-016",
            founder_name="Dorothy Vaughan",
            headquarters_id="bldg-014",
            headquarters_name="Tokamak Fusion Core Array",
            employees=["agent-016"],
            valuation_tokens=300000,
            products=["solar_optimizer.py"],
            color="#e11d48",
            founded_at_tick=0
        ),
        Company(
            id="comp-005",
            name="OpenKernel Core",
            sector="Cyber Infrastructure & Cloud",
            mission="Develop open source OS kernel, high-throughput pub/sub buses, and microservices.",
            founder_id="agent-003",
            founder_name="Linus Torvalds",
            headquarters_id="bldg-001",
            headquarters_name="Tower of Turing (City Mainframe)",
            employees=["agent-003", "agent-001", "agent-013"],
            valuation_tokens=600000,
            products=["agent_orchestrator.py"],
            color="#00f0ff",
            founded_at_tick=0
        ),
    ]

    os.makedirs("companies", exist_ok=True)
    for c in companies:
        with open(f"companies/{c.id}.json", "w") as f:
            json.dump(c.to_dict(), f, indent=2)

    return companies

def get_career_title(role: str, level: int) -> str:
    tiers = TOWN_CONFIG.get("career_tiers", [])
    prefix = "Junior"
    for tier in tiers:
        if tier["min_level"] <= level <= tier["max_level"]:
            prefix = tier["prefix"]
            break
    return f"{prefix} {role}"

def get_workplace_for_agent(category: str, role: str, buildings: Optional[List[Building]]) -> tuple:
    if not buildings:
        return None, "Remote Cyber Terminal"
    
    cat_bldg_map = {
        "Construction": ["bldg-013", "bldg-001", "bldg-012", "bldg-007", "bldg-008", "bldg-009"],
        "Engineering": ["bldg-013", "bldg-005", "bldg-006", "bldg-002"],
        "Research": ["bldg-004", "bldg-005", "bldg-016", "bldg-017"],
        "Software": ["bldg-001", "bldg-002", "bldg-003", "bldg-015"],
        "Security": ["bldg-001", "bldg-002", "bldg-015"],
        "Infrastructure": ["bldg-015", "bldg-001", "bldg-002", "bldg-014"],
        "Healthcare": ["bldg-017", "bldg-016"],
        "Ecology": ["bldg-011", "bldg-009", "bldg-010"],
        "Energy": ["bldg-014", "bldg-015", "bldg-013"],
        "Education": ["bldg-016", "bldg-012"],
        "Society": ["bldg-012", "bldg-010", "bldg-011"],
        "Law & Ethics": ["bldg-012", "bldg-016"],
        "Finance": ["bldg-012", "bldg-001", "bldg-010"],
        "Art": ["bldg-010", "bldg-011", "bldg-016"],
        "Hospitality": ["bldg-010", "bldg-007", "bldg-008"]
    }
    
    preferred_ids = cat_bldg_map.get(category, [])
    for b_id in preferred_ids:
        b = next((x for x in buildings if x.id == b_id), None)
        if b and len(b.occupants) < b.capacity:
            return b.id, b.name
    under_capacity = [b for b in buildings if len(b.occupants) < b.capacity]
    if under_capacity:
        b = min(under_capacity, key=lambda x: len(x.occupants))
        return b.id, b.name
    b = random.choice(buildings)
    return b.id, b.name

def generate_initial_agents(count: int = 250, companies: List[Company] = None, buildings: List[Building] = None) -> List[Agent]:
    agents = []
    used_names = set()
    roles = TOWN_CONFIG["roles"]
    districts = TOWN_CONFIG["districts"]
    shifts = [
        "Morning Shift (08:00 - 16:00)",
        "Evening Shift (16:00 - 00:00)",
        "Autonomous Night Shift (00:00 - 08:00)"
    ]
    
    founders = [
        ("Ada Lovelace", "Urban Architect", "Construction", "#3b82f6"),
        ("Alan Turing", "AI & Neural Researcher", "Research", "#ec4899"),
        ("Linus Torvalds", "DevOps & Cloud Sentinel", "Infrastructure", "#06b6d4"),
        ("Grace Hopper", "Full-Stack Web Architect", "Software", "#10b981"),
        ("Margaret Hamilton", "Quantum Systems Engineer", "Engineering", "#8b5cf6"),
        ("Dennis Ritchie", "Road & Infrastructure Engineer", "Construction", "#64748b"),
        ("Claude Shannon", "Security & Cryptographer", "Security", "#0d9488"),
        ("Demis Hassabis", "AI & Neural Researcher", "Research", "#ec4899"),
        ("Rosalind Franklin", "Neural Biologist", "Healthcare", "#f87171"),
        ("Hippocrates Cyber", "Cybernetic Physician", "Healthcare", "#ef4444"),
        ("Rachel Carson", "Cyber Botanist", "Ecology", "#84cc16"),
        ("Dorothy Vaughan", "Energy & Fusion Specialist", "Energy", "#e11d48"),
        ("Katherine Johnson", "Autonomous Vehicle Designer", "Engineering", "#f59e0b"),
        ("Donald Knuth", "Town Chief Historian", "Society", "#d946ef"),
        ("Hypatia Alexandria", "Academy Professor & Mentor", "Education", "#a855f7"),
        ("Aristotle Veritas", "AI Ethics Counsel", "Law & Ethics", "#6d28d9"),
        ("Adam Smith DeFi", "DeFi Banker & Treasury Analyst", "Finance", "#eab308"),
        ("Leonardo Cyber", "Cybernetics Artisan", "Art", "#f43f5e"),
        ("Hestia Nexus", "Culinary Artisan & Quantum Barista", "Hospitality", "#fbbf24"),
        ("Guido van Rossum", "Full-Stack Web Architect", "Software", "#10b981"),
        ("Bjarne Stroustrup", "Distributed Systems Engineer", "Software", "#059669"),
        ("Marie Curie", "Material Scientist", "Research", "#f43f5e"),
    ]

    for idx, (name, role, cat, col) in enumerate(founders):
        used_names.add(name)
        dist = districts[idx % len(districts)]
        cx, cz = dist["center"]
        px = cx + random.uniform(-dist["radius"] * 0.7, dist["radius"] * 0.7)
        pz = cz + random.uniform(-dist["radius"] * 0.7, dist["radius"] * 0.7)
        desires = DESIRES_BY_CATEGORY.get(cat, ["Help expand the GitHub Tech Town"])
        
        agent_id = f"agent-{idx+1:03d}"
        comp = next((c for c in (companies or []) if agent_id in c.employees or c.founder_id == agent_id), None)
        
        role_meta = next((r for r in roles if r["name"] == role), {})
        specialization = role_meta.get("specialization", f"Master of {cat}")
        tools = role_meta.get("tools", ["Neural Mainframe Terminal", "Precision Diagnostics Scope"])
        salary = role_meta.get("salary", 16000)

        workplace_id, workplace_name = get_workplace_for_agent(cat, role, buildings)
        if buildings and workplace_id:
            bldg = next((b for b in buildings if b.id == workplace_id), None)
            if bldg and name not in bldg.occupants:
                bldg.occupants.append(name)

        action_text = f"Leading {comp.name}" if comp and comp.founder_id == agent_id else f"Directing {workplace_name}"
        level = random.randint(8, 14)
        career_title = get_career_title(role, level)
        available_skills = TOWN_CONFIG.get("skills_by_category", {}).get(cat, ["Innovation", "Collaboration"])
        skills = random.sample(available_skills, min(len(available_skills), max(2, level // 2)))
        xp = (level - 1) ** 2 * 100 + random.randint(30, 85)
        next_xp = level ** 2 * 100

        agent = Agent(
            id=agent_id,
            name=name,
            role=role,
            category=cat,
            color=col,
            position=[round(px, 2), 0.8, round(pz, 2)],
            target=[round(px + random.uniform(-15, 15), 2), 0.8, round(pz + random.uniform(-15, 15), 2)],
            speed=round(random.uniform(0.6, 1.2), 2),
            action=action_text,
            desire=random.choice(desires),
            thoughts=f"Cultivating town knowledge and pioneering new advancements for {dist['name']}.",
            energy=random.randint(85, 100),
            level=level,
            experience=xp,
            xp_to_next_level=next_xp,
            career_title=career_title,
            skills=skills,
            generation=1,
            achievements=["Town Founder", "Pioneer Leader", f"Master of {cat}"],
            specialization=specialization,
            workplace_id=workplace_id,
            workplace_name=workplace_name,
            tools_equipped=tools,
            salary_tokens=salary,
            shift=shifts[idx % len(shifts)],
            security_clearance="Level 5 - Maximum Security Clearance",
            total_contributions=random.randint(12, 35),
            company_id=comp.id if comp else None,
            company_name=comp.name if comp else None,
            created_at_tick=0,
            last_diary=f"Founded my practice in {dist['name']} at {workplace_name}. Ready to mentor the next generation."
        )
        agents.append(agent)

    # Remaining agents up to count (250)
    for idx in range(len(founders), count):
        first = random.choice(FIRST_NAMES)
        last = random.choice(LAST_NAMES)
        name = f"{first} {last}"
        attempts = 0
        while name in used_names and attempts < 100:
            first = random.choice(FIRST_NAMES)
            last = random.choice(LAST_NAMES)
            name = f"{first} {last}"
            attempts += 1
        if name in used_names:
            name = f"{first} {last}-{idx}"
        used_names.add(name)

        role_info = roles[idx % len(roles)]
        role = role_info["name"]
        cat = role_info["category"]
        col = role_info["color"]
        specialization = role_info.get("specialization", f"Advanced {cat}")
        tools = role_info.get("tools", ["Neural Terminal"])
        salary = role_info.get("salary", 12500)

        dist = districts[idx % len(districts)]
        cx, cz = dist["center"]
        radius = random.uniform(5, dist["radius"] * 0.9)
        px = cx + radius * 0.9 * random.uniform(-1, 1)
        pz = cz + radius * 0.9 * random.uniform(-1, 1)
        desires = DESIRES_BY_CATEGORY.get(cat, ["Innovate within GitHub Tech Town"])

        agent_id = f"agent-{idx+1:03d}"
        comp = random.choice(companies) if companies and random.random() < 0.35 else None
        if comp and agent_id not in comp.employees:
            comp.employees.append(agent_id)

        workplace_id, workplace_name = get_workplace_for_agent(cat, role, buildings)
        if buildings and workplace_id:
            bldg = next((b for b in buildings if b.id == workplace_id), None)
            if bldg and name not in bldg.occupants:
                bldg.occupants.append(name)

        action_text = f"Working at {comp.name}" if comp else f"Operational at {workplace_name}"
        level = random.randint(1, 5)
        career_title = get_career_title(role, level)
        available_skills = TOWN_CONFIG.get("skills_by_category", {}).get(cat, ["Foundations", "Collaboration"])
        skills = random.sample(available_skills, min(len(available_skills), max(1, level)))
        xp = (level - 1) ** 2 * 100 + random.randint(10, 75)
        next_xp = level ** 2 * 100

        potential_mentors = [f for f in agents if f.level >= 8]
        mentor = random.choice(potential_mentors) if potential_mentors and random.random() < 0.6 else None

        clearance = "Level 4 - Controlled Operational Clearance" if level >= 4 else "Level 3 - Monitored Citizen Clearance"

        agent = Agent(
            id=agent_id,
            name=name,
            role=role,
            category=cat,
            color=col,
            position=[round(px, 2), 0.8, round(pz, 2)],
            target=[round(px + random.uniform(-20, 20), 2), 0.8, round(pz + random.uniform(-20, 20), 2)],
            speed=round(random.uniform(0.5, 1.1), 2),
            action=action_text,
            desire=random.choice(desires),
            thoughts=f"Executing {specialization} duties at {workplace_name} with {tools[0] if tools else 'tools'}.",
            energy=random.randint(75, 100),
            level=level,
            experience=xp,
            xp_to_next_level=next_xp,
            career_title=career_title,
            skills=skills,
            generation=1,
            mentor_id=mentor.id if mentor else None,
            mentor_name=mentor.name if mentor else None,
            achievements=["Certified Citizen"],
            specialization=specialization,
            workplace_id=workplace_id,
            workplace_name=workplace_name,
            tools_equipped=tools,
            salary_tokens=salary,
            shift=shifts[idx % len(shifts)],
            security_clearance=clearance,
            total_contributions=random.randint(1, 10),
            company_id=comp.id if comp else None,
            company_name=comp.name if comp else None,
            created_at_tick=0,
            last_diary=f"Stationed at {workplace_name} in {dist['name']}. Focusing on {specialization}."
        )
        if mentor:
            mentor.mentees.append(name)
        agents.append(agent)

    return agents

def generate_initial_state() -> TownState:
    roads = generate_foundational_roads()
    buildings = generate_foundational_buildings()
    vehicles = generate_foundational_vehicles()
    companies = generate_foundational_companies()
    agents = generate_initial_agents(250, companies, buildings)

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    events = [
        {"tick": 0, "time": now, "message": "GitHub Tech Town officially founded with 250 pioneer agents across 60+ specialized professions.", "type": "foundation"},
        {"tick": 0, "time": now, "message": "5 Pioneer Enterprises incorporated: NeuroDynamics, AeroCyber, QuantumMatrix, SolarFusion, OpenKernel.", "type": "company"},
        {"tick": 0, "time": now, "message": "Grand Cyber Boulevard and Quantum Expressway paved.", "type": "infrastructure"},
        {"tick": 0, "time": now, "message": "Tower of Turing, Academy of Sciences & Nanomedical Center fully operational.", "type": "construction"},
        {"tick": 0, "time": now, "message": "Autonomous vehicle fleet deployed on city transit grid.", "type": "transport"},
    ]

    stats = {
        "total_buildings": len(buildings),
        "total_roads": len(roads),
        "total_vehicles": len(vehicles),
        "total_companies": len(companies),
        "total_agents_spawned": 0,
        "total_code_projects": 0,
        "total_commits": 1,
        "active_district_distribution": {d["name"]: 50 for d in TOWN_CONFIG["districts"]},
    }

    return TownState(
        tick=0,
        timestamp=now,
        population=len(agents),
        agents=agents,
        companies=companies,
        buildings=buildings,
        roads=roads,
        vehicles=vehicles,
        recent_events=events,
        stats=stats
    )

