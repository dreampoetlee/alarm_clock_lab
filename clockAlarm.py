# Alarm Clock Lab

# As a developer, I want to use Python’s proper snake_case for variable names.

# As a developer, I want to create a AlarmClock class.
class AlarmClock:
  def __init__(self, current_time, is_on, set_time) :
    # Instance variable to keep track of current time
    self.current_time = current_time
    # Instance variable for if alarm is on or off
    self.is_on = is_on
    # Instance variable for if alarm is set
    self.set_time = set_time

# As a developer, I want the AlarmClock class to have a method to set (or change) the current time and print to the console the current time.
  def what_time_is_it(self) :
    self.current_time = input('Please enter the current time. ')
    print(f'The current time is {self.current_time}')

# As a developer, I want the AlarmClock class to have a method to toggle the alarm on or off.
  def status_of_alarm(self) :
    self.is_on = True

# As a developer, I want the AlarmClock class to have a method to set the current alarm time and print to the console the current alarm time.
  def set_alarm(self) :
    self.set_time = input('Please enter the time that you want the alarm set to. ')
    print(f'You have set the alarm for {self.set_time}')