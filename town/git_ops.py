"""
Git Operations for GitHub Autonomous Tech Town.
Enables agents to autonomously commit their work directly into the repository.
"""
import subprocess
import os
from typing import Optional, List, Dict, Any

def run_git(args: List[str]) -> subprocess.CompletedProcess:
    return subprocess.run(["git"] + args, capture_output=True, text=True)

def commit_town_activity(events: List[Dict[str, Any]], tick: int) -> Optional[str]:
    """Stages town changes and creates an agent-attributed commit."""
    # Ensure git user config exists if not already set (e.g. in GitHub Actions)
    check_user = run_git(["config", "user.name"])
    if not check_user.stdout.strip():
        run_git(["config", "user.name", "GitHub Tech Town Bot"])
        run_git(["config", "user.email", "agent-town@github.local"])

    # Stage files
    paths_to_stage = ["state", "docs/data", "buildings", "projects", "diaries", "companies", "commands"]
    for path in paths_to_stage:
        if os.path.exists(path):
            run_git(["add", path])

    # Check status
    status = run_git(["status", "--porcelain"])
    if not status.stdout.strip():
        return None  # No changes to commit

    # Craft commit message from latest events
    if events:
        latest = events[-1]
        msg = f"town(tick-{tick}): {latest.get('message', 'Autonomous city cycle')}"
    else:
        msg = f"town(tick-{tick}): Autonomous life cycle update"

    commit_res = run_git(["commit", "-m", msg])
    if commit_res.returncode == 0:
        return msg
    return None
