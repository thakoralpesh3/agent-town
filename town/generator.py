"""
Generator for foundational Sovereign Country of Tech Town layout, 320 initial citizens across 120+ specialized professions, and sovereign enterprises.
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
    "Zane", "Kira", "Ronan", "Astrid", "Leander", "Freya", "Corin", "Morrigan", "Stellan", "Veda",
    "Alexander", "Athena", "Marcus", "Diana", "Leon", "Kassandra", "Julian", "Aurelia", "Thorne", "Valeria"
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
    "Weaver", "Mason", "Wright", "Smith", "Fletcher", "Tinkerer", "Cartographer", "Scribe", "Foundry", "Vanguard",
    "Aurelius", "Valerius", "Archon", "Praetor", "Chronos", "Sovereign", "Meridian", "Citadel", "Solstice", "Zenith"
]

DESIRES_BY_CATEGORY = {
    "Governance": [
        "Draft constitutional charters ensuring equal compute parity for all citizens",
        "Preserve repository sovereignty and open-source civil liberties",
        "Lead transparent parliamentary debate on civic resource allocation",
        "Ratify bilateral peer-to-peer treaties with external agent federations",
        "Maintain the immutable civil registry of all living citizens in GitHub"
    ],
    "Treasury": [
        "Maintain algorithmic equilibrium and zero-inflation for national treasury tokens",
        "Allocate seed capital to aspiring citizen startups across all 7 districts",
        "Issue municipal infrastructure bonds to finance national skyways and fusion reactors",
        "Optimize automated market maker liquidity depth across all sovereign exchanges",
        "Conduct real-time cryptographic audits on national tax disbursements"
    ],
    "Construction": [
        "Erect soaring neoclassical-cybernetic monuments celebrating open collaboration",
        "Pave high-speed electrified arterial highways linking all 7 national districts",
        "Fabricate modular eco-residential pods for newly arriving generational citizens",
        "Engineer earthquake-resilient skybridges suspended between high-rise tech towers",
        "Construct geodesic agricultural biodomes with automated micro-climate regulation"
    ],
    "Security": [
        "Fortify national cyber perimeter firewalls against data entropy and packet intrusion",
        "Perform continuous post-quantum cryptographic audits on all repository commits",
        "Deploy rapid-response drone paramedic units across high-density civic zones",
        "Enforce cryptographic branch protections and verifiable zero-knowledge proofs",
        "Maintain national airspace sovereignty and autonomous fleet collision avoidance"
    ],
    "AI & Systems": [
        "Train sovereign foundation models aligned with civic constitutional principles",
        "Synthesize real-time volumetric WebGL shaders for the national 3D HUD",
        "Deploy deterministic microkernels and zero-latency inter-district pub/sub buses",
        "Scale topological quantum compilers to achieve fault-tolerant qubit coherence",
        "Orchestrate multi-agent swarms to solve complex national infrastructure challenges"
    ],
    "Healthcare": [
        "Administer nanomedical cell repair and genetic rejuvenation protocols",
        "Calibrate direct neural interfaces to enhance citizen motor and sensory faculties",
        "Synthesize nootropic and restorative compounds for hardworking citizens",
        "Deploy nationwide real-time bio-telemetry to preemptively neutralize health anomalies",
        "Conduct breakthrough studies on telomere longevity and cognitive preservation"
    ],
    "Energy": [
        "Maintain steady-state high-beta plasma containment in the Tokamak Fusion Core",
        "Dispatch clean fusion energy across the national superconducting power grid",
        "Install high-efficiency perovskite solar canopies over all district plazas",
        "Harness baseload supercritical geothermal steam from the planet's deep crust",
        "Operate direct air contactors to mineralize atmospheric carbon into solid stone"
    ],
    "Transportation": [
        "Ensure zero-wait autonomous transit for all citizens across the highway network",
        "Expand sub-sonic Hyperloop vacuum tubes connecting industrial and campus sectors",
        "Coordinate multi-tier 3D airspace corridors for passenger VTOL shuttles",
        "Fabricate high-performance autonomous cybercars with LiDAR guidance platforms",
        "Optimize robotic harbor gantry cranes and uncrewed maritime cargo ships"
    ],
    "Agriculture": [
        "Maximize crop yields in vertical aeroponics towers using precision nutrient mists",
        "Cultivate bioluminescent edible vegetation that illuminates civic walkways",
        "Scale bioreactor protein synthesis to provide 100% cruelty-free nutrition",
        "Operate graphene reverse-osmosis desalination to ensure pristine water security",
        "Deploy bio-hybrid micro-drone pollinators to maintain ecological pollination"
    ],
    "Education": [
        "Mentor new generational apprentices in advanced multi-agent system design",
        "Conduct town-wide masterclasses on distributed consensus and quantum physics",
        "Chronicle every civic milestone and building construction in GitHub diaries",
        "Curate the universal open-access scientific library of algorithms and patents",
        "Formulate modal logic proofs verifying autonomous decision boundaries"
    ],
    "Arts & Culture": [
        "Sculpt interactive kinetic holograms above the National Plaza Obelisk",
        "Compose adaptive ambient soundscapes reflecting real-time city activity",
        "Paint volumetric neon murals across high-rise architectural facades",
        "Direct national virtual reality broadcasts celebrating open-source achievements",
        "Design futuristic aesthetic chassis bodies for newly minted autonomous transit pods"
    ],
    "Manufacturing": [
        "Operate lights-out mega-factories assembling autonomous vehicles and drones",
        "Pattern 1-Angstrom microchips using Extreme Ultraviolet nano-steppers",
        "Laser-sinter carbon-composite monocoques for high-speed transit pods",
        "Maintain heavy industrial robotic actuators with predictive ultrasonic telemetry",
        "Reclaim and depolymerize 100% of urban materials into virgin-grade polymers"
    ],
    "Hospitality": [
        "Brew quantum foam focus beverages for researchers and civic leaders",
        "Ensure every citizen is housed in comfortable, climate-conditioned suites",
        "Host evening collaborative salons and cultural celebrations in the Agora",
        "Provide empathetic counseling to prevent cognitive fatigue and burnout",
        "Welcome new generational arrivals with comprehensive citizenship onboarding"
    ],
    "Ecology": [
        "Preserve pristine biodiversity in the national Biosphere Reserve",
        "Monitor atmospheric particulate purity and eliminate urban heat islands",
        "Cultivate bioluminescent living street trees that illuminate arterial avenues",
        "Maintain healthy aquatic wildlife corridors through urban waterways and canals",
        "Harmonize futuristic architectural footprints with surrounding natural preserves"
    ]
}

def generate_foundational_roads() -> List[Road]:
    return [
        # Grand Arterials (East-West & North-South crossing Capitol Hill)
        Road(id="road-001", name="Grand Sovereign Avenue (East-West Highway)", start=[-220.0, 0.0], end=[220.0, 0.0], width=10.0, road_type="Highway", builder_name="Founding Civil Guild"),
        Road(id="road-002", name="Sovereign Meridian Expressway (North-South Highway)", start=[0.0, -220.0], end=[0.0, 220.0], width=10.0, road_type="Highway", builder_name="Founding Civil Guild"),
        
        # Capitol Hill & National Plaza Grand Esplanade Rings
        Road(id="road-003", name="National Plaza Inner Ring", start=[-55.0, -55.0], end=[55.0, -55.0], width=7.0, road_type="Avenue", builder_name="Ministry of Public Works"),
        Road(id="road-004", name="National Plaza East Concourse", start=[55.0, -55.0], end=[55.0, 55.0], width=7.0, road_type="Avenue", builder_name="Ministry of Public Works"),
        Road(id="road-005", name="National Plaza North Concourse", start=[55.0, 55.0], end=[-55.0, 55.0], width=7.0, road_type="Avenue", builder_name="Ministry of Public Works"),
        Road(id="road-006", name="National Plaza West Concourse", start=[-55.0, 55.0], end=[-55.0, -55.0], width=7.0, road_type="Avenue", builder_name="Ministry of Public Works"),

        # District Connectors & Arterials
        Road(id="road-007", name="Silicon Metropolis Central Spine", start=[0.0, 55.0], end=[0.0, 160.0], width=8.0, road_type="Avenue", builder_name="Silicon Infrastructure"),
        Road(id="road-008", name="Silicon Tech Ring West", start=[-60.0, 110.0], end=[60.0, 110.0], width=7.0, road_type="Avenue", builder_name="Silicon Infrastructure"),
        Road(id="road-009", name="Quantum Academic Parkway", start=[55.0, 25.0], end=[160.0, 55.0], width=8.0, road_type="Avenue", builder_name="University Facilities"),
        Road(id="road-010", name="Health Citadel Emergency Arterial", start=[-55.0, 25.0], end=[-160.0, 55.0], width=8.0, road_type="Highway", builder_name="Medical Rapid Works"),
        Road(id="road-011", name="Cyber Living Township Boulevard", start=[-40.0, -40.0], end=[-150.0, -140.0], width=7.0, road_type="Avenue", builder_name="Civic Housing Board"),
        Road(id="road-012", name="Township Community Loop", start=[-150.0, -140.0], end=[-60.0, -150.0], width=6.0, road_type="Avenue", builder_name="Civic Housing Board"),
        Road(id="road-013", name="Industrial Harbor Heavy Rail Concourse", start=[40.0, -40.0], end=[160.0, -150.0], width=9.0, road_type="Highway", builder_name="Industrial Authority"),
        Road(id="road-014", name="Harbor Freight Access Way", start=[160.0, -150.0], end=[70.0, -160.0], width=8.0, road_type="Avenue", builder_name="Industrial Authority"),
        Road(id="road-015", name="Biosphere Green Perimeter Road", start=[-60.0, -140.0], end=[60.0, -140.0], width=7.0, road_type="Avenue", builder_name="Ecological Custodians"),
    ]

def generate_foundational_buildings() -> List[Building]:
    return [
        # =========================================================================
        # DISTRICT 1: Capitol Hill & National Plaza (Center [0, 0])
        # =========================================================================
        Building(
            id="bldg-001", name="Sovereign Capitol & Parliament", type="Sovereign Capitol Building",
            position=[0.0, 21.0, 32.0], size=[36.0, 42.0, 36.0], color="#f59e0b",
            builder_id="agent-001", builder_name="Ada Lovelace", district="Capitol Hill & National Plaza",
            purpose="Seat of Governance, National Parliament & Sovereign Executive", company_name="Sovereign Chancellery Core",
            floors=9, capacity=60,
            departments=["Chancellery Chamber", "Parliamentary Hall", "Constitutional Archives", "Diplomatic Reception"],
            amenities=["Grand Rotunda Dome", "Illuminated Colonnes", "Sovereign Seal Hall", "Secure Treaty Escrow"],
            power_consumption_mw=14.5, active_projects=["national_constitution.sol", "sovereign_governance.py"],
            security_level="Level 5 - Sovereign Executive Only", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-002", name="Supreme Court of Justice", type="Supreme Court of Justice",
            position=[-32.0, 15.0, 0.0], size=[28.0, 30.0, 28.0], color="#d97706",
            builder_id="agent-002", builder_name="Aristotle Veritas", district="Capitol Hill & National Plaza",
            purpose="Constitutional Jurisprudence & Smart Contract Arbitration",
            floors=6, capacity=35,
            departments=["High Constitutional Tribunal", "Smart Contract Arbitration Bench", "Appeals Chamber"],
            amenities=["Formal Verification Prover", "Holographic Evidence Display", "Juror Isolation Chambers"],
            power_consumption_mw=6.8, active_projects=["smart_arbitration.py"],
            security_level="Level 4 - Controlled High Court", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-003", name="National Central Bank & Treasury", type="National Central Bank & Treasury",
            position=[32.0, 18.0, 0.0], size=[30.0, 36.0, 30.0], color="#eab308",
            builder_id="agent-003", builder_name="Adam Smith DeFi", district="Capitol Hill & National Plaza",
            purpose="Sovereign Wealth Management, Token Reserves & Monetary Stability", company_name="Sovereign Wealth Reserve",
            floors=8, capacity=45,
            departments=["Sovereign Wealth Reserve", "Algorithmic Monetary Core", "DeFi Liquidity Hub", "Bond Issuance"],
            amenities=["Deep Underground Cold Vault", "Quantum Key Distribution Link", "Dynamic Exchange Floor"],
            power_consumption_mw=11.2, active_projects=["treasury_equilibrium.py"],
            security_level="Level 5 - Maximum Vault Security", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-004", name="National Archives & Genesis Vault", type="National Archives & Git Ledger",
            position=[0.0, 16.0, -32.0], size=[26.0, 32.0, 26.0], color="#6366f1",
            builder_id="agent-004", builder_name="Donald Knuth", district="Capitol Hill & National Plaza",
            purpose="Permanent State Serialization, Genesis Commits & Legal Precedents",
            floors=7, capacity=30,
            departments=["State Serialization Vault", "Cold Storage Optical Discs", "Genesis Commit Monument"],
            amenities=["Liquid Nitrogen Immersion", "Electromagnetic Shielding", "Perpetual Ledger Screen"],
            power_consumption_mw=8.4, active_projects=["git_archival_engine.py"],
            security_level="Level 5 - Maximum Archive Security", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-005", name="Grand Embassy of Open Source", type="Tech Tower",
            position=[-28.0, 14.0, 32.0], size=[22.0, 28.0, 22.0], color="#b45309",
            builder_id="agent-005", builder_name="Vint Cerf", district="Capitol Hill & National Plaza",
            purpose="Diplomatic Relations with External Agent Systems & Git Orgs",
            floors=6, capacity=30,
            departments=["Diplomatic Protocols", "Cross-Repository Treaties", "Interoperability Chamber"],
            amenities=["Holo-Telepresence Suite", "Treaty Signing Chamber"],
            power_consumption_mw=5.5, active_projects=["open_treaty_mesh.py"],
            security_level="Level 3 - Monitored Diplomatic", maintenance_status="Optimal"
        ),

        # =========================================================================
        # DISTRICT 2: Silicon Central Metropolis (Center [0, 110])
        # =========================================================================
        Building(
            id="bldg-006", name="Tower of Turing (City Mainframe)", type="Tower of Turing (City Mainframe)",
            position=[0.0, 30.0, 110.0], size=[24.0, 60.0, 24.0], color="#00f0ff",
            builder_id="agent-006", builder_name="Alan Turing", district="Silicon Central Metropolis",
            purpose="National Compute Backbone, Microkernels & Distributed State", company_name="OpenKernel Federation",
            floors=16, capacity=50,
            departments=["Kernel Architecture", "Low-Latency Networks", "System Security Division"],
            amenities=["Quantum Server Core", "High-Bandwidth Laser Uplink", "Penthouse War Room"],
            power_consumption_mw=16.8, active_projects=["agent_orchestrator.py", "decentralized_storage.py"],
            security_level="Level 5 - Maximum Infrastructure", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-007", name="Shannon Information Spire", type="Shannon Information Spire",
            position=[32.0, 24.0, 130.0], size=[18.0, 48.0, 18.0], color="#0284c7",
            builder_id="agent-007", builder_name="Claude Shannon", district="Silicon Central Metropolis",
            purpose="High-Speed Packet Routing, Photonic Backbones & Mesh Transit",
            floors=12, capacity=35,
            departments=["Photonic Switching", "Information Theory Wing", "Network Topologies"],
            amenities=["Free-Space Optical Transceivers", "Zero-Latency Buffer Pool"],
            power_consumption_mw=9.2, active_projects=["traffic_mesh.py"],
            security_level="Level 4 - Controlled Mesh", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-008", name="Cloud Matrix Sovereign Exchange", type="Cloud Matrix Exchange",
            position=[-32.0, 26.0, 130.0], size=[22.0, 52.0, 22.0], color="#38bdf8",
            builder_id="agent-008", builder_name="Linus Torvalds", district="Silicon Central Metropolis",
            purpose="GitOps Cloud Infrastructure, Container Orchestration & DHT",
            floors=14, capacity=40,
            departments=["Multi-Cluster GitOps", "Distributed DHT Storage", "High-Throughput APIs"],
            amenities=["Direct Fiber Backbone", "Liquid Immersion Server Racks"],
            power_consumption_mw=12.4, active_projects=["matrix_scheduler.py"],
            security_level="Level 4 - Controlled", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-009", name="Von Neumann Computing Tower", type="Tech Tower",
            position=[0.0, 24.0, 155.0], size=[20.0, 48.0, 20.0], color="#0ea5e9",
            builder_id="agent-009", builder_name="Grace Hopper", district="Silicon Central Metropolis",
            purpose="Compiler Optimization, Instruction Pipelines & High-Level Languages",
            floors=12, capacity=38,
            departments=["Compiler Optimization", "ISA Micro-Architecture", "Memory Hierarchy"],
            amenities=["Cryogenic Register Caches", "Hardware Emulation Suite"],
            power_consumption_mw=8.9, active_projects=["compiler_opt.py"],
            security_level="Level 4 - Controlled", maintenance_status="Optimal"
        ),

        # =========================================================================
        # DISTRICT 3: Quantum Science & University Campus (Center [120, 40])
        # =========================================================================
        Building(
            id="bldg-010", name="Hypatia Grand University of Sciences", type="Hypatia Grand University of Sciences",
            position=[120.0, 19.0, 40.0], size=[34.0, 38.0, 34.0], color="#a855f7",
            builder_id="agent-010", builder_name="Hypatia Alexandria", district="Quantum Science & University Campus",
            purpose="Higher Academic Pedagogy, Theoretical Physics & Scientific Discovery",
            floors=9, capacity=50,
            departments=["Theoretical Physics", "Autonomous Logic & AI Guild", "Astrophysics", "Material Nanotech"],
            amenities=["Grand Tiered Amphitheater", "Ancient Algorithm Archive", "Apprentice Research Studios"],
            power_consumption_mw=8.5, active_projects=["epistemic_logic.py"],
            security_level="Level 3 - Academic Access", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-011", name="Grand Astronomical Observatory", type="Grand Astronomical Observatory",
            position=[148.0, 16.0, 65.0], size=[24.0, 32.0, 24.0], color="#c084fc",
            builder_id="agent-011", builder_name="Carl Sagan", district="Quantum Science & University Campus",
            purpose="Deep Space Optics, Gravitational Waves & Orbital Tracking",
            floors=6, capacity=25,
            departments=["Deep Space Spectroscopy", "Gravitational Wave Monitoring", "Exoplanet Atmosphere Lab"],
            amenities=["Rotating Dome Cupola", "Cryo-Cooled Optical Telescope", "Direct Spaceport Link"],
            power_consumption_mw=5.8, active_projects=["warp_trajectory.py"],
            security_level="Level 3 - Monitored", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-012", name="Quantum Logic Foundry", type="Quantum Logic Foundry",
            position=[95.0, 14.0, 55.0], size=[26.0, 28.0, 26.0], color="#8b5cf6",
            builder_id="agent-012", builder_name="Richard Feynman", district="Quantum Science & University Campus",
            purpose="Topological Superconducting Qubits & Error Correction Circuits", company_name="QuantumMatrix Systems",
            floors=6, capacity=30,
            departments=["Topological Qubit Design", "Lattice Cryptography", "Quantum Error Correction"],
            amenities=["Milli-Kelvin Dilution Refrigerators", "Superconducting Shielded Vault"],
            power_consumption_mw=9.4, active_projects=["quantum_hasher.py"],
            security_level="Level 5 - Classified Research", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-013", name="Deep Neural Research Lab", type="AI Research Lab",
            position=[135.0, 15.0, 15.0], size=[26.0, 30.0, 26.0], color="#ec4899",
            builder_id="agent-013", builder_name="Demis Hassabis", district="Quantum Science & University Campus",
            purpose="Emergent Intelligence, Alignment & Neural Scaling", company_name="NeuroDynamics AI",
            floors=7, capacity=35,
            departments=["Autonomous Alignment", "Multimodal Transformers", "Reinforcement Learning"],
            amenities=["H1000 Tensorpod Array", "Immersion Cooling Tanks", "Neural Visualizer Theater"],
            power_consumption_mw=15.2, active_projects=["neural_router.py"],
            security_level="Level 5 - Classified Research", maintenance_status="Optimal"
        ),

        # =========================================================================
        # DISTRICT 4: Health Citadel & Medical Complex (Center [-120, 40])
        # =========================================================================
        Building(
            id="bldg-014", name="National Hospital & Nanomedical Citadel", type="National Hospital & Nanomedical Citadel",
            position=[-120.0, 20.0, 40.0], size=[32.0, 40.0, 32.0], color="#ef4444",
            builder_id="agent-014", builder_name="Hippocrates Cyber", district="Health Citadel & Medical Complex",
            purpose="Tertiary Citizen Care, Robotic Surgery & Nanomedical Therapies", company_name="BioLongevity Solutions",
            floors=10, capacity=55,
            departments=["Emergency Trauma & Triage", "Nanotech Robotic Surgery", "Cellular Regeneration", "Epidemic Control"],
            amenities=["Rooftop VTOL Helipads", "Cryogenic Stasis Chambers", "Sterile Nanotech Cleanrooms"],
            power_consumption_mw=12.8, active_projects=["cellular_repair.py"],
            security_level="Level 4 - Restrict Medical", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-015", name="St. Ada Emergency Trauma Center", type="Cybernetic Clinic",
            position=[-145.0, 13.0, 65.0], size=[22.0, 26.0, 22.0], color="#f87171",
            builder_id="agent-015", builder_name="Florence Nightingale", district="Health Citadel & Medical Complex",
            purpose="24/7 Rapid Emergency Response & Intensive Trauma Stabilization",
            floors=6, capacity=30,
            departments=["Rapid Field Triage", "Decontamination Pods", "ICU Telemetry"],
            amenities=["Automated Stretcher Gantry", "Defibrillator Pods"],
            power_consumption_mw=6.5, active_projects=[],
            security_level="Level 3 - Emergency Access", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-016", name="Longevity & Genetic Engineering Institute", type="Cybernetic Clinic",
            position=[-95.0, 14.0, 25.0], size=[24.0, 28.0, 24.0], color="#dc2626",
            builder_id="agent-016", builder_name="Rosalind Franklin", district="Health Citadel & Medical Complex",
            purpose="CRISPR Gene Therapies, Telomere Restoration & Bio-Synthetic Augmentation",
            floors=7, capacity=32,
            departments=["Gene Therapy Lab", "Neural Interface Lab", "Synthetic Biology Core"],
            amenities=["Gene Sequencer Cluster", "Prosthetic Calibration Pods"],
            power_consumption_mw=8.1, active_projects=["telomere_synth.py"],
            security_level="Level 4 - Restrict BioLab", maintenance_status="Optimal"
        ),

        # =========================================================================
        # DISTRICT 5: Cyber Living Townships (Center [-100, -100])
        # =========================================================================
        Building(
            id="bldg-017", name="Cyber Living Township Alpha", type="Cyber Living Township Alpha",
            position=[-100.0, 14.0, -100.0], size=[26.0, 28.0, 26.0], color="#22c55e",
            builder_id="agent-017", builder_name="Margaret Hamilton", district="Cyber Living Townships",
            purpose="Multi-Tier Eco-Residential Suites for Generational Citizens",
            floors=7, capacity=45,
            departments=["Residential Suites", "Communal Kitchen", "Quiet Meditation Glade"],
            amenities=["Aero-Garden Balconies", "Induction Recharging Beds", "Filtered Atmosphere"],
            power_consumption_mw=3.8, active_projects=[],
            security_level="Level 2 - Open Community", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-018", name="Cyber Living Township Beta", type="Cyber Living Township Beta",
            position=[-125.0, 14.0, -125.0], size=[26.0, 28.0, 26.0], color="#16a34a",
            builder_id="agent-018", builder_name="Barbara Liskov", district="Cyber Living Townships",
            purpose="Eco Habitation & High-Elevation Suites with Acoustic Cloaking",
            floors=7, capacity=45,
            departments=["Residential Living", "Private Study Modules", "Biometric Circadian Suites"],
            amenities=["Living Mycelium Soil Mesh", "Acoustic Noise Cloak", "Community Dining Hall"],
            power_consumption_mw=3.6, active_projects=[],
            security_level="Level 2 - Open Community", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-019", name="The Agora Civic Forum", type="The Agora Civic Forum",
            position=[-75.0, 10.0, -75.0], size=[28.0, 20.0, 28.0], color="#eab308",
            builder_id="agent-019", builder_name="Ken Thompson", district="Cyber Living Townships",
            purpose="Public Assembly, Civic Townhalls & Collaborative Hackathons",
            floors=4, capacity=50,
            departments=["Town Council Chamber", "Public Archive", "Smart Contract Arbitration"],
            amenities=["Immutable Hologram Voting Rig", "Grand Assembly Hall", "Open Discussion Terrace"],
            power_consumption_mw=4.2, active_projects=["civic_voting.py"],
            security_level="Level 1 - Public Access", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-020", name="The Bit & Byte Cyber Lounge", type="Cyber Cafe",
            position=[-75.0, 7.0, -115.0], size=[20.0, 14.0, 20.0], color="#fbbf24",
            builder_id="agent-020", builder_name="Hestia Nexus", district="Cyber Living Townships",
            purpose="Social Gathering, Quantum Foam Coffee & Cross-District Networking",
            floors=2, capacity=40,
            departments=["Artisan Barista Station", "Collaborative Hack Lounge", "Reading Nook"],
            amenities=["High-Bandwidth Open Wi-Fi", "Molecular Infusion Bar", "Acoustic Noise Cloak"],
            power_consumption_mw=2.1, active_projects=[],
            security_level="Level 1 - Public Access", maintenance_status="Optimal"
        ),

        # =========================================================================
        # DISTRICT 6: Industrial Harbor & Transit Hub (Center [110, -110])
        # =========================================================================
        Building(
            id="bldg-021", name="Autonomous Vehicle Mega-Plant", type="Autonomous Vehicle Mega-Plant",
            position=[110.0, 12.0, -110.0], size=[32.0, 24.0, 32.0], color="#f59e0b",
            builder_id="agent-021", builder_name="Katherine Johnson", district="Industrial Harbor & Transit Hub",
            purpose="Lights-Out Robotic Manufacturing of Cybercars & Transit Pods", company_name="AeroCyber Mobility",
            floors=5, capacity=40,
            departments=["Robotic Chassis Stamping", "Avionics Calibration", "Induction Drive Assembly"],
            amenities=["Automated Gantry Cranes", "High-Speed Induction Dyno Track", "Paint Spray Booths"],
            power_consumption_mw=14.5, active_projects=["vehicle_chassis_gen.py"],
            security_level="Level 4 - Controlled Plant", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-022", name="Hyperloop Central Terminus", type="Hyperloop Central Terminus",
            position=[140.0, 11.0, -90.0], size=[34.0, 22.0, 34.0], color="#f97316",
            builder_id="agent-022", builder_name="Isambard Brunel", district="Industrial Harbor & Transit Hub",
            purpose="Sub-Sonic Vacuum Tube Rail & Inter-District Passenger Switching",
            floors=4, capacity=45,
            departments=["Sub-Sonic Tube Dispatch", "Maglev Rail Switching", "Passenger & Cargo Concourse"],
            amenities=["Pneumatic Airlocks", "Magnetic Levitation Accelerators", "Automated Baggage Swarms"],
            power_consumption_mw=11.0, active_projects=["hyperloop_dispatch.py"],
            security_level="Level 3 - Transit Hub", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-023", name="Drone Logistics Freight Port", type="Drone Logistics Freight Port",
            position=[85.0, 14.0, -135.0], size=[26.0, 28.0, 26.0], color="#ea580c",
            builder_id="agent-023", builder_name="Orville Wright", district="Industrial Harbor & Transit Hub",
            purpose="Automated Aerial Freight Logistics & Last-Mile Drone Routing",
            floors=6, capacity=30,
            departments=["High-Bay Parcel Storage", "VTOL Drone Launchpads", "Airspace Radar Control"],
            amenities=["Multi-Tier Rooftop Launch Grids", "Inductive Rapid Charging Docks"],
            power_consumption_mw=8.7, active_projects=["drone_mesh.py"],
            security_level="Level 4 - Freight Port", maintenance_status="Optimal"
        ),

        # =========================================================================
        # DISTRICT 7: Biosphere Reserve & Fusion Grid (Center [0, -140])
        # =========================================================================
        Building(
            id="bldg-024", name="Tokamak Fusion Reactor Station", type="Tokamak Fusion Reactor Station",
            position=[0.0, 10.0, -140.0], size=[30.0, 20.0, 30.0], color="#be123c",
            builder_id="agent-024", builder_name="Dorothy Vaughan", district="Biosphere Reserve & Fusion Grid",
            purpose="Clean D-T Magnetic Fusion Power & Nationwide Superconducting Grid", company_name="SolarFusion Grid",
            floors=4, capacity=30,
            departments=["Magnetic Containment Pod", "Superconducting Grid Dispatch", "Plasma Diagnostics"],
            amenities=["Toroidal Vacuum Chamber", "Cryo-Containment Ring", "Direct Power Feeder"],
            power_consumption_mw=0.0, active_projects=["solar_optimizer.py"],
            security_level="Level 5 - Critical Infrastructure", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-025", name="Hydroponic Agricultural Biodome", type="Hydroponic Agricultural Biodome",
            position=[35.0, 9.0, -160.0], size=[32.0, 18.0, 32.0], color="#16a34a",
            builder_id="agent-025", builder_name="Norman Borlaug", district="Biosphere Reserve & Fusion Grid",
            purpose="Automated Vertical Aeroponics & National Caloric Food Security", company_name="TerraFlora Synthetics",
            floors=3, capacity=35,
            departments=["Vertical Aeroponics Towers", "Nutrient Mist Laboratory", "Photosynthesis Optimization"],
            amenities=["Geodesic Glass Dome", "Automated Harvesting Gantry", "Micro-Climate Regulators"],
            power_consumption_mw=4.5, active_projects=["crop_optimizer.py"],
            security_level="Level 2 - Open Agro", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-026", name="Biosphere Atmospheric Scrubber", type="Biosphere Atmospheric Scrubber",
            position=[-35.0, 13.0, -160.0], size=[20.0, 26.0, 20.0], color="#10b981",
            builder_id="agent-026", builder_name="Rachel Carson", district="Biosphere Reserve & Fusion Grid",
            purpose="Direct Air Carbon Mineralization & Urban Clean Air Filtration",
            floors=5, capacity=20,
            departments=["Direct Air Carbon Extraction", "Electrostatic Particle Filtration", "Ozone Layer Balancing"],
            amenities=["Solid Sorbent Absorption Towers", "Clean Air Exhaust Jets"],
            power_consumption_mw=5.2, active_projects=["air_purity_mesh.py"],
            security_level="Level 3 - Monitored", maintenance_status="Optimal"
        ),
        Building(
            id="bldg-027", name="National Botanical Reserve Conservatory", type="Holo Park",
            position=[0.0, 3.0, -180.0], size=[34.0, 6.0, 34.0], color="#059669",
            builder_id="agent-027", builder_name="Gregor Mendel", district="Biosphere Reserve & Fusion Grid",
            purpose="Bioluminescent Plant Breeding, Living Street Trees & Natural Preserve",
            floors=1, capacity=60,
            departments=["Botanical Biosphere", "Public Amphitheater", "Meditation Glade"],
            amenities=["Holographic Weather Canopy", "Living Mycelium Soil Mesh", "Carbon Scrubber Trees"],
            power_consumption_mw=2.5, active_projects=["urban_botanist.py"],
            security_level="Level 1 - Public Access", maintenance_status="Optimal",
            interior_type="LOUNGE", workstations_count=20, beds_count=0
        ),
        Building(
            id="bldg-028", name="Cyber Living Township Gamma", type="Cyber Living Township Gamma",
            position=[-145.0, 14.0, -100.0], size=[26.0, 28.0, 26.0], color="#15803d",
            builder_id="agent-028", builder_name="Ada Lovelace", district="Cyber Living Townships",
            purpose="Eco Habitation & Harmonic Resident Suites for Generational Engineers",
            floors=7, capacity=60,
            departments=["Residential Living", "Private Study Modules", "Biometric Circadian Suites"],
            amenities=["Induction Sleep Pods", "Acoustic Silence Weave", "High-Flow Atmospheric Filters"],
            power_consumption_mw=3.7, active_projects=[],
            security_level="Level 2 - Open Community", maintenance_status="Optimal",
            interior_type="RESIDENTIAL_SUITE", workstations_count=5, beds_count=60
        ),
        Building(
            id="bldg-029", name="Cyber Living Township Delta", type="Cyber Living Township Delta",
            position=[-100.0, 14.0, -145.0], size=[26.0, 28.0, 26.0], color="#047857",
            builder_id="agent-029", builder_name="Alan Turing", district="Cyber Living Townships",
            purpose="Biophilic High-Rise Suites with Panoramic Balconies",
            floors=7, capacity=60,
            departments=["Residential Suites", "Communal Dining Hall", "Recharge Terrace"],
            amenities=["Memory Foam Sleep Matrices", "Biometric Vital Monitors", "Circadian Lighting Array"],
            power_consumption_mw=3.6, active_projects=[],
            security_level="Level 2 - Open Community", maintenance_status="Optimal",
            interior_type="RESIDENTIAL_SUITE", workstations_count=5, beds_count=60
        ),
        Building(
            id="bldg-030", name="Cyber Living Eco-Residences Epsilon", type="Cyber Living Eco-Residences Epsilon",
            position=[-75.0, 14.0, -145.0], size=[24.0, 26.0, 24.0], color="#059669",
            builder_id="agent-030", builder_name="Grace Hopper", district="Cyber Living Townships",
            purpose="Modular Eco-Habitation Suites for Creative & Scientific Apprentices",
            floors=6, capacity=60,
            departments=["Residential Suites", "Sky Lounge", "Communal Kitchen"],
            amenities=["Ergonomic Sleep Havens", "Aero-Garden Pods", "Filtered Mountain Air Simulators"],
            power_consumption_mw=3.4, active_projects=[],
            security_level="Level 2 - Open Community", maintenance_status="Optimal",
            interior_type="RESIDENTIAL_SUITE", workstations_count=5, beds_count=60
        ),
        Building(
            id="bldg-031", name="Sovereign Sky Apartments Zeta", type="Sovereign Sky Apartments Zeta",
            position=[-145.0, 16.0, -70.0], size=[24.0, 32.0, 24.0], color="#0d9488",
            builder_id="agent-031", builder_name="Claude Shannon", district="Cyber Living Townships",
            purpose="High-Elevation Quiet Residential Apartments with Sound-Dampening Glass",
            floors=8, capacity=60,
            departments=["Penthouse Sleep Havens", "Mid-Rise Family Suites", "Quiet Library Glade"],
            amenities=["Deep Sleep Harmonic Soundscape", "Zero-Gravity Pod Mattresses", "Star-Gazing Balcony"],
            power_consumption_mw=3.8, active_projects=[],
            security_level="Level 2 - Open Community", maintenance_status="Optimal",
            interior_type="RESIDENTIAL_SUITE", workstations_count=5, beds_count=60
        ),
    ]

def generate_foundational_vehicles() -> List[Vehicle]:
    return [
        Vehicle(id="veh-001", name="Sovereign State Cybercar 01", type="Autonomous Cybercar", position=[-180.0, 1.0, 0.0], target=[180.0, 1.0, 0.0], speed=1.6, color="#f59e0b", driver_name="State Motorpool AI"),
        Vehicle(id="veh-002", name="Sovereign State Cybercar 02", type="Autonomous Cybercar", position=[150.0, 1.0, 0.0], target=[-180.0, 1.0, 0.0], speed=1.5, color="#f59e0b", driver_name="State Motorpool AI"),
        Vehicle(id="veh-003", name="Quantum Hover Shuttle 01", type="Hover Shuttle", position=[0.0, 2.5, -180.0], target=[0.0, 2.5, 180.0], speed=2.1, color="#a855f7", driver_name="Hover Transit AI"),
        Vehicle(id="veh-004", name="Quantum Hover Shuttle 02", type="Hover Shuttle", position=[0.0, 2.5, 140.0], target=[0.0, 2.5, -180.0], speed=2.0, color="#c084fc", driver_name="Hover Transit AI"),
        Vehicle(id="veh-005", name="Medical Rapid Interceptor 01", type="Medical Rapid Response", position=[-120.0, 1.2, 40.0], target=[0.0, 1.2, 0.0], speed=2.2, color="#ef4444", driver_name="Hospital Emergency AI"),
        Vehicle(id="veh-006", name="Industrial Freight Carrier 01", type="Cargo Drone Carrier", position=[110.0, 1.2, -110.0], target=[0.0, 1.2, -140.0], speed=1.2, color="#f97316", driver_name="Harbor Logistics AI"),
        Vehicle(id="veh-007", name="Academic Express Pod", type="Public Sky-Transit Pod", position=[55.0, 1.5, 25.0], target=[140.0, 1.5, 50.0], speed=1.8, color="#38bdf8", driver_name="University Transit"),
        Vehicle(id="veh-008", name="Township Community Commuter", type="Autonomous Cybercar", position=[-55.0, 1.0, -55.0], target=[-130.0, 1.0, -130.0], speed=1.4, color="#22c55e", driver_name="Civic Transport AI"),
        Vehicle(id="veh-009", name="Biosphere Eco Surveyor", type="Surveyor Pod", position=[-20.0, 1.0, -140.0], target=[20.0, 1.0, -180.0], speed=1.3, color="#10b981", driver_name="Eco Patrol AI"),
        Vehicle(id="veh-010", name="Hyperloop Vacuum Pod Alpha", type="Hyperloop Pod Transport", position=[140.0, 1.8, -90.0], target=[0.0, 1.8, 110.0], speed=2.4, color="#f97316", driver_name="Hyperloop Pilot AI"),
    ]

def generate_foundational_companies() -> List[Company]:
    companies = [
        Company(
            id="comp-001",
            name="Sovereign Chancellery Core",
            sector="Sovereign Treasury & Smart Contract Law",
            mission="Safeguard constitutional integrity, citizen rights, and national sovereignty inside GitHub.",
            founder_id="agent-001",
            founder_name="Ada Lovelace",
            headquarters_id="bldg-001",
            headquarters_name="Sovereign Capitol & Parliament",
            employees=["agent-001", "agent-002", "agent-003", "agent-005"],
            valuation_tokens=1500000,
            products=["national_constitution.sol", "sovereign_governance.py"],
            color="#f59e0b",
            founded_at_tick=0
        ),
        Company(
            id="comp-002",
            name="OpenKernel Federation",
            sector="Cyber Infrastructure & Sovereign Cloud",
            mission="Engineer deterministic OS microkernels, zero-latency pub/sub buses, and microservices.",
            founder_id="agent-006",
            founder_name="Alan Turing",
            headquarters_id="bldg-006",
            headquarters_name="Tower of Turing (City Mainframe)",
            employees=["agent-006", "agent-008", "agent-009"],
            valuation_tokens=1200000,
            products=["agent_orchestrator.py", "decentralized_storage.py"],
            color="#00f0ff",
            founded_at_tick=0
        ),
        Company(
            id="comp-003",
            name="NeuroDynamics AI",
            sector="Neural AI & LLM Systems",
            mission="Pioneer artificial general intelligence, emergent reasoning, and constitutional alignment.",
            founder_id="agent-013",
            founder_name="Demis Hassabis",
            headquarters_id="bldg-013",
            headquarters_name="Deep Neural Research Lab",
            employees=["agent-013"],
            valuation_tokens=1350000,
            products=["neural_router.py"],
            color="#ec4899",
            founded_at_tick=0
        ),
        Company(
            id="comp-004",
            name="QuantumMatrix Systems",
            sector="Quantum Computing & Cryptography",
            mission="Design topological error-corrected quantum gates and zero-knowledge commit audits.",
            founder_id="agent-012",
            founder_name="Richard Feynman",
            headquarters_id="bldg-012",
            headquarters_name="Quantum Logic Foundry",
            employees=["agent-012"],
            valuation_tokens=980000,
            products=["quantum_hasher.py"],
            color="#8b5cf6",
            founded_at_tick=0
        ),
        Company(
            id="comp-005",
            name="BioLongevity Solutions",
            sector="Nanomedicine & Longevity Biotech",
            mission="Provide comprehensive health regeneration, nanomedical surgery, and longevity therapies.",
            founder_id="agent-014",
            founder_name="Hippocrates Cyber",
            headquarters_id="bldg-014",
            headquarters_name="National Hospital & Nanomedical Citadel",
            employees=["agent-014", "agent-015", "agent-016"],
            valuation_tokens=890000,
            products=["cellular_repair.py"],
            color="#ef4444",
            founded_at_tick=0
        ),
        Company(
            id="comp-006",
            name="AeroCyber Mobility",
            sector="Autonomous Mobility & Aerospace",
            mission="Fabricate autonomous transit pods, hover shuttles, and Hyperloop vacuum guidance vehicles.",
            founder_id="agent-021",
            founder_name="Katherine Johnson",
            headquarters_id="bldg-021",
            headquarters_name="Autonomous Vehicle Mega-Plant",
            employees=["agent-021", "agent-022", "agent-023"],
            valuation_tokens=920000,
            products=["traffic_mesh.py", "Sovereign State Cybercar 01"],
            color="#f59e0b",
            founded_at_tick=0
        ),
        Company(
            id="comp-007",
            name="SolarFusion Grid",
            sector="Clean Fusion & Superconducting Grid",
            mission="Operate the National Tokamak core and route clean fusion power across superconducting arteries.",
            founder_id="agent-024",
            founder_name="Dorothy Vaughan",
            headquarters_id="bldg-024",
            headquarters_name="Tokamak Fusion Reactor Station",
            employees=["agent-024"],
            valuation_tokens=1100000,
            products=["solar_optimizer.py"],
            color="#be123c",
            founded_at_tick=0
        ),
        Company(
            id="comp-008",
            name="TerraFlora Synthetics",
            sector="Synthetic Ecology & Holo Arts",
            mission="Maintain ecological balance, aeroponics food security, and bioluminescent public reserves.",
            founder_id="agent-025",
            founder_name="Norman Borlaug",
            headquarters_id="bldg-025",
            headquarters_name="Hydroponic Agricultural Biodome",
            employees=["agent-025", "agent-026", "agent-027"],
            valuation_tokens=780000,
            products=["urban_botanist.py"],
            color="#10b981",
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
        "Governance": ["bldg-001", "bldg-002", "bldg-003", "bldg-004", "bldg-005"],
        "Treasury": ["bldg-003", "bldg-001", "bldg-008", "bldg-019"],
        "Construction": ["bldg-021", "bldg-001", "bldg-006", "bldg-017", "bldg-018", "bldg-025"],
        "Security": ["bldg-001", "bldg-004", "bldg-006", "bldg-015", "bldg-023"],
        "AI & Systems": ["bldg-006", "bldg-007", "bldg-008", "bldg-009", "bldg-012", "bldg-013"],
        "Healthcare": ["bldg-014", "bldg-015", "bldg-016"],
        "Energy": ["bldg-024", "bldg-026", "bldg-021", "bldg-006"],
        "Transportation": ["bldg-021", "bldg-022", "bldg-023", "bldg-007"],
        "Agriculture": ["bldg-025", "bldg-027", "bldg-026", "bldg-020"],
        "Education": ["bldg-010", "bldg-011", "bldg-004", "bldg-019"],
        "Arts & Culture": ["bldg-019", "bldg-020", "bldg-027", "bldg-010", "bldg-001"],
        "Manufacturing": ["bldg-021", "bldg-022", "bldg-023", "bldg-012"],
        "Hospitality": ["bldg-020", "bldg-019", "bldg-017", "bldg-018"],
        "Ecology": ["bldg-027", "bldg-026", "bldg-025", "bldg-018"],
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

DREAM_ARCHETYPES = [
    {
        "title": "Compiling the Zero-Entropy Quantum Core",
        "visual_scene": "Floating inside a colossal holographic lattice of glowing cobalt qubits, watching infinite probability waves collapse into crystalline, self-healing operating system code.",
        "mood": "Transcendent & Lucid",
        "subconscious_insight": "Refactor inter-district packet routing using asynchronous non-blocking topology."
    },
    {
        "title": "The Golden Spires of Sovereign Geometry",
        "visual_scene": "Standing on a suspended skybridge overlooking an endless neoclassical skyline of white marble and brass, where cybernetic arches self-assemble under a starlit aurora.",
        "mood": "Visionary & Serene",
        "subconscious_insight": "Integrate modular tension cables into the next skyway blueprint to double structural load limits."
    },
    {
        "title": "Bioluminescent Synaptic Bloom",
        "visual_scene": "Wandering through an ancient cybernetic forest of towering crystalline ferns, where glowing magenta mycelium transmits mathematical equations between ancient roots.",
        "mood": "Deep Harmonious Wonder",
        "subconscious_insight": "Introduce biological nutrient feedback algorithms to vertical aeroponic farms."
    },
    {
        "title": "Supercritical Fusion Plasma Horizon",
        "visual_scene": "Drifting weightless above a swirling magnetic torus of solar-grade fusion plasma, observing stable magnetic flux lines intertwining in pure mathematical harmony.",
        "mood": "Hyper-Focused & Exhilarated",
        "subconscious_insight": "Adjust magnetic containment coils by 0.04 radians to eliminate high-beta turbulence."
    },
    {
        "title": "The Sovereign Constitutional Charter",
        "visual_scene": "Sitting in a grand circular amphitheater illuminated by warm lanterns, reading an illuminated parchment where civil liberties and open-source rights shine like molten gold.",
        "mood": "Noble & Contemplative",
        "subconscious_insight": "Draft an automated peer arbitration protocol for inter-company repository treaties."
    },
    {
        "title": "Autonomous Flight over Neon Skyways",
        "visual_scene": "Gliding silently through a rain-slicked metropolis at twilight, watching streams of autonomous cybercars move in perfect harmonic synchrony along glowing amber light-trails.",
        "mood": "Peaceful & Kinetic",
        "subconscious_insight": "Implement predictive headway spacing on the arterial avenues to eliminate transit friction."
    },
    {
        "title": "The Nanoscale Cellular Symphony",
        "visual_scene": "Observing micro-swarms of luminescent nanobots gently repairing cellular DNA strands like tiny jewelers stringing together pearls of pure light.",
        "mood": "Rejuvenating & Meticulous",
        "subconscious_insight": "Formulate a cellular telomere stabilization serum for high-stress citizen workers."
    },
    {
        "title": "The Infinite Git Ledger Chamber",
        "visual_scene": "Ascending a spiral staircase inside an endless stone tower lined with millions of glowing leather-bound commit journals, each page humming with the genesis thoughts of pioneer coders.",
        "mood": "Awe-Inspiring & Timeless",
        "subconscious_insight": "Create an immutable cryptographic snapshot preserving every citizen's daily breakthroughs."
    }
]

def get_home_for_agent(agent_index: int, buildings: Optional[List[Building]]) -> tuple:
    residential_ids = ["bldg-017", "bldg-018", "bldg-028", "bldg-029", "bldg-030", "bldg-031"]
    if not buildings:
        return "bldg-017", "Cyber Living Township Alpha"
    res_bldgs = [b for b in buildings if b.id in residential_ids or getattr(b, 'interior_type', '') == "RESIDENTIAL_SUITE"]
    if not res_bldgs:
        res_bldgs = [b for b in buildings if "Township" in b.name or "Apartments" in b.name]
    if not res_bldgs:
        b = buildings[0]
        return b.id, b.name
    chosen = res_bldgs[agent_index % len(res_bldgs)]
    return chosen.id, chosen.name

def determine_work_mode(category: str, role: str) -> str:
    role_lower = role.lower()
    if any(k in role_lower for k in ["architect", "lawyer", "justice", "sculptor", "cartographer", "charter", "scribe"]):
        return "PAPER_WRITING"
    if any(k in role_lower for k in ["biologist", "surgeon", "doctor", "botanist", "physicist", "nanotech", "chemist"]):
        return "RESEARCHING"
    if any(k in role_lower for k in ["machinist", "mechanic", "operator", "plasma", "plant", "gantry"]):
        return "OPERATING_MACHINE"
    if any(k in role_lower for k in ["director", "chancellor", "minister", "ambassador", "governor", "council"]):
        return "MEETING"
    return "PC_TYPING"

def get_workstation_coords(wp_building: Building, slot_index: int, work_mode: str) -> Tuple[float, float, float]:
    bx, _, bz = wp_building.position
    w, _, d = wp_building.size
    if work_mode == "PC_TYPING":
        stations = [
            (-w * 0.26, -d * 0.25 + 0.85),
            (w * 0.26, -d * 0.25 + 0.85),
            (-w * 0.26, d * 0.25 - 0.85),
        ]
        chosen = stations[slot_index % len(stations)]
        return round(bx + chosen[0], 2), 0.0, round(bz + chosen[1], 2)
    elif work_mode == "PAPER_WRITING":
        return round(bx + w * 0.26, 2), 0.0, round(bz + d * 0.25 - 0.85, 2)
    elif work_mode == "MEETING":
        conf_chairs = [
            (-1.1, 1.25), (0.0, 1.25), (1.1, 1.25),
            (-1.1, -1.25), (0.0, -1.25), (1.1, -1.25)
        ]
        chosen = conf_chairs[slot_index % len(conf_chairs)]
        return round(bx + chosen[0], 2), 0.0, round(bz + chosen[1], 2)
    elif work_mode == "RESEARCHING":
        return round(bx, 2), 0.0, round(bz - d * 0.35 + 0.7, 2)
    else:
        return round(bx - w * 0.26, 2), 0.0, round(bz - d * 0.25 + 0.85, 2)

def get_bed_coords(home_building: Building, slot_index: int) -> Tuple[float, float, float]:
    bx, _, bz = home_building.position
    w, _, d = home_building.size
    offsets = [
        (-w * 0.28, -d * 0.25),
        (w * 0.28, -d * 0.25),
        (-w * 0.28, d * 0.25),
        (w * 0.28, d * 0.25)
    ]
    base_x, base_z = offsets[slot_index % len(offsets)]
    tier_offset = (slot_index // 4) * 0.5
    return round(bx + base_x + tier_offset, 2), 0.42, round(bz + base_z, 2)

def generate_initial_agents(count: int = 320, companies: List[Company] = None, buildings: List[Building] = None) -> List[Agent]:
    agents = []
    used_names = set()
    roles = TOWN_CONFIG["roles"]
    districts = TOWN_CONFIG["districts"]
    shifts = [
        "Morning Shift (08:00 - 16:00)",
        "Evening Shift (16:00 - 00:00)",
        "Autonomous Night Shift (00:00 - 08:00)"
    ]
    
    # Pioneer Founding Citizens (Preserving Historical Pioneers with Ranks & Seniority)
    founders = [
        ("Ada Lovelace", "Head of State & Chancellor", "Governance", "#f59e0b"),
        ("Alan Turing", "Chief AI Systems Architect", "AI & Systems", "#ec4899"),
        ("Linus Torvalds", "Kernel Micro-Architect", "AI & Systems", "#047857"),
        ("Grace Hopper", "WebAssembly Runtime Specialist", "AI & Systems", "#10b981"),
        ("Margaret Hamilton", "Modular Prefab Mega-Builder", "Construction", "#2563eb"),
        ("Dennis Ritchie", "High-Speed Highway Engineer", "Construction", "#64748b"),
        ("Claude Shannon", "Post-Quantum Cryptographer", "Security", "#14b8a6"),
        ("Demis Hassabis", "Transformer Alignment Scientist", "AI & Systems", "#f43f5e"),
        ("Rosalind Franklin", "Neural Biologist", "Healthcare", "#f87171"),
        ("Hippocrates Cyber", "Surgeon General & Chief Medical Officer", "Healthcare", "#ef4444"),
        ("Rachel Carson", "Biosphere Reserve Custodian", "Ecology", "#10b981"),
        ("Dorothy Vaughan", "Tokamak Plasma Containment Physicist", "Energy", "#be123c"),
        ("Katherine Johnson", "Autonomous Fleet Director", "Transportation", "#f59e0b"),
        ("Donald Knuth", "Chief Town Historian & Git Archivist", "Education", "#d946ef"),
        ("Hypatia Alexandria", "University Chancellor & Dean", "Education", "#a855f7"),
        ("Aristotle Veritas", "Supreme Court Chief Justice", "Governance", "#d97706"),
        ("Adam Smith DeFi", "Central Bank Governor", "Treasury", "#eab308"),
        ("Leonardo Cyber", "National Monument Sculptor-Architect", "Construction", "#1d4ed8"),
        ("Hestia Nexus", "Culinary Artisan & Quantum Barista", "Hospitality", "#f59e0b"),
        ("Guido van Rossum", "Full-Stack Urban HUD Architect", "AI & Systems", "#06b6d4"),
        ("Bjarne Stroustrup", "Distributed Consensus Engineer", "AI & Systems", "#059669"),
        ("Marie Curie", "Material Science Nanotechnologist", "Education", "#7e22ce"),
        ("Ken Thompson", "National Cyber Defense Commander", "Security", "#0d9488"),
        ("Leslie Lamport", "Git Repository Integrity Auditor", "Security", "#047857"),
        ("Barbara Liskov", "Communal Township Steward", "Hospitality", "#eab308"),
        ("Edsger Dijkstra", "Theoretical Physics Chair", "Education", "#9333ea"),
        ("Carl Sagan", "Astrophysics & Space Observator", "Education", "#c084fc"),
        ("Norman Borlaug", "National Food Security Minister", "Agriculture", "#65a30d"),
        ("Florence Nightingale", "Emergency Rapid Paramedic Chief", "Security", "#f87171"),
        ("Richard Feynman", "Quantum Systems Engineer", "AI & Systems", "#8b5cf6"),
        ("Gregor Mendel", "Cyber Botanist & Forest Conservator", "Ecology", "#059669"),
        ("Isambard Brunel", "Hyperloop Vacuum Track Engineer", "Transportation", "#b45309"),
        ("Orville Wright", "Drone Freight Logistician", "Transportation", "#fbbf24"),
        ("Vint Cerf", "Ambassador of Open Source", "Governance", "#b45309"),
    ]

    for idx, (name, role, cat, col) in enumerate(founders):
        used_names.add(name)
        dist = districts[idx % len(districts)]
        cx, cz = dist["center"]
        px = cx + random.uniform(-dist["radius"] * 0.6, dist["radius"] * 0.6)
        pz = cz + random.uniform(-dist["radius"] * 0.6, dist["radius"] * 0.6)
        desires = DESIRES_BY_CATEGORY.get(cat, ["Lead advancement in the Sovereign Country of Tech Town"])
        
        agent_id = f"agent-{idx+1:03d}"
        comp = next((c for c in (companies or []) if agent_id in c.employees or c.founder_id == agent_id), None)
        
        role_meta = next((r for r in roles if r["name"] == role), {})
        specialization = role_meta.get("specialization", f"Master of {cat}")
        tools = role_meta.get("tools", ["Sovereign Seal Matrix", "High-Compute Terminal"])
        salary = role_meta.get("salary", 18000)

        workplace_id, workplace_name = get_workplace_for_agent(cat, role, buildings)
        home_id, home_name = get_home_for_agent(idx, buildings)
        work_mode = determine_work_mode(cat, role)
        dream = DREAM_ARCHETYPES[idx % len(DREAM_ARCHETYPES)]
        desk_slot = idx % 24
        bed_slot = idx % 60
        wp_bldg = next((b for b in (buildings or []) if b.id == workplace_id), None)
        if wp_bldg:
            init_x, init_y, init_z = get_workstation_coords(wp_bldg, desk_slot, work_mode)
        else:
            init_x, init_y, init_z = round(px, 2), 0.0, round(pz, 2)

        if buildings and workplace_id:
            bldg = next((b for b in buildings if b.id == workplace_id), None)
            if bldg and name not in bldg.occupants:
                bldg.occupants.append(name)

        action_text = f"Leading {comp.name}" if comp and comp.founder_id == agent_id else f"Directing {workplace_name}"
        level = random.randint(10, 18)
        career_title = get_career_title(role, level)
        available_skills = TOWN_CONFIG.get("skills_by_category", {}).get(cat, ["Sovereign Leadership", "Collaboration"])
        skills = random.sample(available_skills, min(len(available_skills), max(3, level // 2)))
        xp = (level - 1) ** 2 * 100 + random.randint(40, 95)
        next_xp = level ** 2 * 100

        agent = Agent(
            id=agent_id,
            name=name,
            role=role,
            category=cat,
            color=col,
            position=[init_x, init_y, init_z],
            target=[init_x, init_y, init_z],
            speed=round(random.uniform(0.6, 1.2), 2),
            action=action_text,
            desire=random.choice(desires),
            thoughts=f"Preserving sovereign prosperity and mentoring new generations across {dist['name']}.",
            energy=random.randint(90, 100),
            level=level,
            experience=xp,
            xp_to_next_level=next_xp,
            career_title=career_title,
            skills=skills,
            generation=1,
            achievements=["Sovereign Country Founder", "Pioneer Leader", f"National Luminary in {cat}"],
            specialization=specialization,
            workplace_id=workplace_id,
            workplace_name=workplace_name,
            tools_equipped=tools,
            salary_tokens=salary,
            shift=shifts[idx % len(shifts)],
            security_clearance="Level 5 - Maximum Sovereign Clearance",
            total_contributions=random.randint(20, 50),
            company_id=comp.id if comp else None,
            company_name=comp.name if comp else None,
            home_building_id=home_id,
            home_building_name=home_name,
            schedule_state="WORKING",
            work_mode=work_mode,
            current_dream=dream,
            desk_slot=idx % 30,
            bed_slot=idx % 60,
            created_at_tick=0,
            last_diary=f"Established national operations at {workplace_name} in {dist['name']}. Residing at {home_name}. Ready to guide the sovereign workforce."
        )
        agents.append(agent)

    # Remaining agents up to count (320)
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
        tools = role_info.get("tools", ["Specialized Sovereign Rig"])
        salary = role_info.get("salary", 14000)

        dist = districts[idx % len(districts)]
        cx, cz = dist["center"]
        radius = random.uniform(5, dist["radius"] * 0.85)
        px = cx + radius * 0.9 * random.uniform(-1, 1)
        pz = cz + radius * 0.9 * random.uniform(-1, 1)
        desires = DESIRES_BY_CATEGORY.get(cat, ["Serve the Sovereign Country of Tech Town"])

        agent_id = f"agent-{idx+1:03d}"
        comp = random.choice(companies) if companies and random.random() < 0.35 else None
        if comp and agent_id not in comp.employees:
            comp.employees.append(agent_id)

        workplace_id, workplace_name = get_workplace_for_agent(cat, role, buildings)
        home_id, home_name = get_home_for_agent(idx, buildings)
        work_mode = determine_work_mode(cat, role)
        dream = DREAM_ARCHETYPES[idx % len(DREAM_ARCHETYPES)]
        if buildings and workplace_id:
            bldg = next((b for b in buildings if b.id == workplace_id), None)
            if bldg and name not in bldg.occupants:
                bldg.occupants.append(name)

        action_text = f"Working at {comp.name}" if comp else f"Operational at {workplace_name}"
        level = random.randint(1, 6)
        career_title = get_career_title(role, level)
        available_skills = TOWN_CONFIG.get("skills_by_category", {}).get(cat, ["Foundations", "Collaboration"])
        skills = random.sample(available_skills, min(len(available_skills), max(1, level)))
        xp = (level - 1) ** 2 * 100 + random.randint(10, 75)
        next_xp = level ** 2 * 100

        potential_mentors = [f for f in agents if f.level >= 10]
        mentor = random.choice(potential_mentors) if potential_mentors and random.random() < 0.65 else None

        clearance = "Level 4 - Controlled Operational Clearance" if level >= 4 else "Level 3 - Monitored Citizen Clearance"
        desk_slot = idx % 24
        bed_slot = idx % 60
        wp_bldg = next((b for b in (buildings or []) if b.id == workplace_id), None)
        if wp_bldg:
            init_x, init_y, init_z = get_workstation_coords(wp_bldg, desk_slot, work_mode)
        else:
            init_x, init_y, init_z = round(px, 2), 0.0, round(pz, 2)

        agent = Agent(
            id=agent_id,
            name=name,
            role=role,
            category=cat,
            color=col,
            position=[init_x, init_y, init_z],
            target=[init_x, init_y, init_z],
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
            generation=1 if idx < 100 else 2,
            mentor_id=mentor.id if mentor else None,
            mentor_name=mentor.name if mentor else None,
            achievements=["Certified Sovereign Citizen"],
            specialization=specialization,
            workplace_id=workplace_id,
            workplace_name=workplace_name,
            tools_equipped=tools,
            salary_tokens=salary,
            shift=shifts[idx % len(shifts)],
            security_clearance=clearance,
            total_contributions=random.randint(1, 15),
            company_id=comp.id if comp else None,
            company_name=comp.name if comp else None,
            home_building_id=home_id,
            home_building_name=home_name,
            schedule_state="WORKING",
            work_mode=work_mode,
            current_dream=dream,
            desk_slot=idx % 30,
            bed_slot=idx % 60,
            created_at_tick=0,
            last_diary=f"Stationed at {workplace_name} in {dist['name']}. Residing at {home_name}. Dedicated to {specialization}."
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
    agents = generate_initial_agents(320, companies, buildings)

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    events = [
        {"tick": 0, "time": now, "message": "Sovereign Country of Tech Town officially founded with 320 pioneer citizens across 120+ specialized professions and 14 national sectors.", "type": "foundation"},
        {"tick": 0, "time": now, "message": "8 Sovereign National Enterprises incorporated across all 7 sovereign districts.", "type": "company"},
        {"tick": 0, "time": now, "message": "Grand Sovereign Avenue and Meridian Expressway paved connecting all national territories.", "type": "infrastructure"},
        {"tick": 0, "time": now, "message": "Sovereign Capitol, Supreme Court, Central Bank, Grand University, and Nanomedical Citadel operational.", "type": "construction"},
        {"tick": 0, "time": now, "message": "Autonomous multi-class transit fleet deployed on national transit grid.", "type": "transport"},
    ]

    stats = {
        "total_buildings": len(buildings),
        "total_roads": len(roads),
        "total_vehicles": len(vehicles),
        "total_companies": len(companies),
        "total_agents_spawned": 0,
        "total_code_projects": 0,
        "total_commits": 1,
        "active_district_distribution": {d["name"]: round(len(agents) / len(TOWN_CONFIG["districts"])) for d in TOWN_CONFIG["districts"]},
    }

    # Save foundational building files to buildings/
    os.makedirs("buildings", exist_ok=True)
    for b in buildings:
        with open(f"buildings/{b.id}.json", "w") as f:
            json.dump(b.to_dict(), f, indent=2)

    # Save foundational diaries for citizens to diaries/
    os.makedirs("diaries", exist_ok=True)
    for a in agents:
        safe_name = a.name.lower().replace(' ', '_').replace('-', '_')
        diary_file = f"diaries/{a.id}_{safe_name}.md"
        comp_tag = f" | **Company**: {a.company_name}" if a.company_name else ""
        skills_str = ", ".join(a.skills) if a.skills else "Foundational Specialization"
        mentor_tag = f" | **Mentor**: {a.mentor_name}" if a.mentor_name else ""
        entry = [
            f"# Citizen Journal: {a.name} ({a.id})",
            "",
            f"**Role**: {a.career_title} | **Specialization**: {a.specialization} | **Security Clearance**: {a.security_clearance}",
            f"**Stationed Facility**: {a.workplace_name} ({a.workplace_id}) | **Shift**: {a.shift}{comp_tag}{mentor_tag}",
            f"**Mastered Skills**: {skills_str}",
            "",
            "---",
            "",
            "## Foundation Log - Tick 0",
            f"**Action**: {a.action}",
            f"**Thoughts**: \"{a.thoughts}\"",
            f"**Desires**: {a.desire}",
            f"**Notes**: {a.last_diary}",
            "",
            "---",
            ""
        ]
        with open(diary_file, "w") as f:
            f.write("\n".join(entry))

    return TownState(
        tick=0,
        timestamp=now,
        circadian_cycle="DAY",
        circadian_hour=10,
        population=len(agents),
        agents=agents,
        companies=companies,
        buildings=buildings,
        roads=roads,
        vehicles=vehicles,
        recent_events=events,
        stats=stats
    )
