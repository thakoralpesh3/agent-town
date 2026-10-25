"""
Town Simulation Engine - Autonomous life cycle, growth, construction, and agent creativity.
"""
import os
import json
import random
import datetime
import math
from typing import List, Dict, Any, Tuple, Optional
from town.config import TOWN_CONFIG
from town.models import Agent, Building, Road, Vehicle, TownState

CODE_TEMPLATES = [
    ("traffic_mesh.py", "Autonomous vehicle grid coordinator with collision avoidance algorithms"),
    ("neural_router.py", "Dynamic low-latency packet routing across all town tech towers"),
    ("solar_optimizer.py", "Fusion and solar array energy distributor balancing residential load"),
    ("agent_orchestrator.py", "Distributed consensus protocol for autonomous building permits"),
    ("quantum_hasher.py", "Zero-knowledge cryptographic audit system for git commits"),
    ("holo_matrix_renderer.py", "3D volumetric holographic projection shader for town squares"),
    ("urban_botanist.py", "Bio-luminescent flora photosynthesis cycle controller"),
    ("decentralized_storage.py", "Content-addressable state store for agent journals and blueprints"),
]

class TownEngine:
    def __init__(self, state_file: str = "state/town_state.json", docs_data_file: str = "docs/data/town_state.json"):
        self.state_file = state_file
        self.docs_data_file = docs_data_file
        self.state: Optional[TownState] = None

    def load_state(self) -> TownState:
        if os.path.exists(self.state_file):
            with open(self.state_file, "r") as f:
                data = json.load(f)
            self.state = TownState.from_dict(data)
        else:
            from town.generator import generate_initial_state
            self.state = generate_initial_state()
            self.save_state()
        return self.state

    def save_state(self):
        if not self.state:
            return
        os.makedirs(os.path.dirname(self.state_file), exist_ok=True)
        os.makedirs(os.path.dirname(self.docs_data_file), exist_ok=True)
        
        data = self.state.to_dict()
        with open(self.state_file, "w") as f:
            json.dump(data, f, indent=2)
        with open(self.docs_data_file, "w") as f:
            json.dump(data, f, indent=2)

    def log_event(self, message: str, event_type: str = "activity"):
        if not self.state:
            return
        now = datetime.datetime.now(datetime.timezone.utc).isoformat()
        self.state.recent_events.append({
            "tick": self.state.tick,
            "time": now,
            "message": message,
            "type": event_type
        })
        if len(self.state.recent_events) > 100:
            self.state.recent_events = self.state.recent_events[-100:]

    def _find_open_plot(self, district_name: str) -> Tuple[float, float]:
        dist = next((d for d in TOWN_CONFIG["districts"] if d["name"] == district_name), TOWN_CONFIG["districts"][0])
        cx, cz = dist["center"]
        rad = dist["radius"]
        
        for _ in range(40):
            angle = random.uniform(0, 2 * math.pi)
            dist_from_center = random.uniform(15, rad * 1.1)
            x = round(cx + dist_from_center * math.cos(angle), 1)
            z = round(cz + dist_from_center * math.sin(angle), 1)
            
            collision = False
            for b in self.state.buildings:
                bx, _, bz = b.position
                if math.hypot(x - bx, z - bz) < 18.0:
                    collision = True
                    break
            if not collision:
                return x, z
        return round(cx + random.uniform(-rad, rad), 1), round(cz + random.uniform(-rad, rad), 1)

    def _agent_build_structure(self, agent: Agent):
        bldg_types = TOWN_CONFIG["building_types"]
        b_type = random.choice(bldg_types)
        x, z = self._find_open_plot(b_type["district"])
        height = b_type["base_size"][1] * random.uniform(0.8, 1.4)
        width = b_type["base_size"][0] * random.uniform(0.9, 1.2)
        depth = b_type["base_size"][2] * random.uniform(0.9, 1.2)
        
        bldg_id = f"bldg-{len(self.state.buildings) + 1:03d}"
        bldg_name = f"{agent.name.split()[0]}'s {b_type['type']} #{random.randint(10, 99)}"
        
        new_bldg = Building(
            id=bldg_id,
            name=bldg_name,
            type=b_type["type"],
            position=[x, round(height / 2.0, 1), z],
            size=[round(width, 1), round(height, 1), round(depth, 1)],
            color=b_type["color"],
            builder_id=agent.id,
            builder_name=agent.name,
            district=b_type["district"],
            purpose=f"Constructed by {agent.name} for {b_type['type']} operations",
            completion=1.0
        )
        self.state.buildings.append(new_bldg)
        agent.creations.append({"type": "building", "id": bldg_id, "name": bldg_name})
        agent.level += 1
        agent.action = f"Finished constructing {bldg_name}"
        agent.thoughts = f"Just completed {bldg_name} in {b_type['district']}. The skyline is expanding!"
        
        os.makedirs("buildings", exist_ok=True)
        with open(f"buildings/{bldg_id}.json", "w") as f:
            json.dump(new_bldg.to_dict(), f, indent=2)
            
        self.log_event(f"{agent.name} constructed {bldg_name} ({b_type['type']}) in {b_type['district']}!", "construction")
        self.state.stats["total_buildings"] = len(self.state.buildings)

    def _agent_build_road(self, agent: Agent):
        road_id = f"road-{len(self.state.roads) + 1:03d}"
        angle = random.uniform(0, 2 * math.pi)
        length = random.uniform(40, 70)
        start_x = round(agent.position[0], 1)
        start_z = round(agent.position[2], 1)
        end_x = round(start_x + length * math.cos(angle), 1)
        end_z = round(start_z + length * math.sin(angle), 1)
        
        road_name = f"{agent.name.split()[0]} Concourse #{len(self.state.roads) + 1}"
        new_road = Road(
            id=road_id,
            name=road_name,
            start=[start_x, start_z],
            end=[end_x, end_z],
            width=6.0,
            builder_name=agent.name,
            road_type="Avenue"
        )
        self.state.roads.append(new_road)
        agent.creations.append({"type": "road", "id": road_id, "name": road_name})
        agent.level += 1
        agent.action = f"Paved {road_name}"
        agent.thoughts = f"Connected transit grid across [{start_x}, {start_z}] -> [{end_x}, {end_z}]."
        
        self.log_event(f"{agent.name} laid new thoroughfare: {road_name}!", "infrastructure")
        self.state.stats["total_roads"] = len(self.state.roads)

    def _agent_craft_vehicle(self, agent: Agent):
        veh_types = TOWN_CONFIG["vehicle_types"]
        v_info = random.choice(veh_types)
        veh_id = f"veh-{len(self.state.vehicles) + 1:03d}"
        veh_name = f"{v_info['type']} #{random.randint(100, 999)}"
        
        px, _, pz = agent.position
        target_road = random.choice(self.state.roads) if self.state.roads else None
        target_pos = [target_road.end[0], 1.0, target_road.end[1]] if target_road else [px + 50, 1.0, pz + 50]
        
        new_veh = Vehicle(
            id=veh_id,
            name=veh_name,
            type=v_info["type"],
            position=[px, 1.0, pz],
            target=target_pos,
            speed=v_info["speed"],
            color=v_info["color"],
            driver_id=agent.id,
            driver_name=agent.name,
            builder_name=agent.name
        )
        self.state.vehicles.append(new_veh)
        agent.creations.append({"type": "vehicle", "id": veh_id, "name": veh_name})
        agent.action = f"Cruising in newly built {veh_name}"
        agent.thoughts = f"The autonomous engine harmonics on {veh_name} are pristine."
        
        self.log_event(f"{agent.name} designed and manufactured {veh_name}!", "transport")
        self.state.stats["total_vehicles"] = len(self.state.vehicles)

    def _agent_spawn_child(self, agent: Agent):
        if len(self.state.agents) >= TOWN_CONFIG["spawn_limits"]["max_agents"]:
            return
            
        child_id = f"agent-{len(self.state.agents) + 1:03d}"
        from town.generator import FIRST_NAMES, LAST_NAMES, DESIRES_BY_CATEGORY
        first = random.choice(FIRST_NAMES)
        last = agent.name.split()[-1] if len(agent.name.split()) > 1 else random.choice(LAST_NAMES)
        child_name = f"{first} {last}"
        
        role_info = random.choice(TOWN_CONFIG["roles"])
        role = role_info["name"]
        cat = role_info["category"]
        col = role_info["color"]
        
        px, _, pz = agent.position
        child = Agent(
            id=child_id,
            name=child_name,
            role=role,
            category=cat,
            color=col,
            position=[round(px + random.uniform(-5, 5), 2), 0.8, round(pz + random.uniform(-5, 5), 2)],
            target=[round(px + random.uniform(-25, 25), 2), 0.8, round(pz + random.uniform(-25, 25), 2)],
            speed=round(random.uniform(0.6, 1.2), 2),
            action=f"Mentored by {agent.name}",
            desire=random.choice(DESIRES_BY_CATEGORY.get(cat, ["Help expand Tech Town"])),
            thoughts=f"Spawned into GitHub Tech Town by mentor {agent.name}! Eager to build.",
            energy=100,
            level=1,
            collaborators=[agent.name],
            created_at_tick=self.state.tick,
            last_diary=f"Brought online in tick {self.state.tick} by {agent.name}."
        )
        self.state.agents.append(child)
        agent.collaborators.append(child.name)
        agent.action = f"Spawned new agent: {child_name}"
        agent.thoughts = f"Proud to have brought {child_name} online to help expand our town!"
        
        self.log_event(f"{agent.name} spawned a new autonomous agent: {child_name} ({role})!", "population")
        self.state.stats["total_agents_spawned"] = self.state.stats.get("total_agents_spawned", 0) + 1

    def _agent_write_code(self, agent: Agent):
        filename, desc = random.choice(CODE_TEMPLATES)
        os.makedirs("projects", exist_ok=True)
        filepath = f"projects/{filename}"
        class_name = filename.split('.')[0].replace('_', ' ').title().replace(' ', '')
        
        code_lines = [
            f"# Auto-generated by GitHub Tech Town Agent: {agent.name}",
            f"# Role: {agent.role} (Level {agent.level})",
            f"# Purpose: {desc}",
            f"# Tick: {self.state.tick}",
            "",
            "import time",
            "import math",
            "",
            f"class {class_name}:",
            f"    def __init__(self, node_id=\"{agent.id}\"):",
            "        self.node_id = node_id",
            f"        self.author = \"{agent.name}\"",
            "        self.status = \"ACTIVE\"",
            "        self.metrics = {}",
            "",
            "    def process_cycle(self, payload: dict) -> dict:",
            "        \"\"\"Executes autonomous logic cycle.\"\"\"",
            "        latency_ms = round(math.sin(time.time()) * 5 + 12, 3)",
            "        return {",
            "            \"status\": \"SUCCESS\",",
            "            \"author\": self.author,",
            "            \"latency_ms\": latency_ms,",
            "            \"processed_by\": self.node_id",
            "        }",
            "",
            "if __name__ == \"__main__\":",
            f"    module = {class_name}()",
            f"    print(f\"{filename} initialized by {agent.name}\")",
            ""
        ]
        
        with open(filepath, "w") as f:
            f.write("\n".join(code_lines))
            
        agent.creations.append({"type": "code", "file": filepath, "name": filename})
        agent.action = f"Committed code {filename}"
        agent.thoughts = f"Refactored {filename} for distributed town infrastructure."
        
        self.log_event(f"{agent.name} pushed code to repository: projects/{filename}!", "software")
        self.state.stats["total_code_projects"] = len(os.listdir("projects")) if os.path.exists("projects") else 1

    def _agent_write_diary(self, agent: Agent):
        os.makedirs("diaries", exist_ok=True)
        safe_name = agent.name.lower().replace(' ', '_').replace('-', '_')
        filename = f"diaries/{agent.id}_{safe_name}.md"
        entry = [
            f"## Log Entry - Tick {self.state.tick}",
            "",
            f"**Location**: [{agent.position[0]}, {agent.position[2]}] | **Energy**: {agent.energy}% | **Level**: {agent.level}",
            "",
            f"**Current Action**: {agent.action}",
            "",
            f"**Thought**: \"{agent.thoughts}\"",
            "",
            f"**Desire**: {agent.desire}",
            "",
            "---",
            ""
        ]
        
        with open(filename, "a") as f:
            f.write("\n".join(entry))
        agent.last_diary = f"Tick {self.state.tick}: {agent.thoughts[:60]}..."

    def tick(self) -> TownState:
        if not self.state:
            self.load_state()

        self.state.tick += 1
        self.state.timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
        limits = TOWN_CONFIG["spawn_limits"]

        # 1. Update Vehicles
        for veh in self.state.vehicles:
            vx, vy, vz = veh.position
            tx, ty, tz = veh.target
            dx = tx - vx
            dz = tz - vz
            dist = math.hypot(dx, dz)
            if dist < 3.0:
                if self.state.roads:
                    chosen_road = random.choice(self.state.roads)
                    target_point = chosen_road.end if random.random() > 0.5 else chosen_road.start
                    veh.target = [target_point[0], 1.0, target_point[1]]
            else:
                step = min(veh.speed * 2.0, dist)
                veh.position[0] = round(vx + (dx / dist) * step, 2)
                veh.position[2] = round(vz + (dz / dist) * step, 2)

        # 2. Update Agents
        for agent in self.state.agents:
            ax, ay, az = agent.position
            tx, ty, tz = agent.target
            dx = tx - ax
            dz = tz - az
            dist = math.hypot(dx, dz)
            
            if dist < 2.0:
                dist_info = random.choice(TOWN_CONFIG["districts"])
                cx, cz = dist_info["center"]
                r = dist_info["radius"]
                agent.target = [
                    round(cx + random.uniform(-r, r), 2),
                    0.8,
                    round(cz + random.uniform(-r, r), 2)
                ]
            else:
                step = min(agent.speed * 1.5, dist)
                agent.position[0] = round(ax + (dx / dist) * step, 2)
                agent.position[2] = round(az + (dz / dist) * step, 2)

            agent.energy = min(100, max(20, agent.energy + random.randint(-5, 7)))

        # 3. Autonomous Creative Actions
        active_agents = random.sample(self.state.agents, min(30, len(self.state.agents)))
        for agent in active_agents:
            roll = random.random()
            if roll < limits["agent_reproduction_probability"]:
                self._agent_spawn_child(agent)
            elif roll < limits["agent_reproduction_probability"] + limits["building_construction_probability"]:
                self._agent_build_structure(agent)
            elif roll < limits["agent_reproduction_probability"] + limits["building_construction_probability"] + limits["road_construction_probability"]:
                self._agent_build_road(agent)
            elif roll < 0.65:
                self._agent_craft_vehicle(agent)
            elif roll < 0.85:
                self._agent_write_code(agent)
            else:
                self._agent_write_diary(agent)

        self.save_state()
        return self.state
