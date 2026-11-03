#!/usr/bin/env bash
# Quick launcher for GitHub Autonomous Tech Town
# Starts the local web server and autonomous simulation loop at http://localhost:8000
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

echo "=========================================================="
echo "🏙️  Starting Sovereign Country of Tech Town..."
echo "🌐 3D Live Viewer: http://localhost:8000"
echo "🤖 Autonomous Agents & 24/7 Engine: Active"
echo "=========================================================="

python3 run_town.py --port 8000
