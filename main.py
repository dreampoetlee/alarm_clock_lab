# As a developer, I want to import the AlarmClock class into main.py so I can instantiate it as a new AlarmClock object and call methods on it.
from tkinter import W
from clockAlarm import AlarmClock

work_clock = AlarmClock(1330, False, 440)
# # 1. Print the clock’s time to the terminal
# work_clock.what_time_is_it()
# 2. Call the alarm clock’s change current time method to change the current time
work_clock.set_alarm()
# 3. Toggle the alarm clock’s on off switch
alarm_switch = work_clock.status_of_alarm
not work_clock.status_of_alarm()
