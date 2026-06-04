import json
import os
from alarm_model import Alarm

ALARMS_FILE = "alarms.json"

def load_alarms() -> list[Alarm]:
    if not os.path.exists(ALARMS_FILE):
        return []
    try:
        with open(ALARMS_FILE, "r") as f:
            data = json.load(f)
            return [Alarm.from_dict(item) for item in data]
    except (json.JSONDecodeError, KeyError, TypeError) as e:
        print(f"Warning: could not load alarms ({e}). Starting fresh.")
        return []

def save_alarms(alarms: list[Alarm]) -> None:
    with open(ALARMS_FILE, "w") as f:
        json.dump([alarm.to_dict() for alarm in alarms], f, indent=2)