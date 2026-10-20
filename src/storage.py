
import json
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent / "tasks.json"


def save_tasks(tasks):
    DATA_FILE.write_text(
        json.dumps(tasks, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def load_tasks():
    if not DATA_FILE.exists():
        return []

    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []
