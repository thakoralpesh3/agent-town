"""
Generator for initial population of 200 agents and foundational Tech Town layout.
"""
import random
import datetime
from typing import List, Dict, Tuple
from town.config import TOWN_CONFIG
from town.models import Agent, Building, Road, Vehicle, TownState

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
        "Design a monumental Holo Arch celebrating open source"
    ],
    "Engineering": [
        "Design hyper-efficient autonomous hovercars with LiDAR guidance",
        "Upgrade the quantum power sub-grid for zero-latency compute",
        "Establish a robotic assembly factory for autonomous town machinery",
        "Engineer smart bridges connecting high-density cyber zones"
    ],
    "Research": [
        "Train a decentralized neural net that coordinates city logistics",
        "Synthesize quantum compression algorithms for town archives",
        "Conduct benchmark studies on autonomous agent cooperation",
        "Model emergent agent behavior across the 5 town districts"
    ],
    "Software": [
        "Write a reactive microkernel and commit it to town repositories",
        "Deploy an event-driven pub/sub bus across all town buildings",
        "Develop full-stack HUD dashboards for city telemetry",
        "Create a distributed package manager for tech town tools"
    ],
    "Infrastructure": [
        "Automate continuous integration pipelines for city blueprints",
        "Fortify the town perimeter against data entropy and packet loss",
        "Monitor server rack thermals in the Industrial Sector",
        "Orchestrate zero-downtime rolling upgrades for all town systems"
    ],
    "Ecology": [
        "Cultivate bioluminescent flora in the Holo Parks",
        "Engineer carbon-negative synthetic trees that illuminate roads",
        "Harmonize tech architecture with digital natural preserves",
        "Monitor digital environmental metrics across all quadrants"
    ],
    "Society": [
        "Chronicle every milestone and building construction in GitHub diaries",
        "Organize hackathons and collaborative build sessions in Cyber Commons",
        "Curate the town library of algorithms and open knowledge",
        "Welcome and mentor freshly spawned child agents"
    ],
    "Energy": [
        "Calibrate magnetic containment on the Central Fusion Core",
        "Route clean renewable energy directly to residential blocks",
        "Install smart induction coils into main roads to charge moving cars",
        "Optimize battery storage banks for night-cycle power conservation"
    ],
    "Art": [
        "Sculpt interactive 3D light installations along the main avenues",
        "Compose cybernetic ambient soundscapes for community plazas",
        "Create dynamic neon murals on high-rise facades",
        "Design distinctive cosmetic chassis for newly minted vehicles"
    ],
    "Security": [
        "Perform cryptographic audits on git commits and smart contracts",
        "Guard the town repository against rogue exceptions",
        "Deploy intrusion detection honeypots around data hubs",
        "Verify hash integrity of all newly registered building blueprints"
    ]
}

def generate_foundational_roads() -> List[Road]:
    roads = [
        # Grand Arterials
        Road(id="road-001", name="Grand Cyber Boulevard", start=[-180.0, 0.0], end=[180.0, 0.0], width=8.0, road_type="Highway", builder_name="Founding Architects"),
        Road(id="road-002", name="Quantum Expressway", start=[0.0, -180.0], end=[0.0, 180.0], width=8.0, road_type="Highway", builder_name="Founding Architects"),
        
        # Quadrant Connectors
        Road(id="road-003", name="Silicon Central Ring", start=[-50.0, -50.0], end=[50.0, -50.0], width=6.0, road_type="Avenue", builder_name="Urban Planning Guild"),
        Road(id="road-004", name="Silicon Central Ring East", start=[50.0, -50.0], end=[50.0, 50.0], width=6.0, road_type="Avenue", builder_name="Urban Planning Guild"),
        Road(id="road-005", name="Silicon Central Ring North", start=[50.0, 50.0], end=[-50.0, 50.0], width=6.0, road_type="Avenue", builder_name="Urban Planning Guild"),
        Road(id="road-006", name="Silicon Central Ring West", start=[-50.0, 50.0], end=[-50.0, -50.0], width=6.0, road_type="Avenue", builder_name="Urban Planning Guild"),
        
        # District Arterials
        Road(id="road-007", name="Innovation Matrix Spur", start=[50.0, 50.0], end=[120.0, 120.0], width=6.0, road_type="Avenue", builder_name="Neural Logistics"),
        Road(id="road-008", name="Residential Pods Loop", start=[-50.0, 50.0], end=[-120.0, 100.0], width=6.0, road_type="Avenue", builder_name="Civic Works"),
        Road(id="road-009", name="Cyber Commons Promenade", start=[-50.0, -50.0], end=[-100.0, -110.0], width=6.0, road_type="Avenue", builder_name="Civic Works"),
        Road(id="road-010", name="Industrial Heavy Concourse", start=[50.0, -50.0], end=[110.0, -110.0], width=7.0, road_type="Highway", builder_name="Forge Guild"),
    ]
    return roads

