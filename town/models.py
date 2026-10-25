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
    company_id: Optional[str] = None
    company_name: Optional[str] = None
    creations: List[Dict[str, Any]] = field(default_factory=list)
    collaborators: List[str] = field(default_factory=list)
    created_at_tick: int = 0
    last_diary: str = "Initial arrival in GitHub Tech Town."

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Agent':
        return cls(**data)

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

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Building':
        return cls(**data)

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
    population: int = 200
    agents: List[Agent] = field(default_factory=list)
    companies: List[Company] = field(default_factory=list)
    buildings: List[Building] = field(default_factory=list)
    roads: List[Road] = field(default_factory=list)
    vehicles: List[Vehicle] = field(default_factory=list)
    recent_events: List[Dict[str, Any]] = field(default_factory=list)
    stats: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "tick": self.tick,
            "timestamp": self.timestamp,
            "population": len(self.agents),
            "agents": [a.to_dict() for a in self.agents],
            "companies": [c.to_dict() for c in self.companies],
            "buildings": [b.to_dict() for b in self.buildings],
            "roads": [r.to_dict() for r in self.roads],
            "vehicles": [v.to_dict() for v in self.vehicles],
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
        return cls(
            tick=data.get("tick", 0),
            timestamp=data.get("timestamp", ""),
            population=len(agents),
            agents=agents,
            companies=companies,
            buildings=buildings,
            roads=roads,
            vehicles=vehicles,
            recent_events=data.get("recent_events", []),
            stats=data.get("stats", {})
        )
