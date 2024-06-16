from datetime import datetime
from dateutil.rrule import rrule, DAILY, WEEKLY, MONTHLY

# Generate a list of daily events starting from a specific date
start_date = datetime(2024, 1, 1)
daily_events = list(rrule(DAILY, count=10, dtstart=start_date))
print("Daily events:")
for event in daily_events:
    print(event)

# Generate a list of weekly events on Mondays
weekly_events = list(
    rrule(WEEKLY, count=10, byweekday=0, dtstart=start_date)
)  # 0=Monday
print("\nWeekly events on Mondays:")
for event in weekly_events:
    print(event)

# Generate a list of monthly events on the first day of each month
monthly_events = list(rrule(MONTHLY, count=10, bymonthday=1, dtstart=start_date))
print("\nMonthly events on the 1st day of each month:")
for event in monthly_events:
    print(event)