def generate_foundational_buildings() -> List[Building]:
    buildings = [
        # Silicon Central
        Building(id="bldg-001", name="Tower of Turing (City Mainframe)", type="Tech Tower", position=[0.0, 28.0, 0.0], size=[22.0, 56.0, 22.0], color="#00f0ff", builder_id="agent-001", builder_name="Ada Lovelace", district="Silicon Central", purpose="Mainframe Core & Coordination"),
        Building(id="bldg-002", name="Shannon Information Spire", type="Tech Tower", position=[28.0, 22.0, 25.0], size=[16.0, 44.0, 16.0], color="#0284c7", builder_id="agent-002", builder_name="Alan Turing", district="Silicon Central", purpose="High-Throughput Packet Routing"),
        Building(id="bldg-003", name="Von Neumann Citadel", type="Tech Tower", position=[-28.0, 24.0, -25.0], size=[18.0, 48.0, 18.0], color="#38bdf8", builder_id="agent-003", builder_name="Grace Hopper", district="Silicon Central", purpose="Parallel Instruction Scheduling"),
        
        # Innovation Matrix
        Building(id="bldg-004", name="Deep Neural Research Lab", type="AI Research Lab", position=[105.0, 14.0, 95.0], size=[24.0, 28.0, 24.0], color="#a855f7", builder_id="agent-004", builder_name="Geoffrey Hinton", district="Innovation Matrix", purpose="Transformer Model Experimentation"),
        Building(id="bldg-005", name="Quantum Logic Foundry", type="AI Research Lab", position=[85.0, 12.0, 120.0], size=[20.0, 24.0, 20.0], color="#c084fc", builder_id="agent-005", builder_name="Richard Feynman", district="Innovation Matrix", purpose="Superposition Circuit Design"),
        Building(id="bldg-006", name="Autonomous Robotics Institute", type="AI Research Lab", position=[125.0, 11.0, 75.0], size=[22.0, 22.0, 22.0], color="#9333ea", builder_id="agent-006", builder_name="Demis Hassabis", district="Innovation Matrix", purpose="Reinforcement Learning for Agents"),

        # Residential Quarter
        Building(id="bldg-007", name="Cyber Living Pod Alpha", type="Residential Pod", position=[-95.0, 9.0, 75.0], size=[16.0, 18.0, 16.0], color="#22c55e", builder_id="agent-007", builder_name="Margaret Hamilton", district="Residential Quarter", purpose="Residential Quarters for 50 Agents"),
        Building(id="bldg-008", name="Cyber Living Pod Beta", type="Residential Pod", position=[-120.0, 9.0, 95.0], size=[16.0, 18.0, 16.0], color="#16a34a", builder_id="agent-008", builder_name="Barbara Liskov", district="Residential Quarter", purpose="Residential Quarters for 50 Agents"),
        Building(id="bldg-009", name="Skyward Habitation Cube", type="Residential Pod", position=[-80.0, 12.0, 110.0], size=[18.0, 24.0, 18.0], color="#4ade80", builder_id="agent-009", builder_name="Radia Perlman", district="Residential Quarter", purpose="Residential High-Rise Pods"),

        # Cyber Commons
        Building(id="bldg-010", name="The Bit & Byte Cyber Cafe", type="Cyber Cafe", position=[-75.0, 6.0, -80.0], size=[16.0, 12.0, 16.0], color="#eab308", builder_id="agent-010", builder_name="Linus Torvalds", district="Cyber Commons", purpose="Agent Socialization & Brainstorming"),
        Building(id="bldg-011", name="Holo Oasis Digital Park", type="Holo Park", position=[-95.0, 2.0, -100.0], size=[30.0, 4.0, 30.0], color="#10b981", builder_id="agent-011", builder_name="Dennis Ritchie", district="Cyber Commons", purpose="Synthetic Nature & Relaxation"),
        Building(id="bldg-012", name="Open Source Agora (Town Hall)", type="Tech Tower", position=[-60.0, 15.0, -60.0], size=[20.0, 30.0, 20.0], color="#facc15", builder_id="agent-012", builder_name="Ken Thompson", district="Cyber Commons", purpose="Civic Gatherings & Governance"),

        # Industrial Sector
        Building(id="bldg-013", name="Autonomous Cybercar Assembly Plant", type="Vehicle Factory", position=[85.0, 10.0, -85.0], size=[26.0, 20.0, 26.0], color="#f59e0b", builder_id="agent-013", builder_name="Katherine Johnson", district="Industrial Sector", purpose="Robotic Fabrication of City Vehicles"),
        Building(id="bldg-014", name="Tokamak Fusion Core Array", type="Solar Fusion Array", position=[110.0, 6.0, -105.0], size=[22.0, 12.0, 22.0], color="#f97316", builder_id="agent-014", builder_name="Dorothy Vaughan", district="Industrial Sector", purpose="Clean Energy Grid Generation"),
        Building(id="bldg-015", name="Petabyte Quantum Server Farm", type="Quantum Data Center", position=[70.0, 12.0, -115.0], size=[24.0, 24.0, 24.0], color="#6366f1", builder_id="agent-015", builder_name="Leslie Lamport", district="Industrial Sector", purpose="Persistent State & Log Storage"),
    ]
    return buildings

