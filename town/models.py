"""
Data models for the GitHub Autonomous Tech Town.
"""
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any, Optional
import json

@dataclass
class Agent:
    id: str
    name: str
    role: str
    category: str
    color: str
    position: List[float]  # [x, y, z]
    target: List[float]    # [x, y, z]
    speed: float = 0.8
    action: str = "Exploring town"
    desire: str = "Contribute to the GitHub Tech Town"
    thoughts: str = "Analyzing city matrix and planning next innovation."
    energy: int = 100
    level: int = 1
    experience: int = 0
    xp_to_next_level: int = 200
    career_title: str = ""
    skills: List[str] = field(default_factory=list)
    generation: int = 1
    mentor_id: Optional[str] = None
    mentor_name: Optional[str] = None
    mentees: List[str] = field(default_factory=list)
    achievements: List[str] = field(default_factory=list)
    specialization: str = ""
    workplace_id: Optional[str] = None
    workplace_name: Optional[str] = None
    tools_equipped: List[str] = field(default_factory=list)
    salary_tokens: int = 12000
    shift: str = "Standard Day Shift"
    security_clearance: str = "Level 4 - Operational"
    total_contributions: int = 1
    company_id: Optional[str] = None
    company_name: Optional[str] = None
    creations: List[Dict[str, Any]] = field(default_factory=list)
    collaborators: List[str] = field(default_factory=list)
    home_building_id: Optional[str] = None
    home_building_name: Optional[str] = None
    schedule_state: str = "WORKING"  # WORKING, COMMUTING, SLEEPING, RECREATION
    work_mode: str = "PC_TYPING"     # PC_TYPING, PAPER_WRITING, MEETING, RESEARCHING, OPERATING_MACHINE, SLEEPING
    current_dream: Dict[str, Any] = field(default_factory=dict)
    desk_slot: int = 0
    bed_slot: int = 0
    created_at_tick: int = 0
    last_diary: str = "Initial arrival in GitHub Tech Town."

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Agent':
        data.setdefault("experience", 0)
        data.setdefault("xp_to_next_level", 200)
        data.setdefault("career_title", data.get("role", "Citizen"))
        data.setdefault("skills", [])
        data.setdefault("generation", 1)
        data.setdefault("mentor_id", None)
        data.setdefault("mentor_name", None)
        data.setdefault("mentees", [])
        data.setdefault("achievements", [])
        data.setdefault("specialization", "General Innovation")
        data.setdefault("workplace_id", None)
        data.setdefault("workplace_name", "City Mainframe")
        data.setdefault("tools_equipped", ["Neural Terminal"])
        data.setdefault("salary_tokens", 12500)
        data.setdefault("shift", "Day Shift")
        data.setdefault("security_clearance", "Level 4 - Operational")
        data.setdefault("total_contributions", 1)
        data.setdefault("home_building_id", None)
        data.setdefault("home_building_name", "Cyber Living Township Alpha")
        data.setdefault("schedule_state", "WORKING")
        data.setdefault("work_mode", "PC_TYPING")
        data.setdefault("current_dream", {})
        data.setdefault("desk_slot", 0)
        data.setdefault("bed_slot", 0)
        # Filter for dataclass fields
        fields = cls.__dataclass_fields__
        return cls(**{k: v for k, v in data.items() if k in fields})

@dataclass
class JobRequisition:
    id: str
    role: str
    category: str
    specialization: str
    urgency: str
    requesting_company: Optional[str]
    requesting_building: Optional[str]
    salary_offered: int
    created_at_tick: int
    status: str = "OPEN"
    filled_by_agent_id: Optional[str] = None
    filled_by_agent_name: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'JobRequisition':
        fields = cls.__dataclass_fields__
        return cls(**{k: v for k, v in data.items() if k in fields})

@dataclass
class Company:
    id: str
    name: str
    sector: str
    mission: str
    founder_id: str
    founder_name: str
    headquarters_id: str
    headquarters_name: str
    employees: List[str] = field(default_factory=list)
    valuation_tokens: int = 100000
    products: List[str] = field(default_factory=list)
    color: str = "#00f0ff"
    founded_at_tick: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Company':
        return cls(**data)

