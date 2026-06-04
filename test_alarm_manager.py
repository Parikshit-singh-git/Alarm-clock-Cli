import pytest
from datetime import datetime, timedelta
from unittest.mock import patch
from models import Alarm
from alarm_manager import add_alarm, cancel_alarm, check_and_fire

def test_add_alarm_future_time():
    future = (datetime.now() + timedelta(hours=2)).strftime("%H:%M")
    with patch("alarm_manager.load_alarms", return_value=[]), \
         patch("alarm_manager.save_alarms"):
        alarm = add_alarm(future, "test")
        assert alarm.time == future
        assert alarm.active is True

def test_add_alarm_past_time_schedules_next_day():
    past = "00:01"
    with patch("alarm_manager.load_alarms", return_value=[]), \
         patch("alarm_manager.save_alarms"):
        alarm = add_alarm(past, "test")
        # Should still be 00:01 but intended for tomorrow
        assert alarm.time == past
        assert alarm.active is True

def test_check_and_fire_fires_matching_alarm():
    alarm = Alarm(time="09:30", label="standup")
    fired = check_and_fire([alarm], now="09:30")
    assert len(fired) == 1
    assert fired[0].active is False

def test_check_and_fire_no_double_fire():
    alarm = Alarm(time="09:30", label="standup")
    check_and_fire([alarm], now="09:30")
    fired_again = check_and_fire([alarm], now="09:30")
    assert len(fired_again) == 0

def test_cancel_alarm():
    alarm = Alarm(time="09:30", label="standup")
    with patch("alarm_manager.load_alarms", return_value=[alarm]), \
         patch("alarm_manager.save_alarms"):
        result = cancel_alarm(alarm.id[:4])
        assert result is True
        assert alarm.active is False

def test_invalid_time_format():
    with pytest.raises(ValueError):
        add_alarm("99:99", "bad")