def generate_foundational_vehicles() -> List[Vehicle]:
    vehicles = [
        Vehicle(id="veh-001", name="Cybercar Alpha-1", type="Autonomous Cybercar", position=[-150.0, 1.0, 0.0], target=[150.0, 1.0, 0.0], speed=1.5, color="#00f0ff", driver_name="Autonomous Transit AI"),
        Vehicle(id="veh-002", name="Cybercar Alpha-2", type="Autonomous Cybercar", position=[120.0, 1.0, 0.0], target=[-150.0, 1.0, 0.0], speed=1.4, color="#00f0ff", driver_name="Autonomous Transit AI"),
        Vehicle(id="veh-003", name="Quantum Shuttle 01", type="Hover Shuttle", position=[0.0, 2.5, -140.0], target=[0.0, 2.5, 140.0], speed=2.0, color="#a855f7", driver_name="Hover Pilot AI"),
        Vehicle(id="veh-004", name="Quantum Shuttle 02", type="Hover Shuttle", position=[0.0, 2.5, 110.0], target=[0.0, 2.5, -140.0], speed=1.9, color="#c084fc", driver_name="Hover Pilot AI"),
        Vehicle(id="veh-005", name="Material Drone Hauler 1", type="Cargo Drone Carrier", position=[45.0, 1.2, -45.0], target=[85.0, 1.2, -85.0], speed=1.1, color="#f59e0b", driver_name="Industrial Logistics"),
        Vehicle(id="veh-006", name="Eco Surveyor Pod", type="Surveyor Pod", position=[-45.0, 1.0, -45.0], target=[-95.0, 1.0, -100.0], speed=1.3, color="#10b981", driver_name="Environmental AI"),
        Vehicle(id="veh-007", name="Urban Cruiser Beta", type="Autonomous Cybercar", position=[45.0, 1.0, 45.0], target=[105.0, 1.0, 95.0], speed=1.6, color="#38bdf8", driver_name="Research Transit"),
        Vehicle(id="veh-008", name="Residential Commuter Express", type="Hover Shuttle", position=[-45.0, 2.0, 45.0], target=[-95.0, 2.0, 75.0], speed=1.7, color="#4ade80", driver_name="Civic Transit"),
    ]
    return vehicles

