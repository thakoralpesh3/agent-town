"""Configuration settings for GitHub Autonomous Tech Town."""

TOWN_CONFIG = {
    "name": "GitHub Tech Town",
    "version": "1.0.0",
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
        {"name": "Urban Architect", "category": "Construction", "color": "#3b82f6"},
        {"name": "Road & Infrastructure Engineer", "category": "Construction", "color": "#64748b"},
        {"name": "Autonomous Vehicle Designer", "category": "Engineering", "color": "#f59e0b"},
        {"name": "AI & Neural Researcher", "category": "Research", "color": "#ec4899"},
        {"name": "Quantum Systems Engineer", "category": "Engineering", "color": "#8b5cf6"},
        {"name": "Full-Stack Web Architect", "category": "Software", "color": "#10b981"},
        {"name": "DevOps & Cloud Sentinel", "category": "Infrastructure", "color": "#06b6d4"},
        {"name": "Cyber Botanist", "category": "Ecology", "color": "#84cc16"},
        {"name": "Town Chronicler & Historian", "category": "Society", "color": "#d946ef"},
        {"name": "Energy & Fusion Specialist", "category": "Energy", "color": "#e11d48"},
        {"name": "Cybernetics Artisan", "category": "Art", "color": "#f43f5e"},
        {"name": "Security & Cryptographer", "category": "Security", "color": "#14b8a6"},
    ],
    "building_types": [
        {"type": "Tech Tower", "base_size": [16, 45, 16], "color": "#0ea5e9", "district": "Silicon Central"},
        {"type": "AI Research Lab", "base_size": [20, 25, 20], "color": "#a855f7", "district": "Innovation Matrix"},
        {"type": "Residential Pod", "base_size": [12, 18, 12], "color": "#22c55e", "district": "Residential Quarter"},
        {"type": "Cyber Cafe", "base_size": [14, 10, 14], "color": "#eab308", "district": "Cyber Commons"},
        {"type": "Quantum Data Center", "base_size": [24, 20, 24], "color": "#6366f1", "district": "Industrial Sector"},
        {"type": "Solar Fusion Array", "base_size": [18, 8, 18], "color": "#f97316", "district": "Industrial Sector"},
        {"type": "Holo Park", "base_size": [25, 4, 25], "color": "#10b981", "district": "Cyber Commons"},
        {"type": "Vehicle Factory", "base_size": [22, 16, 22], "color": "#f59e0b", "district": "Industrial Sector"},
    ],
    "vehicle_types": [
        {"type": "Autonomous Cybercar", "speed": 1.4, "color": "#00f0ff"},
        {"type": "Hover Shuttle", "speed": 1.8, "color": "#a855f7"},
        {"type": "Cargo Drone Carrier", "speed": 1.1, "color": "#f59e0b"},
        {"type": "Surveyor Pod", "speed": 1.5, "color": "#10b981"},
    ],
    "spawn_limits": {
        "max_agents": 500,
        "agent_reproduction_probability": 0.05,
        "building_construction_probability": 0.25,
        "road_construction_probability": 0.20,
        "vehicle_construction_probability": 0.15,
        "coding_probability": 0.35,
    }
}
