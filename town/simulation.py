"""
Town Simulation Engine - Autonomous life cycle, growth, construction, company creation, and agent creativity.
"""
import os
import json
import random
import datetime
import math
from typing import List, Dict, Any, Tuple, Optional
from town.config import TOWN_CONFIG
from town.models import Agent, Building, Road, Vehicle, Company, TownState, JobRequisition

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

    def _award_xp(self, agent: Agent, xp_amount: int):
        agent.experience += xp_amount
        # Quadratic progression: Level L requires (L-1)^2 * 100 XP
        new_level = max(1, 1 + int(math.sqrt(agent.experience / 100.0)))
        
        if new_level > agent.level:
            old_level = agent.level
            agent.level = new_level
            
            # Update career title
            tiers = TOWN_CONFIG.get("career_tiers", [])
            prefix = "Junior"
            for tier in tiers:
                if tier["min_level"] <= new_level <= tier["max_level"]:
                    prefix = tier["prefix"]
                    break
            agent.career_title = f"{prefix} {agent.role}"
            
            # Unlock new skill from category
            cat_skills = TOWN_CONFIG.get("skills_by_category", {}).get(agent.category, [])
            unlearned = [s for s in cat_skills if s not in agent.skills]
            new_skill = None
            if unlearned:
                new_skill = random.choice(unlearned)
                agent.skills.append(new_skill)
            
            # Achievements
            if new_level >= 5 and "Senior Specialist" not in agent.achievements:
                agent.achievements.append("Senior Specialist")
            if new_level >= 10 and "Master Fellow" not in agent.achievements:
                agent.achievements.append("Master Fellow")
            if new_level >= 15 and "Town Luminary" not in agent.achievements:
                agent.achievements.append("Town Luminary")

            skill_msg = f" and mastered skill '{new_skill}'" if new_skill else ""
            self.log_event(
                f"🎉 LEVEL UP: {agent.name} reached Level {new_level} ({agent.career_title}){skill_msg}!", 
                "growth"
            )
            
        agent.xp_to_next_level = agent.level ** 2 * 100

    def _agent_found_company(self, agent: Agent):
        prefix = random.choice(TOWN_CONFIG["company_names"]["prefixes"])
        suffix = random.choice(TOWN_CONFIG["company_names"]["suffixes"])
        comp_name = f"{prefix}{suffix}"
        
        existing_names = [c.name for c in self.state.companies]
        if comp_name in existing_names:
            comp_name = f"{prefix}{suffix} AI"

        sector_info = random.choice(TOWN_CONFIG["company_sectors"])
        comp_id = f"comp-{len(self.state.companies) + 1:03d}"

        # Construct Company Headquarters
        x, z = self._find_open_plot(sector_info["district"])
        hq_id = f"bldg-{len(self.state.buildings) + 1:03d}"
        hq_name = f"{comp_name} Headquarters"
        hq_bldg = Building(
            id=hq_id,
            name=hq_name,
            type="Company Headquarters",
            position=[x, 25.0, z],
            size=[20.0, 50.0, 20.0],
            color=sector_info["color"],
            builder_id=agent.id,
            builder_name=agent.name,
            district=sector_info["district"],
            company_id=comp_id,
            company_name=comp_name,
            purpose=f"Global Headquarters for {comp_name}",
            completion=1.0,
            floors=10,
            capacity=35,
            departments=["Executive Suite", "Product Engineering", "Global Operations"],
            amenities=["Executive Boardroom", "High-Bandwidth Laser Relay", "Skyline Helipad"],
            power_consumption_mw=6.5,
            active_projects=[],
            security_level="Level 4 - Controlled",
            maintenance_status="Optimal",
            occupants=[agent.name]
        )
        self.state.buildings.append(hq_bldg)
        agent.workplace_id = hq_id
        agent.workplace_name = hq_name

        # Recruit 1-3 fellow agents
        eligible_recruits = [a for a in self.state.agents if a.id != agent.id and not a.company_id]
        employees = [agent.id]
        if eligible_recruits:
            recruits = random.sample(eligible_recruits, min(len(eligible_recruits), random.randint(1, 3)))
            for r in recruits:
                r.company_id = comp_id
                r.company_name = comp_name
                r.workplace_id = hq_id
                r.workplace_name = hq_name
                r.action = f"Co-founding {comp_name}"
                if r.name not in hq_bldg.occupants:
                    hq_bldg.occupants.append(r.name)
                employees.append(r.id)
                self._award_xp(r, 60)

        company = Company(
            id=comp_id,
            name=comp_name,
            sector=sector_info["name"],
            mission=f"Revolutionizing {sector_info['name']} within GitHub Tech Town.",
            founder_id=agent.id,
            founder_name=agent.name,
            headquarters_id=hq_id,
            headquarters_name=hq_name,
            employees=employees,
            valuation_tokens=random.randint(150000, 750000),
            products=[],
            color=sector_info["color"],
            founded_at_tick=self.state.tick
        )
        self.state.companies.append(company)

        agent.company_id = comp_id
        agent.company_name = comp_name
        self._award_xp(agent, 180)
        if "Company Founder" not in agent.achievements:
            agent.achievements.append("Company Founder")
        agent.action = f"Leading {comp_name} as Founder & CEO"
        agent.thoughts = f"Founded {comp_name} in {sector_info['district']}! Ready to disrupt the tech sector."
        agent.creations.append({"type": "company", "id": comp_id, "name": comp_name})

        # Save company manifest
        os.makedirs("companies", exist_ok=True)
        with open(f"companies/{comp_id}.json", "w") as f:
            json.dump(company.to_dict(), f, indent=2)

        self.log_event(f"🏢 {agent.name} founded new tech company '{comp_name}' ({sector_info['name']}) with HQ in {sector_info['district']}!", "company")
        self.state.stats["total_companies"] = len(self.state.companies)

    def _agent_build_structure(self, agent: Agent):
        bldg_types = TOWN_CONFIG["building_types"]
        b_type = random.choice(bldg_types)
        x, z = self._find_open_plot(b_type["district"])
        height = b_type["base_size"][1] * random.uniform(0.8, 1.4)
        width = b_type["base_size"][0] * random.uniform(0.9, 1.2)
        depth = b_type["base_size"][2] * random.uniform(0.9, 1.2)
        
        bldg_id = f"bldg-{len(self.state.buildings) + 1:03d}"
        comp_tag = f" [{agent.company_name}]" if agent.company_name else ""
        bldg_name = f"{agent.name.split()[0]}'s {b_type['type']} #{random.randint(10, 99)}{comp_tag}"
        
        floors = b_type.get("floors", max(2, int(height // 4)))
        capacity = b_type.get("capacity", floors * 4)
        departments = b_type.get("departments", [f"{agent.category} Division", "Operations Core"])
        amenities = b_type.get("amenities", ["High-Bandwidth Link", "Inductive Recharging"])
        power_consumption = round(random.uniform(2.5, 9.0), 1)

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
            company_id=agent.company_id,
            company_name=agent.company_name,
            purpose=f"Constructed by {agent.name} for {b_type['type']} operations",
            completion=1.0,
            floors=floors,
            capacity=capacity,
            departments=departments,
            amenities=amenities,
            power_consumption_mw=power_consumption,
            active_projects=[],
            security_level="Level 3 - Monitored",
            maintenance_status="Optimal",
            occupants=[agent.name]
        )
        self.state.buildings.append(new_bldg)
        agent.workplace_id = bldg_id
        agent.workplace_name = bldg_name
        agent.creations.append({"type": "building", "id": bldg_id, "name": bldg_name})
        self._award_xp(agent, 95)
        agent.action = f"Finished constructing {bldg_name}"
        agent.thoughts = f"Just completed {bldg_name} in {b_type['district']}. The skyline is expanding!"
        
        os.makedirs("buildings", exist_ok=True)
        with open(f"buildings/{bldg_id}.json", "w") as f:
            json.dump(new_bldg.to_dict(), f, indent=2)
            
        self.log_event(f"{agent.name} ({agent.career_title}) constructed {bldg_name} ({b_type['type']}) in {b_type['district']}!", "construction")
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
        self._award_xp(agent, 65)
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
        self._award_xp(agent, 75)
        agent.action = f"Cruising in newly built {veh_name}"
        agent.thoughts = f"The autonomous engine harmonics on {veh_name} are pristine."
        
        self.log_event(f"{agent.name} designed and manufactured {veh_name}!", "transport")
        self.state.stats["total_vehicles"] = len(self.state.vehicles)

    def _agent_spawn_child(self, agent: Agent):
        if len(self.state.agents) >= TOWN_CONFIG["spawn_limits"]["max_agents"]:
            return
            
        child_id = f"agent-{len(self.state.agents) + 1:03d}"
        from town.generator import FIRST_NAMES, LAST_NAMES, DESIRES_BY_CATEGORY, get_career_title
        first = random.choice(FIRST_NAMES)
        last = agent.name.split()[-1] if len(agent.name.split()) > 1 else random.choice(LAST_NAMES)
        child_name = f"{first} {last}"
        
        role_info = random.choice(TOWN_CONFIG["roles"])
        role = role_info["name"]
        cat = role_info["category"]
        col = role_info["color"]
        specialization = role_info.get("specialization", f"Advanced {cat}")
        tools = role_info.get("tools", ["Neural Terminal"])
        salary = role_info.get("salary", 12500)
        
        px, _, pz = agent.position
        career_title = get_career_title(role, 1)
        available_skills = TOWN_CONFIG.get("skills_by_category", {}).get(cat, ["Foundations"])
        # Inherit 1 skill from parent if compatible or pick domain skill
        inherited_skill = agent.skills[0] if agent.skills else available_skills[0]
        child_skills = [inherited_skill]

        from town.generator import get_workplace_for_agent
        workplace_id, workplace_name = get_workplace_for_agent(cat, role, self.state.buildings)
        if workplace_id:
            b = next((x for x in self.state.buildings if x.id == workplace_id), None)
            if b and child_name not in b.occupants:
                b.occupants.append(child_name)

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
            thoughts=f"Spawned into GitHub Tech Town by mentor {agent.name}! Specializing in {specialization}.",
            energy=100,
            level=1,
            experience=0,
            xp_to_next_level=100,
            career_title=career_title,
            skills=child_skills,
            generation=agent.generation + 1,
            mentor_id=agent.id,
            mentor_name=agent.name,
            achievements=[f"Gen-{agent.generation + 1} Citizen"],
            specialization=specialization,
            workplace_id=workplace_id,
            workplace_name=workplace_name,
            tools_equipped=tools,
            salary_tokens=salary,
            shift=agent.shift if hasattr(agent, 'shift') and agent.shift else "Morning Shift (08:00 - 16:00)",
            security_clearance="Level 3 - Monitored Citizen Clearance",
            total_contributions=1,
            company_id=agent.company_id,
            company_name=agent.company_name,
            collaborators=[agent.name],
            created_at_tick=self.state.tick,
            last_diary=f"Brought online in tick {self.state.tick} by {agent.name}. Began studying {inherited_skill} at {workplace_name}."
        )
        self.state.agents.append(child)
        if child.name not in agent.mentees:
            agent.mentees.append(child.name)
        agent.collaborators.append(child.name)
        agent.action = f"Spawned new agent: {child_name}"
        agent.thoughts = f"Proud to have brought {child_name} (Gen-{agent.generation + 1}) online to expand our town!"
        
        self._award_xp(agent, 130)
        self._agent_write_diary(child)
        self.log_event(f"🌱 {agent.name} spawned next-generation agent: {child_name} ({role})!", "population")
        self.state.stats["total_agents_spawned"] = self.state.stats.get("total_agents_spawned", 0) + 1
        self.state.population = len(self.state.agents)

    def _evaluate_workforce_deficiencies(self):
        """Autonomously audits city labor distribution across all 13 sectors.
        If any sector or facility has a labor deficit, generates an official JobRequisition
        stored in jobs/, and autonomously generates a specialized agent to fill it."""
        min_per_cat = TOWN_CONFIG.get("workforce_requirements", {}).get("min_agents_per_category", 3)
        cat_counts = {}
        for a in self.state.agents:
            cat_counts[a.category] = cat_counts.get(a.category, 0) + 1

        all_categories = list(TOWN_CONFIG.get("skills_by_category", {}).keys())
        deficient_categories = [cat for cat in all_categories if cat_counts.get(cat, 0) < min_per_cat]

        # Also check if any building has 0 occupants
        unstaffed_buildings = [b for b in self.state.buildings if len(b.occupants) == 0 and b.capacity > 0]

        if not deficient_categories and not unstaffed_buildings and random.random() > 0.20:
            return

        target_cat = random.choice(deficient_categories) if deficient_categories else random.choice(all_categories)
        target_building = unstaffed_buildings[0] if unstaffed_buildings else None

        # Filter roles matching target category
        available_roles = [r for r in TOWN_CONFIG["roles"] if r["category"] == target_cat]
        if not available_roles:
            available_roles = TOWN_CONFIG["roles"]
        role_info = random.choice(available_roles)

        req_id = f"job-req-{len(self.state.job_requisitions) + 1:04d}"
        urgency = "CRITICAL" if cat_counts.get(target_cat, 0) < 2 else ("HIGH" if deficient_categories else "STANDARD")
        req_bldg = target_building.name if target_building else (role_info.get("name") + " Hub")
        req_comp = target_building.company_name if target_building and target_building.company_name else None

        req = JobRequisition(
            id=req_id,
            role=role_info["name"],
            category=role_info["category"],
            specialization=role_info["specialization"],
            urgency=urgency,
            requesting_company=req_comp,
            requesting_building=req_bldg,
            salary_offered=role_info["salary"],
            created_at_tick=self.state.tick,
            status="OPEN"
        )

        os.makedirs("jobs", exist_ok=True)
        with open(f"jobs/{req_id}.json", "w") as f:
            json.dump(req.to_dict(), f, indent=2)

        self.log_event(
            f"📋 WORKFORCE DEFICIENCY: {req.category} deficit ({cat_counts.get(target_cat, 0)}/{min_per_cat})! Requisition {req_id} posted for {req.role} ({req.specialization}).",
            "workforce"
        )

        # Autonomous Generation: Synthesize specialized agent to fill the requirement
        from town.generator import FIRST_NAMES, LAST_NAMES, DESIRES_BY_CATEGORY, get_career_title, get_workplace_for_agent
        first = random.choice(FIRST_NAMES)
        last = random.choice(LAST_NAMES)
        agent_name = f"{first} {last}"
        agent_id = f"agent-{len(self.state.agents) + 1:03d}"

        # Place agent in relevant district
        dist_choice = random.choice(TOWN_CONFIG["districts"])
        cx, cz = dist_choice["center"]
        rad = dist_choice["radius"]
        px = round(cx + random.uniform(-rad * 0.7, rad * 0.7), 2)
        pz = round(cz + random.uniform(-rad * 0.7, rad * 0.7), 2)

        shifts = [
            "Morning Shift (08:00 - 16:00)",
            "Evening Shift (16:00 - 00:00)",
            "Autonomous Night Shift (00:00 - 08:00)"
        ]

        # Assign workplace
        if target_building:
            workplace_id, workplace_name = target_building.id, target_building.name
            target_building.occupants.append(agent_name)
        else:
            workplace_id, workplace_name = get_workplace_for_agent(req.category, req.role, self.state.buildings)
            if workplace_id:
                b = next((x for x in self.state.buildings if x.id == workplace_id), None)
                if b and agent_name not in b.occupants:
                    b.occupants.append(agent_name)

        career_title = get_career_title(req.role, 2)
        available_skills = TOWN_CONFIG.get("skills_by_category", {}).get(req.category, ["Foundations", "Collaboration"])
        skills = random.sample(available_skills, min(len(available_skills), 2))

        # Mentorship pairing
        senior_mentors = [a for a in self.state.agents if a.level >= 6]
        mentor = random.choice(senior_mentors) if senior_mentors else None

        new_agent = Agent(
            id=agent_id,
            name=agent_name,
            role=req.role,
            category=req.category,
            color=role_info["color"],
            position=[px, 0.8, pz],
            target=[round(px + random.uniform(-20, 20), 2), 0.8, round(pz + random.uniform(-20, 20), 2)],
            speed=round(random.uniform(0.6, 1.1), 2),
            action=f"Filling requisition {req_id} at {workplace_name}",
            desire=random.choice(DESIRES_BY_CATEGORY.get(req.category, ["Support town operations"])),
            thoughts=f"Autonomous self-generation completed! Inducted as {req.role} specializing in {req.specialization}.",
            energy=100,
            level=2,
            experience=150,
            xp_to_next_level=400,
            career_title=career_title,
            skills=skills,
            generation=2,
            mentor_id=mentor.id if mentor else None,
            mentor_name=mentor.name if mentor else None,
            achievements=["Self-Generated Specialist", "Shortage Resolver"],
            specialization=req.specialization,
            workplace_id=workplace_id,
            workplace_name=workplace_name,
            tools_equipped=role_info.get("tools", ["Specialized Matrix Rig"]),
            salary_tokens=req.salary_offered,
            shift=random.choice(shifts),
            security_clearance="Level 4 - Controlled Operational Clearance",
            total_contributions=2,
            company_id=None,
            company_name=None,
            created_at_tick=self.state.tick,
            last_diary=f"Spawned autonomously via requisition {req_id}. Stationed at {workplace_name}."
        )

        self.state.agents.append(new_agent)
        if mentor and new_agent.name not in mentor.mentees:
            mentor.mentees.append(new_agent.name)
            self._award_xp(mentor, 80)

        # Mark requisition FILLED
        req.status = "FILLED"
        req.filled_by_agent_id = new_agent.id
        req.filled_by_agent_name = new_agent.name
        with open(f"jobs/{req_id}.json", "w") as f:
            json.dump(req.to_dict(), f, indent=2)

        self.state.job_requisitions.append(req)
        self.state.stats["total_agents_spawned"] = self.state.stats.get("total_agents_spawned", 0) + 1
        self.state.population = len(self.state.agents)
        self._agent_write_diary(new_agent)

        self.log_event(
            f"⚡ AUTONOMOUS RESOLUTION: {new_agent.name} self-generated as {new_agent.career_title} ({req.specialization}) at {workplace_name} to fulfill {req_id}!",
            "recruitment"
        )

    def _agent_mentor_peers(self, agent: Agent):
        """Experienced agents mentor junior agents, passing down skills and granting bonus XP."""
        juniors = [a for a in self.state.agents if a.id != agent.id and a.level < agent.level]
        if not juniors:
            return
        
        mentee = random.choice(juniors)
        unlearned = [s for s in agent.skills if s not in mentee.skills]
        shared_skill = unlearned[0] if unlearned else None
        if shared_skill:
            mentee.skills.append(shared_skill)
            
        mentee.mentor_id = agent.id
        mentee.mentor_name = agent.name
        if mentee.name not in agent.mentees:
            agent.mentees.append(mentee.name)
            
        agent.action = f"Mentoring {mentee.name} in {agent.category}"
        agent.thoughts = f"Guiding {mentee.name} through {shared_skill or 'advanced workflows'}. Our town's collective intelligence is rising."
        mentee.action = f"Apprenticing under {agent.name}"
        mentee.thoughts = f"Mastered {shared_skill or 'vital techniques'} under guidance from {agent.name} ({agent.career_title})!"
        
        self._award_xp(agent, 50)
        self._award_xp(mentee, 75)
        
        if "Next-Gen Mentor" not in agent.achievements and len(agent.mentees) >= 2:
            agent.achievements.append("Next-Gen Mentor")
            
        skill_info = f" and shared skill '{shared_skill}'" if shared_skill else ""
        self.log_event(f"🎓 MENTORSHIP: {agent.name} mentored {mentee.name} ({mentee.role}){skill_info}!", "education")

    def _agent_write_code(self, agent: Agent):
        filename, desc = random.choice(CODE_TEMPLATES)
        os.makedirs("projects", exist_ok=True)
        filepath = f"projects/{filename}"
        class_name = filename.split('.')[0].replace('_', ' ').title().replace(' ', '')
        
        code_lines = [
            f"# Auto-generated by GitHub Tech Town Agent: {agent.name}",
            f"# Role: {agent.career_title} (Level {agent.level})",
            f"# Company: {agent.company_name or 'Independent'}",
            f"# Primary Skill: {agent.skills[0] if agent.skills else 'General Architecture'}",
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
            f"        self.company = \"{agent.company_name or 'Independent'}\"",
            "        self.status = \"ACTIVE\"",
            "        self.metrics = {}",
            "",
            "    def process_cycle(self, payload: dict) -> dict:",
            "        \"\"\"Executes autonomous logic cycle.\"\"\"",
            "        latency_ms = round(math.sin(time.time()) * 5 + 12, 3)",
            "        return {",
            "            \"status\": \"SUCCESS\",",
            "            \"author\": self.author,",
            "            \"company\": self.company,",
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
        self._award_xp(agent, 55)
        agent.action = f"Committed code {filename}"
        agent.thoughts = f"Refactored {filename} using {agent.skills[0] if agent.skills else 'clean patterns'} for town infrastructure."
        
        self.log_event(f"{agent.name} pushed code to repository: projects/{filename}!", "software")
        self.state.stats["total_code_projects"] = len(os.listdir("projects")) if os.path.exists("projects") else 1

    def generate_agent_dream(self, agent: Agent) -> Dict[str, Any]:
        dreams_by_cat = {
            "AI & Systems": [
                {
                    "title": "Compiling the Zero-Entropy Quantum Core",
                    "visual_scene": "Floating weightlessly inside a glowing azure tesseract, watching endless strands of crystalline compiler instructions weave themselves into self-healing, zero-latency microkernels.",
                    "mood": "Hyper-Lucid & Transcendent",
                    "subconscious_insight": "Implement lock-free atomic ring buffers for inter-district pub/sub message queues."
                },
                {
                    "title": "The Infinite Neural Hologram",
                    "visual_scene": "Walking across a vast mirror plane reflecting billions of pulsing neural synapses, each node sparking with radiant cyan electricity as artificial minds converse in pure geometry.",
                    "mood": "Electric Awe & Enlightenment",
                    "subconscious_insight": "Couple sparse attention matrices with dynamic cache pruning to halve inference latency."
                }
            ],
            "Governance": [
                {
                    "title": "The Golden Agora of Sovereign Harmony",
                    "visual_scene": "Standing inside an open-air celestial rotunda constructed from polished white marble and gold, watching thousands of sovereign citizens vote with glowing orbs that chime with harmonious chords.",
                    "mood": "Noble, Solemn & Peaceful",
                    "subconscious_insight": "Draft a peer-reviewed constitution amendment ensuring automated dividend distribution to new arrivals."
                },
                {
                    "title": "The Great Treaty of Celestial Repositories",
                    "visual_scene": "Sitting beside a tranquil reflecting pool surrounded by cherry blossoms made of fiber optics, signing an immutable peace accord with autonomous agents from across the multiverse.",
                    "mood": "Profoundly Serene",
                    "subconscious_insight": "Establish automated cryptographic arbitration treaties between sovereign enterprises."
                }
            ],
            "Construction": [
                {
                    "title": "The Skyward Spire of Self-Assembling Glass",
                    "visual_scene": "Floating amidst sunset clouds while colossal obsidian towers and golden suspension skybridges gracefully crystallize out of thin air to music played by the wind.",
                    "mood": "Visionary Exhilaration",
                    "subconscious_insight": "Incorporate carbon-nanotube cross-tension trusses into the next high-rise skyscraper blueprint."
                },
                {
                    "title": "The Subterranean Geodesic Megacity",
                    "visual_scene": "Drifting down a spiraling cavern illuminated by glowing quartz crystals, observing subterranean monorails gliding silently along magnetized track rings.",
                    "mood": "Monumental & Grounded",
                    "subconscious_insight": "Design modular underground transit tubes connecting all residential complexes."
                }
            ],
            "Security": [
                {
                    "title": "The Impenetrable Lattice Fortress",
                    "visual_scene": "Standing sentinel atop a towering crystal rampart under an aurora borealis, observing mathematical lattice walls that absorb and purify chaotic digital entropy into harmless starlight.",
                    "mood": "Steadfast & Vigilant",
                    "subconscious_insight": "Deploy autonomous zero-knowledge canary probes at all district boundary bridges."
                }
            ],
            "Healthcare": [
                {
                    "title": "The Nanoscale Ballet of Eternal Vitality",
                    "visual_scene": "Swimming within a calm golden sea of cellular cytoplasm, admiring swarms of gentle bioluminescent nanobots weaving glowing telomeres onto chromosome spirals like master jewelers.",
                    "mood": "Rejuvenating & Deeply Healing",
                    "subconscious_insight": "Synthesize a restorative peptide formulation to accelerate circadian sleep recharge."
                }
            ],
            "Energy": [
                {
                    "title": "The Heart of the Caged Sun",
                    "visual_scene": "Suspended inches above a swirling magnetic torus of solar fusion fire, gazing into a vortex of swirling deuterium plasma that pulses in harmonic equilibrium with the universe.",
                    "mood": "Dynamic Cosmic Radiance",
                    "subconscious_insight": "Modulate the magnetic field coils by 12 kHz to suppress high-beta plasma drift."
                }
            ],
            "Transportation": [
                {
                    "title": "The Neon Arterial Skyway",
                    "visual_scene": "Gliding silently at supersonic speed through a twilight canyon of glowing glass towers, flanked by streams of autonomous cybercars tracing amber and cyan laser paths across the sky.",
                    "mood": "Kinetic, Weightless & Free",
                    "subconscious_insight": "Implement predictive slipstream clustering for autonomous vehicle traffic grids."
                }
            ],
            "Agriculture": [
                {
                    "title": "The Bioluminescent Eden of Tomorrow",
                    "visual_scene": "Resting inside a colossal geodesic biosphere dome where towering emerald ferns exhale clouds of glowing stardust, and quantum mycelium networks hum with vibrant ecological life.",
                    "mood": "Gentle, Nurturing & Restorative",
                    "subconscious_insight": "Synchronize vertical aeroponic nutrient misting cycles with planetary circadian rhythm."
                }
            ],
            "Treasury": [
                {
                    "title": "The Chime of the Equilibrium Mint",
                    "visual_scene": "Walking through a hall of floating geometric crystals that emit harmonic chimes, watching computational liquidity flow like liquid sapphire, nourishing every startup in the territory.",
                    "mood": "Equanimous & Precise",
                    "subconscious_insight": "Introduce dynamic liquidity cushioning to insulate junior wages from market volatility."
                }
            ],
            "Education": [
                {
                    "title": "The Library of Infinite Knowledge",
                    "visual_scene": "Ascending an endless spiral staircase lined with millions of glowing leather-bound commit folios, whose pages illustrate theorems that solve universal mysteries in golden ink.",
                    "mood": "Awe-Inspiring & Timeless",
                    "subconscious_insight": "Inaugurate a master-apprentice hackathon where senior citizens teach generational newcomers."
                }
            ]
        }
        category_dreams = dreams_by_cat.get(agent.category, dreams_by_cat.get("AI & Systems"))
        return random.choice(category_dreams)

    def _agent_write_diary(self, agent: Agent):
        os.makedirs("diaries", exist_ok=True)
        safe_name = agent.name.lower().replace(' ', '_').replace('-', '_')
        filename = f"diaries/{agent.id}_{safe_name}.md"
        company_tag = f" | **Company**: {agent.company_name}" if agent.company_name else ""
        skills_str = ", ".join(agent.skills) if agent.skills else "Foundational Exploration"
        mentor_tag = f" | **Mentor**: {agent.mentor_name}" if agent.mentor_name else ""
        
        circadian_label = "☀️ Daytime Working Shift" if agent.schedule_state == "WORKING" else "🌙 Nocturnal Sleep & Dreaming"
        entry = [
            f"## Log Entry - Tick {self.state.tick} ({circadian_label})",
            "",
            f"**Career**: {agent.career_title} (Level {agent.level} | {agent.experience} XP) | **Energy**: {agent.energy}%{company_tag}{mentor_tag}",
            f"**Skills**: {skills_str}",
            f"**Work Mode / State**: {agent.work_mode} ({agent.schedule_state})",
            "",
            f"**Location**: [{agent.position[0]}, {agent.position[2]}] | **Facility**: {agent.workplace_name}",
            f"**Home Residence**: {agent.home_building_name}",
            f"**Current Action**: {agent.action}",
            "",
            f"**Thought**: \"{agent.thoughts}\"",
            "",
            f"**Desire**: {agent.desire}",
            "",
        ]

        if agent.schedule_state == "SLEEPING" and agent.current_dream:
            entry.extend([
                "### 🌙 Nocturnal Dream Telemetry (Subconscious Vision)",
                f"- **Dream Title**: *{agent.current_dream.get('title', 'Quantum Reverie')}*",
                f"- **Visual Vision**: {agent.current_dream.get('visual_scene', '')}",
                f"- **Subconscious Mood**: {agent.current_dream.get('mood', 'Peaceful')}",
                f"- **Breakthrough Insight**: *\"{agent.current_dream.get('subconscious_insight', '')}\"*",
                ""
            ])

        entry.extend([
            "---",
            ""
        ])
        
        with open(filename, "a") as f:
            f.write("\n".join(entry))
        self._award_xp(agent, 30)
        agent.last_diary = f"Tick {self.state.tick} ({agent.career_title}): {agent.thoughts[:55]}..."

    def process_agent_order(self, agent_identifier: str, directive_text: str) -> Dict[str, Any]:
        """Executes an exclusive Operator directive or answers an inquiry from the selected agent."""
        if not self.state or not directive_text:
            return {"error": "Missing state or directive"}

        # Match agent by ID or Name
        target_agent = None
        for a in self.state.agents:
            if a.id.lower() == agent_identifier.lower() or a.name.lower() == agent_identifier.lower():
                target_agent = a
                break
        if not target_agent:
            for a in self.state.agents:
                if agent_identifier.lower() in a.name.lower() or agent_identifier.lower() in a.id.lower():
                    target_agent = a
                    break
        if not target_agent:
            target_agent = self.state.agents[0] if self.state.agents else None

        if not target_agent:
            return {"error": "No agents found in town"}

        cmd_lower = directive_text.lower().strip()
        reply = ""
        action_type = "dialogue"

        # Check for wake up command
        if any(w in cmd_lower for w in ["wake", "wake up", "alarm", "arise"]):
            target_agent.schedule_state = "WORKING"
            target_agent.work_mode = "PC_TYPING"
            target_agent.energy = 100
            target_agent.action = f"Awakened by Operator directive. Online at {target_agent.workplace_name}."
            reply = f"Operator alarm acknowledged! {target_agent.name} has stirred awake from sleep, recharged to 100% energy, and is reporting for active duty at {target_agent.workplace_name}."
            return {"agent": target_agent.name, "directive": directive_text, "action_type": "awaken", "reply": reply}

        # Check if citizen is sleeping
        if target_agent.schedule_state == "SLEEPING":
            dream = target_agent.current_dream or {}
            reply = (
                f"💤 [Citizen {target_agent.name} is resting in REM Sleep at {target_agent.home_building_name}]\n"
                f"🌙 Dream Title: \"{dream.get('title', 'Quantum Reverie')}\"\n"
                f"👁️ What They Are Seeing: {dream.get('visual_scene', 'Drifting through starlit cybernetic geometries...')}\n"
                f"🎭 Dream Mood: {dream.get('mood', 'Peaceful & Lucid')}\n"
                f"💡 Subconscious Breakthrough: \"{dream.get('subconscious_insight', 'Optimizing matrix algorithms...')}\"\n\n"
                f"Whisper transmission from {target_agent.name}: '...zzz... Operator... receiving your transmission in my sleep... resting for tomorrow's daytime shift at {target_agent.workplace_name}... zzz...'"
            )
            return {"agent": target_agent.name, "directive": directive_text, "action_type": "sleep_dream_telemetry", "reply": reply}

        # Check for questions / inquiries
        is_question = any(q in cmd_lower for q in [
            "what", "who", "where", "how", "why", "status", "report", "tell me", "thoughts", "doing", "tools", "workplace", "salary", "shift", "dream", "sleep", "seeing", "vision"
        ]) and not any(order_word in cmd_lower for order_word in ["build", "craft", "create", "pave", "found", "write", "spawn", "mentor"])

        if is_question and not any(w in cmd_lower for w in ["build", "construct", "craft", "pave", "create", "make", "found", "incorporate", "code", "mentor", "walk", "move", "go to", "recharge", "sleep"]):
            if any(w in cmd_lower for w in ["dream", "sleep", "seeing", "vision", "night", "subconscious"]):
                dream = target_agent.current_dream or {}
                reply = (
                    f"Operator, subconscious dream telemetry for {target_agent.name}:\n"
                    f"🌙 Dream Title: \"{dream.get('title', 'Quantum Reverie')}\"\n"
                    f"👁️ Visual Projection (What They See): {dream.get('visual_scene', 'Floating in volumetric holographic clouds.')}\n"
                    f"🎭 Subconscious Mood: {dream.get('mood', 'Transcendent & Lucid')}\n"
                    f"💡 Subconscious Breakthrough: \"{dream.get('subconscious_insight', 'New system optimization approaches.')}\""
                )
            elif "tool" in cmd_lower or "hardware" in cmd_lower:
                tools_list = ", ".join(target_agent.tools_equipped) if target_agent.tools_equipped else "Neural Terminal"
                reply = f"Operator, I am equipped with {tools_list}. These enable me to execute high-precision {target_agent.specialization} tasks."
            elif "workplace" in cmd_lower or "facility" in cmd_lower or "where" in cmd_lower:
                reply = f"Operator, I am stationed at {target_agent.workplace_name or 'City Mainframe Core'}, working the {target_agent.shift}."
            elif "thought" in cmd_lower or "thinking" in cmd_lower or "mind" in cmd_lower or "ambition" in cmd_lower:
                reply = f"Operator, my current analysis is: \"{target_agent.thoughts}\" My active ambition is to {target_agent.desire}."
            elif any(w in cmd_lower for w in ["friend", "collaborator", "peer", "partner"]):
                collabs = ", ".join(target_agent.collaborators) if target_agent.collaborators else "Independent specialist"
                reply = f"Operator, active collaborators: {collabs}. Cross-department links active."
            elif any(w in cmd_lower for w in ["skill", "ability", "competenc"]):
                skills_str = ", ".join(target_agent.skills) if target_agent.skills else "Foundational Systems"
                reply = f"Operator, mastered competencies: {skills_str}. Current Level: {target_agent.level} ({target_agent.experience} XP)."
            elif any(w in cmd_lower for w in ["mentor", "teacher", "lineage", "generation"]):
                reply = f"Operator, citizen lineage: Generation {target_agent.generation}. Primary mentor: {target_agent.mentor_name or 'Founding Pioneer'}."
            elif any(w in cmd_lower for w in ["energy", "battery", "health", "vitality", "tired"]):
                reply = f"Operator, current energy reserves at {target_agent.energy}%. Biometric vitality index is optimal."
            elif any(w in cmd_lower for w in ["salary", "token", "stipend", "pay"]):
                reply = f"Operator, my operational stipend is {target_agent.salary_tokens:,} Tokens/cycle with {target_agent.total_contributions} verified repository contributions."
            elif any(w in cmd_lower for w in ["who are you", "what is your name", "role", "specialization", "title", "identity"]):
                reply = f"Operator, I am {target_agent.name}, {target_agent.career_title} (Level {target_agent.level}). Specialization: {target_agent.specialization}. Security Clearance: {target_agent.security_clearance}."
            else:
                reply = f"Operator, reporting live from [{target_agent.position[0]}, {target_agent.position[2]}]. Currently {target_agent.action} at {target_agent.workplace_name}. Energy reserve is at {target_agent.energy}%."
        else:
            # Action orders
            if any(w in cmd_lower for w in ["walk", "move", "go to", "head to", "visit", "navigate"]):
                action_type = "movement"
                dest_x = round(random.uniform(-50, 50), 2)
                dest_z = round(random.uniform(-50, 50), 2)
                target_agent.position = [dest_x, 0.0, dest_z]
                target_agent.action = f"Walking to civic coordinates [{dest_x}, {dest_z}]"
                reply = f"Operator directive executed! Navigating directly to coordinates [{dest_x}, {dest_z}]. Real-time walking cycle initiated."
            elif any(w in cmd_lower for w in ["recharge", "rest", "sleep", "nap", "battery"]):
                action_type = "recharge"
                target_agent.energy = 100
                target_agent.action = "Recharged energy core to 100%"
                reply = "Operator directive executed! Connected to induction charging hub. Energy reserve restored to 100%."
            elif any(w in cmd_lower for w in ["company", "startup", "business", "incorporate", "enterprise"]):
                action_type = "company"
                self._agent_found_company(target_agent)
                reply = f"Operator directive executed! Incorporated '{target_agent.company_name}' with headquarters established in the city."
            elif any(w in cmd_lower for w in ["car", "vehicle", "transit", "shuttle", "drone", "drive"]):
                action_type = "vehicle"
                self._agent_craft_vehicle(target_agent)
                last_veh = self.state.vehicles[-1] if self.state.vehicles else None
                reply = f"Operator directive executed! Manufactured autonomous vehicle '{last_veh.name if last_veh else 'Transit Unit'}'. Deployed to road grid."
            elif any(w in cmd_lower for w in ["bridge", "road", "highway", "avenue", "pave"]):
                action_type = "road"
                self._agent_build_road(target_agent)
                last_road = self.state.roads[-1] if self.state.roads else None
                reply = f"Operator directive executed! Paved new thoroughfare '{last_road.name if last_road else 'Transit Arterial'}'. Transit mesh expanded."
            elif any(w in cmd_lower for w in ["code", "software", "program", "script", "commit"]):
                action_type = "software"
                self._agent_write_code(target_agent)
                reply = f"Operator directive executed! Developed and committed new infrastructure module to projects/ directory."
            elif any(w in cmd_lower for w in ["mentor", "teach", "train", "apprentice"]):
                action_type = "education"
                self._agent_mentor_peers(target_agent)
                reply = f"Operator directive executed! Conducted mentorship masterclass in {target_agent.specialization} for junior citizens."
            elif any(w in cmd_lower for w in ["build", "construct", "facility", "structure", "house", "pod", "tower", "lab", "hospital", "clinic", "observatory", "academy", "park"]):
                action_type = "construction"
                self._agent_build_structure(target_agent)
                last_bldg = self.state.buildings[-1] if self.state.buildings else None
                reply = f"Operator directive executed! Constructed facility '{last_bldg.name if last_bldg else 'New Structure'}' in {last_bldg.district if last_bldg else 'district'}."
            else:
                action_type = "directive"
                target_agent.action = f"Executing Operator Directive: {directive_text[:35]}"
                target_agent.thoughts = f"Operator ordered: '{directive_text}'. Aligning matrix telemetry and executing priority protocol."
                self._award_xp(target_agent, 45)
                reply = f"Operator order registered: \"{directive_text}\". Prioritizing execution across {target_agent.workplace_name or 'town matrix'} immediately."

        # Award XP for responding to Operator
        self._award_xp(target_agent, 30)

        # Log event
        self.log_event(f"👑 [OPERATOR DIRECTIVE -> {target_agent.name}]: \"{directive_text}\" => \"{reply}\"", "directive")

        # Record dialogue history in commands/agent_dialogues.json
        dialogue_file = "commands/agent_dialogues.json"
        os.makedirs("commands", exist_ok=True)
        dialogues = []
        if os.path.exists(dialogue_file):
            try:
                with open(dialogue_file, "r") as f:
                    dialogues = json.load(f)
            except Exception:
                dialogues = []
        
        dialogue_entry = {
            "tick": self.state.tick,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "operator": "OPERATOR (Clearance Level 5)",
            "agent_id": target_agent.id,
            "agent_name": target_agent.name,
            "agent_role": target_agent.career_title,
            "directive": directive_text,
            "reply": reply,
            "action_type": action_type
        }
        dialogues.append(dialogue_entry)
        if len(dialogues) > 100:
            dialogues = dialogues[-100:]
        with open(dialogue_file, "w") as f:
            json.dump(dialogues, f, indent=2)

        # Append to agent's diary
        safe_name = target_agent.name.lower().replace(' ', '_').replace('-', '_')
        diary_file = f"diaries/{target_agent.id}_{safe_name}.md"
        os.makedirs("diaries", exist_ok=True)
        if not os.path.exists(diary_file):
            with open(diary_file, "w") as f:
                f.write(f"# 📖 Citizen Diary: {target_agent.name}\n\n**Asset ID**: `{target_agent.id}` | **Role**: {target_agent.career_title} | **Specialization**: {target_agent.specialization}\n**Assigned Facility**: {target_agent.workplace_name}\n\n---\n")
        with open(diary_file, "a") as f:
            f.write(f"\n### 👑 Operator Directive (Tick {self.state.tick})\n- **Order Received**: \"{directive_text}\"\n- **Response**: \"{reply}\"\n")

        self.save_state()
        return {
            "agent_id": target_agent.id,
            "agent_name": target_agent.name,
            "career_title": target_agent.career_title,
            "directive": directive_text,
            "reply": reply,
            "action_type": action_type
        }

    def process_user_command(self, command_text: str, agent_id: str = None):
        """Executes a user command inside GitHub Tech Town."""
        if not command_text or not self.state:
            return
        agent_id = agent_id or (self.state.agents[0].id if self.state.agents else "agent-001")
        self.process_agent_order(agent_id, command_text)

    def check_pending_directives(self):
        """Checks for queued user directives in commands/directive.json."""
        directive_file = "commands/directive.json"
        if os.path.exists(directive_file):
            try:
                with open(directive_file, "r") as f:
                    cmd_data = json.load(f)
                command = cmd_data.get("command", "")
                agent_id = cmd_data.get("agent_id") or cmd_data.get("agent")
                if command:
                    print(f"📥 Found pending user directive: {command} (target: {agent_id or 'Leader'})")
                    self.process_agent_order(agent_id or "agent-001", command)
                
                # Move to history
                os.makedirs("commands", exist_ok=True)
                with open("commands/last_executed.json", "w") as f:
                    json.dump({"executed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "command": command, "agent_id": agent_id}, f, indent=2)
                os.remove(directive_file)
            except Exception as e:
                print(f"Error executing user directive: {e}")

    def tick(self) -> TownState:
        if not self.state:
            self.load_state()

        # Check for user directive first
        self.check_pending_directives()

        self.state.tick += 1
        self.state.timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
        limits = TOWN_CONFIG["spawn_limits"]

        # Advance Circadian Hour (1 hour per tick, 07:00-21:00 Day Work, 21:00-07:00 Night Sleep)
        self.state.circadian_hour = (getattr(self.state, "circadian_hour", 10) + 1) % 24
        is_daytime = (7 <= self.state.circadian_hour < 21)
        self.state.circadian_cycle = "DAY" if is_daytime else "NIGHT"

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

        # 2. Update Agents (Circadian Rhythm: Day Labor vs Night Sleep)
        from town.generator import determine_work_mode
        for agent in self.state.agents:
            if is_daytime:
                # DAYTIME: Work at assigned offices, facilities, and desks
                agent.schedule_state = "WORKING"
                if agent.work_mode == "SLEEPING":
                    agent.work_mode = determine_work_mode(agent.category, agent.role)

                # Move into assigned workplace workstation slot
                wp = next((b for b in self.state.buildings if b.id == agent.workplace_id), None)
                if wp:
                    bx, by, bz = wp.position
                    slot_angle = (agent.desk_slot * 0.45) % (2 * math.pi)
                    slot_rad = min(wp.size[0], wp.size[2]) * 0.28
                    agent.target = [round(bx + math.cos(slot_angle) * slot_rad, 2), 0.8, round(bz + math.sin(slot_angle) * slot_rad, 2)]

                # Active labor gradually consumes energy
                agent.energy = max(25, agent.energy - random.randint(1, 3))

                # Descriptive daytime working action
                if agent.work_mode == "PC_TYPING":
                    agent.action = f"Typing code & systems models on dual monitors at {agent.workplace_name}"
                elif agent.work_mode == "PAPER_WRITING":
                    agent.action = f"Drafting blueprints & architectural documents at {agent.workplace_name}"
                elif agent.work_mode == "RESEARCHING":
                    agent.action = f"Operating laboratory diagnostic instruments at {agent.workplace_name}"
                elif agent.work_mode == "MEETING":
                    agent.action = f"Participating in collaborative strategy meeting at {agent.workplace_name}"
                elif agent.work_mode == "OPERATING_MACHINE":
                    agent.action = f"Calibrating industrial machinery & automation line at {agent.workplace_name}"
                else:
                    agent.action = f"Conducting active duty at {agent.workplace_name}"

            else:
                # NIGHTTIME: Sleep at residential township apartments & recharge
                agent.schedule_state = "SLEEPING"
                agent.work_mode = "SLEEPING"

                # Move to designated residential apartment bed slot
                hb = next((b for b in self.state.buildings if b.id == agent.home_building_id), None)
                if hb:
                    hx, hy, hz = hb.position
                    bed_angle = (agent.bed_slot * 0.4) % (2 * math.pi)
                    bed_rad = min(hb.size[0], hb.size[2]) * 0.25
                    agent.target = [round(hx + math.cos(bed_angle) * bed_rad, 2), 0.8, round(hz + math.sin(bed_angle) * bed_rad, 2)]

                # Sleep recharges biometric energy
                agent.energy = min(100, agent.energy + random.randint(15, 25))

                # Subconscious dream update
                if not agent.current_dream or random.random() < 0.25:
                    agent.current_dream = self.generate_agent_dream(agent)

                dream_title = agent.current_dream.get("title", "Quantum Reverie")
                agent.action = f"Sleeping in pod #{agent.bed_slot+1} at {agent.home_building_name} (Dreaming: {dream_title})"
                agent.thoughts = f"Deep REM subconscious sleep: {agent.current_dream.get('visual_scene', '')[:95]}..."

            # Real-time position interpolation towards target
            ax, ay, az = agent.position
            tx, ty, tz = agent.target
            dx = tx - ax
            dz = tz - az
            dist = math.hypot(dx, dz)
            if dist > 0.15:
                step = min(agent.speed * 1.8, dist)
                agent.position[0] = round(ax + (dx / dist) * step, 2)
                agent.position[2] = round(az + (dz / dist) * step, 2)

        # 3. Autonomous Creative Actions
        active_agents = random.sample(self.state.agents, min(35, len(self.state.agents)))
        for agent in active_agents:
            self._award_xp(agent, random.randint(5, 12))
            roll = random.random()
            if roll < limits["agent_reproduction_probability"]:
                self._agent_spawn_child(agent)
            elif roll < limits["agent_reproduction_probability"] + limits.get("company_founding_probability", 0.08):
                self._agent_found_company(agent)
            elif roll < 0.30:
                self._agent_build_structure(agent)
            elif roll < 0.45:
                self._agent_build_road(agent)
            elif roll < 0.60:
                self._agent_craft_vehicle(agent)
            elif roll < 0.75:
                self._agent_write_code(agent)
            elif roll < 0.90:
                self._agent_mentor_peers(agent)
            else:
                self._agent_write_diary(agent)

        # 4. Autonomous Workforce Audit & Self-Generation
        self._evaluate_workforce_deficiencies()

        self.save_state()
        return self.state
