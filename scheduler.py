import time
from alarm_manager import check_and_fire
from alarm_store import load_alarms, save_alarms

# FUTURE: Replace sleep loop with asyncio or APScheduler for non-blocking behavior

def run_loop() -> None:
    print("Alarm clock running... Press Ctrl+C to stop.")
    try:
        while True:
            alarms = load_alarms()
            fired = check_and_fire(alarms)
            if fired:
                save_alarms(alarms)
                for alarm in fired:
                    print(f"\a ALARM: {alarm.label} ({alarm.time})")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nAlarm clock stopped.")