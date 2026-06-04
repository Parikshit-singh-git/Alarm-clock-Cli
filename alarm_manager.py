from datetime import datetime, timedelta
from alarm_model import Alarm
from alarm_store import load_alarms, save_alarms

def add_alarm(time_str: str, label: str) -> Alarm:
    try:
        alarm_time = datetime.strptime(time_str, "%H:%M")
    except ValueError:
        raise ValueError(f"Invalid time format '{time_str}'. Use HH:MM.")

    now = datetime.now()
    scheduled = now.replace(
        hour=alarm_time.hour,
        minute=alarm_time.minute,
        second=0,
        microsecond=0
    )

    # Past-time decision: schedule for next day, not an error
    if scheduled <= now:
        scheduled += timedelta(days=1)

    alarm = Alarm(time=scheduled.strftime("%H:%M"), label=label)
    alarms = load_alarms()
    alarms.append(alarm)
    save_alarms(alarms)
    return alarm

def list_alarms() -> list[Alarm]:
    return [a for a in load_alarms() if a.active]

def cancel_alarm(alarm_id: str) -> bool:
    alarms = load_alarms()
    for alarm in alarms:
        if alarm.id.startswith(alarm_id):
            alarm.active = False
            save_alarms(alarms)
            return True
    return False

def check_and_fire(alarms: list[Alarm], now: str = None) -> list[Alarm]:
    if now is None:
        now = datetime.now().strftime("%H:%M")
    fired = []
    for alarm in alarms:
        if alarm.active and alarm.time == now:
            alarm.active = False
            fired.append(alarm)
    return fired