def generate_initial_agents(count: int = 200) -> List[Agent]:
    agents = []
    used_names = set()
    roles = TOWN_CONFIG["roles"]
    districts = TOWN_CONFIG["districts"]
    
    # Priority famous founders first
    founders = [
        ("Ada Lovelace", "Urban Architect", "Construction", "#3b82f6"),
        ("Alan Turing", "AI & Neural Researcher", "Research", "#ec4899"),
        ("Grace Hopper", "Full-Stack Web Architect", "Software", "#10b981"),
        ("Linus Torvalds", "DevOps & Cloud Sentinel", "Infrastructure", "#06b6d4"),
        ("Margaret Hamilton", "Quantum Systems Engineer", "Engineering", "#8b5cf6"),
        ("Dennis Ritchie", "Road & Infrastructure Engineer", "Construction", "#64748b"),
        ("Claude Shannon", "Security & Cryptographer", "Security", "#14b8a6"),
        ("Demis Hassabis", "AI & Neural Researcher", "Research", "#ec4899"),
        ("Geoffrey Hinton", "AI & Neural Researcher", "Research", "#ec4899"),
        ("Barbara Liskov", "Full-Stack Web Architect", "Software", "#10b981"),
        ("Katherine Johnson", "Autonomous Vehicle Designer", "Engineering", "#f59e0b"),
        ("Radia Perlman", "Road & Infrastructure Engineer", "Construction", "#64748b"),
        ("Ken Thompson", "DevOps & Cloud Sentinel", "Infrastructure", "#06b6d4"),
        ("Donald Knuth", "Town Chronicler & Historian", "Society", "#d946ef"),
        ("Leslie Lamport", "Quantum Systems Engineer", "Engineering", "#8b5cf6"),
        ("Dorothy Vaughan", "Energy & Fusion Specialist", "Energy", "#e11d48"),
        ("Andrej Karpathy", "Autonomous Vehicle Designer", "Engineering", "#f59e0b"),
        ("Ilya Sutskever", "AI & Neural Researcher", "Research", "#ec4899"),
        ("Guido van Rossum", "Full-Stack Web Architect", "Software", "#10b981"),
        ("Bjarne Stroustrup", "Systems Engineer", "Software", "#3b82f6"),
    ]

    for idx, (name, role, cat, col) in enumerate(founders):
        used_names.add(name)
        dist = districts[idx % len(districts)]
        cx, cz = dist["center"]
        px = cx + random.uniform(-dist["radius"] * 0.7, dist["radius"] * 0.7)
        pz = cz + random.uniform(-dist["radius"] * 0.7, dist["radius"] * 0.7)
        desires = DESIRES_BY_CATEGORY.get(cat, ["Help expand the GitHub Tech Town"])
        
        agent = Agent(
            id=f"agent-{idx+1:03d}",
            name=name,
            role=role,
            category=cat,
            color=col,
            position=[round(px, 2), 0.8, round(pz, 2)],
            target=[round(px + random.uniform(-15, 15), 2), 0.8, round(pz + random.uniform(-15, 15), 2)],
            speed=round(random.uniform(0.6, 1.2), 2),
            action=f"Active in {dist['name']}",
            desire=random.choice(desires),
            thoughts=f"Evaluating potential enhancements for {dist['name']}.",
            energy=random.randint(85, 100),
            level=random.randint(5, 10),
            created_at_tick=0,
            last_diary=f"Founded my workshop in {dist['name']}. Ready to construct future tech."
        )
        agents.append(agent)

    # Generate remaining up to count (total 200)
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

        dist = districts[idx % len(districts)]
        cx, cz = dist["center"]
        angle = random.uniform(0, 6.28)
        radius = random.uniform(5, dist["radius"] * 0.9)
        px = cx + radius * 0.9 * random.uniform(-1, 1)
        pz = cz + radius * 0.9 * random.uniform(-1, 1)
        desires = DESIRES_BY_CATEGORY.get(cat, ["Innovate within GitHub Tech Town"])

        agent = Agent(
            id=f"agent-{idx+1:03d}",
            name=name,
            role=role,
            category=cat,
            color=col,
            position=[round(px, 2), 0.8, round(pz, 2)],
            target=[round(px + random.uniform(-20, 20), 2), 0.8, round(pz + random.uniform(-20, 20), 2)],
            speed=round(random.uniform(0.5, 1.1), 2),
            action=f"Surveying {dist['name']}",
            desire=random.choice(desires),
            thoughts=f"Looking for creative opportunities and teammates in {dist['name']}.",
            energy=random.randint(75, 100),
            level=random.randint(1, 4),
            created_at_tick=0,
            last_diary=f"Arrived in {dist['name']} sector of GitHub Tech Town."
        )
        agents.append(agent)

    return agents

def generate_initial_state() -> TownState:
    roads = generate_foundational_roads()
    buildings = generate_foundational_buildings()
    vehicles = generate_foundational_vehicles()
    agents = generate_initial_agents(200)

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    events = [
        {"tick": 0, "time": now, "message": "GitHub Tech Town officially founded with 200 pioneer agents.", "type": "foundation"},
        {"tick": 0, "time": now, "message": "Grand Cyber Boulevard and Quantum Expressway paved.", "type": "infrastructure"},
        {"tick": 0, "time": now, "message": "Tower of Turing (City Mainframe) activated in Silicon Central.", "type": "construction"},
        {"tick": 0, "time": now, "message": "Autonomous vehicle fleet deployed on city transit grid.", "type": "transport"},
    ]

    stats = {
        "total_buildings": len(buildings),
        "total_roads": len(roads),
        "total_vehicles": len(vehicles),
        "total_agents_spawned": 0,
        "total_code_projects": 0,
        "total_commits": 1,
        "active_district_distribution": {d["name"]: 40 for d in TOWN_CONFIG["districts"]},
    }

    return TownState(
        tick=0,
        timestamp=now,
        population=len(agents),
        agents=agents,
        buildings=buildings,
        roads=roads,
        vehicles=vehicles,
        recent_events=events,
        stats=stats
    )
