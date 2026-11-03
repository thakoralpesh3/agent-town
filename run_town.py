#!/usr/bin/env python3
"""
GitHub Autonomous Tech Town - Main Controller CLI
Allows running ticks, 24/7 daemon loop, initializing town, serving the 3D viewer, and executing user commands.
"""
import argparse
import sys
import os
import time
import json
import http.server
import threading
from typing import Optional
from town.simulation import TownEngine
from town.generator import generate_initial_state
from town.git_ops import commit_town_activity

def serve_web(port: int = 8000, directory: str = "docs", engine: Optional[TownEngine] = None, auto_commit: bool = False):
    """Serves the 3D Tech Town WebGL viewer with live API endpoint for operator orders."""
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)

        def log_message(self, format, *args):
            # Suppress noisy HTTP asset logs
            pass

        def do_POST(self):
            if self.path == "/api/command" and engine:
                content_length = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(content_length).decode("utf-8") if content_length > 0 else "{}"
                try:
                    data = json.loads(body)
                    cmd = data.get("command", "")
                    agent_id = data.get("agent_id") or "agent-001"
                    res = engine.process_agent_order(agent_id, cmd)
                    engine.save_state()
                    if auto_commit:
                        commit_town_activity(engine.state.recent_events, engine.state.tick)
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(res).encode("utf-8"))
                except Exception as e:
                    self.send_response(500)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
            elif self.path == "/api/tick" and engine:
                state = engine.tick()
                if auto_commit:
                    commit_town_activity(state.recent_events, state.tick)
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"tick": state.tick, "population": len(state.agents)}).encode("utf-8"))
            else:
                self.send_response(404)
                self.end_headers()

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
    parser.add_argument("--no-sim", action="store_true", help="Disable the background simulation engine loop when serving")

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

    # Serve locally (default behavior or when --serve is passed)
    if not os.path.exists("state/town_state.json"):
        print("🏛️  Initializing new Tech Town foundation...")
        state = generate_initial_state()
        engine.state = state
        engine.save_state()
    else:
        engine.load_state()

    def run_sim_loop():
        while True:
            try:
                state = engine.tick()
                if args.git_commit:
                    commit_town_activity(state.recent_events, state.tick)
            except Exception as e:
                print(f"[Sim Error] {e}")
            time.sleep(args.delay)

    if not args.no_sim:
        sim_thread = threading.Thread(target=run_sim_loop, daemon=True)
        sim_thread.start()
        print(f"🤖 Autonomous simulation engine running (interval: {args.delay}s).")

    serve_web(port=args.port, engine=engine, auto_commit=args.git_commit)

if __name__ == "__main__":
    main()
