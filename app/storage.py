
import json
from pathlib import Path

# Locate the project's data/tasks.json file
DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "tasks.json"


def load_tasks():
    """Load tasks from the JSON file."""

    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks):
    """Save tasks into the JSON file."""

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)
