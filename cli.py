import typer
from alarm_manager import add_alarm, list_alarms, cancel_alarm
from scheduler import run_loop

app = typer.Typer(help="Python CLI Alarm Clock")

@app.command()
def add(
    time: str = typer.Argument(..., help="Alarm time in HH:MM format"),
    label: str = typer.Argument("Alarm", help="Label for the alarm")
):
    """Add a new alarm."""
    try:
        alarm = add_alarm(time, label)
        print(f" Alarm set — [{alarm.id}] {alarm.time} '{alarm.label}'")
    except ValueError as e:
        print(f" {e}")
        raise typer.Exit(1)

@app.command()
def list():
    """List all active alarms."""
    alarms = list_alarms()
    if not alarms:
        print("No active alarms.")
        return
    for alarm in alarms:
        print(f"  [{alarm.id}]  {alarm.time}  —  {alarm.label}")

@app.command()
def cancel(alarm_id: str = typer.Argument(..., help="Alarm ID to cancel")):
    """Cancel an alarm by ID."""
    if cancel_alarm(alarm_id):
        print(f" Alarm {alarm_id} cancelled.")
    else:
        print(f" No alarm found with ID '{alarm_id}'.")
        raise typer.Exit(1)

@app.command()
def run():
    """Start the alarm daemon."""
    run_loop()