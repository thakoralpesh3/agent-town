#!/usr/bin/env python3
"""
GitHub Autonomous Tech Town - Main Controller CLI
Allows running ticks, 24/7 daemon loop, initializing town, serving the 3D viewer, and executing user commands.
"""
import argparse
import sys
import os
import time
import http.server
import socketserver
import threading
from town.simulation import TownEngine
from town.generator import generate_initial_state
from town.git_ops import commit_town_activity

def serve_web(port: int = 8000, directory: str = "docs"):
    """Serves the 3D Tech Town WebGL viewer."""
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)

        def log_message(self, format, *args):
            # Suppress noisy HTTP asset logs
            pass

    print(f"\n=======================================================")
    print(f"🚀 3D Tech Town Viewer live at: http://localhost:{port}")
    print(f"Press Ctrl+C to stop.")
    print(f"=======================================================\n")
    with http.server.ThreadingHTTPServer(("", port), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down 3D Web server...")

def main():
    parser = argparse.ArgumentParser(description="GitHub Autonomous Tech Town Controller")
    parser.add_argument("--init", action="store_true", help="Generate initial 320 citizens, 8 companies, and sovereign town foundation")
    parser.add_argument("--tick", type=int, nargs="?", const=1, help="Execute N simulation ticks (default 1)")
    parser.add_argument("--continuous", action="store_true", help="Run 24/7 continuous simulation loop")
    parser.add_argument("--delay", type=float, default=3.0, help="Seconds between continuous ticks (default 3.0)")
    parser.add_argument("--command", type=str, help="Issue a direct user command or question to the town agents")
    parser.add_argument("--agent", type=str, default=None, help="Target specific agent by ID or Name for directive")
    parser.add_argument("--git-commit", action="store_true", help="Automatically git commit town changes")
    parser.add_argument("--serve", action="store_true", help="Serve the 3D Tech Town Viewer locally")
    parser.add_argument("--port", type=int, default=8000, help="Web server port (default 8000)")

    args = parser.parse_args()
    engine = TownEngine()

    if args.init:
        print("🏛️  Generating foundational Sovereign Country of Tech Town, 320 pioneer citizens across 120+ professions, and 8 enterprises...")
        state = generate_initial_state()
        engine.state = state
        engine.save_state()
        print(f"✅ Generated {len(state.agents)} citizens, {len(state.companies)} companies, {len(state.buildings)} buildings, {len(state.roads)} roads, {len(state.vehicles)} vehicles!")
        if args.git_commit:
            msg = commit_town_activity(state.recent_events, state.tick)
            if msg:
                print(f"📦 Git commit created: {msg}")
        return

    if args.command:
        engine.load_state()
        target = args.agent or "agent-001"
        print(f"👑 [OPERATOR L5 DIRECTIVE] -> Target: '{target}' | Order: '{args.command}'...")
        res = engine.process_agent_order(target, args.command)
        print(f"💬 [{res.get('agent_name', target)} ({res.get('career_title', '')})]: \"{res.get('reply')}\"")
        if args.git_commit:
            msg = commit_town_activity(engine.state.recent_events, engine.state.tick)
            if msg:
                print(f"📦 Git commit: {msg}")
        print("✅ Order executed and recorded to state and diaries.")
        return

    if args.serve and not (args.tick or args.continuous):
        serve_web(port=args.port)
        return

    if args.serve and args.continuous:
        t = threading.Thread(target=serve_web, args=(args.port,), daemon=True)
        t.start()

    if args.continuous:
        print(f"⚙️  Starting 24/7 Autonomous Tech Town loop (Interval: {args.delay}s)...")
        engine.load_state()
        try:
            while True:
                state = engine.tick()
                latest_event = state.recent_events[-1]["message"] if state.recent_events else "Cycle complete"
                print(f"[Tick {state.tick}] Pop: {len(state.agents)} | Corps: {len(state.companies)} | Bldgs: {len(state.buildings)} | {latest_event}")
                if args.git_commit:
                    commit_town_activity(state.recent_events, state.tick)
                time.sleep(args.delay)
        except KeyboardInterrupt:
            print("\n🛑 Town simulation paused by user.")
        return

    if args.tick is not None:
        engine.load_state()
        num_ticks = max(1, args.tick)
        print(f"⚙️  Executing {num_ticks} simulation tick(s)...")
        for _ in range(num_ticks):
            state = engine.tick()
            latest_event = state.recent_events[-1]["message"] if state.recent_events else "Cycle complete"
            print(f"[Tick {state.tick}] Pop: {len(state.agents)} | Corps: {len(state.companies)} | Bldgs: {len(state.buildings)} | {latest_event}")
        
        if args.git_commit:
            msg = commit_town_activity(state.recent_events, state.tick)
            if msg:
                print(f"📦 Git commit: {msg}")
        print("✅ Simulation tick(s) finished.")
        return

    # Default action
    if not os.path.exists("state/town_state.json"):
        print("Initializing new Tech Town with 200 agents...")
        state = generate_initial_state()
        engine.state = state
        engine.save_state()
        print(f"✅ Town initialized with 200 agents and companies.")
    else:
        engine.load_state()
        state = engine.tick()
        print(f"Tick {state.tick} executed. Population: {len(state.agents)}. Run with --help for options.")

if __name__ == "__main__":
    main()