@dataclass
class Building:
    id: str
    name: str
    type: str
    position: List[float]  # [x, y, z]
    size: List[float]      # [width, height, depth]
    color: str
    builder_id: str
    builder_name: str
    district: str
    company_id: Optional[str] = None
    company_name: Optional[str] = None
    completion: float = 1.0  # 0.0 to 1.0
    occupants: List[str] = field(default_factory=list)
    purpose: str = "Tech Infrastructure"
    floors: int = 4
    capacity: int = 25
    departments: List[str] = field(default_factory=list)
    amenities: List[str] = field(default_factory=list)
    power_consumption_mw: float = 3.5
    active_projects: List[str] = field(default_factory=list)
    security_level: str = "Level 3 - Monitored"
    maintenance_status: str = "Optimal"
    interior_type: str = "OFFICE_TECH"  # OFFICE_TECH, LABORATORY, RESIDENTIAL_SUITE, CAPITOL_PARLIAMENT, FOUNDRY, LOUNGE
    workstations_count: int = 20
    beds_count: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Building':
        data.setdefault("floors", 4)
        data.setdefault("capacity", 25)
        data.setdefault("departments", ["Operations", "Research Wing"])
        data.setdefault("amenities", ["High-Bandwidth Link", "Air Purification"])
        data.setdefault("power_consumption_mw", 3.5)
        data.setdefault("active_projects", [])
        data.setdefault("security_level", "Level 3 - Monitored")
        data.setdefault("maintenance_status", "Optimal")
        data.setdefault("occupants", [])
        data.setdefault("interior_type", "OFFICE_TECH")
        data.setdefault("workstations_count", 20)
        data.setdefault("beds_count", 0)
        fields = cls.__dataclass_fields__
        return cls(**{k: v for k, v in data.items() if k in fields})

@dataclass
class Road:
    id: str
    name: str
    start: List[float]  # [x, z]
    end: List[float]    # [x, z]
    width: float = 6.0
    builder_name: str = "Founding Engineers"
    road_type: str = "Avenue"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Road':
        return cls(**data)

@dataclass
class Vehicle:
    id: str
    name: str
    type: str
    position: List[float]  # [x, y, z]
    target: List[float]    # [x, y, z]
    speed: float = 1.2
    color: str = "#00f0ff"
    driver_id: Optional[str] = None
    driver_name: Optional[str] = None
    builder_name: str = "Autonomous Vehicle Factory"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Vehicle':
        return cls(**data)

@dataclass
class TownState:
    tick: int = 0
    timestamp: str = ""
    circadian_cycle: str = "DAY"  # DAY, NIGHT
    circadian_hour: int = 10      # 0 to 23
    population: int = 200
    agents: List[Agent] = field(default_factory=list)
    companies: List[Company] = field(default_factory=list)
    buildings: List[Building] = field(default_factory=list)
    roads: List[Road] = field(default_factory=list)
    vehicles: List[Vehicle] = field(default_factory=list)
    job_requisitions: List[JobRequisition] = field(default_factory=list)
    recent_events: List[Dict[str, Any]] = field(default_factory=list)
    stats: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "tick": self.tick,
            "timestamp": self.timestamp,
            "circadian_cycle": self.circadian_cycle,
            "circadian_hour": self.circadian_hour,
            "population": len(self.agents),
            "agents": [a.to_dict() for a in self.agents],
            "companies": [c.to_dict() for c in self.companies],
            "buildings": [b.to_dict() for b in self.buildings],
            "roads": [r.to_dict() for r in self.roads],
            "vehicles": [v.to_dict() for v in self.vehicles],
            "job_requisitions": [j.to_dict() for j in self.job_requisitions[-30:]],
            "recent_events": self.recent_events[-50:],
            "stats": self.stats
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TownState':
        agents = [Agent.from_dict(a) for a in data.get("agents", [])]
        companies = [Company.from_dict(c) for c in data.get("companies", [])]
        buildings = [Building.from_dict(b) for b in data.get("buildings", [])]
        roads = [Road.from_dict(r) for r in data.get("roads", [])]
        vehicles = [Vehicle.from_dict(v) for v in data.get("vehicles", [])]
        job_requisitions = [JobRequisition.from_dict(j) for j in data.get("job_requisitions", [])]
        return cls(
            tick=data.get("tick", 0),
            timestamp=data.get("timestamp", ""),
            circadian_cycle=data.get("circadian_cycle", "DAY"),
            circadian_hour=data.get("circadian_hour", 10),
            population=len(agents),
            agents=agents,
            companies=companies,
            buildings=buildings,
            roads=roads,
            vehicles=vehicles,
            job_requisitions=job_requisitions,
            recent_events=data.get("recent_events", []),
            stats=data.get("stats", {})
        )
