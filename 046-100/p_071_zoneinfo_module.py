from datetime import datetime, timedelta
import pytz

# Get the current time in UTC
current_time_utc = datetime.now(pytz.utc)
print(f"Current time in UTC: {current_time_utc}")

# Convert UTC time to a different time zone (e.g., Asia/Tokyo)
tokyo_tz = pytz.timezone("Asia/Tokyo")
current_time_tokyo = current_time_utc.astimezone(tokyo_tz)
print(f"Current time in Tokyo: {current_time_tokyo}")

# Convert UTC time to another time zone (e.g., America/New_York)
ny_tz = pytz.timezone("America/New_York")
current_time_ny = current_time_utc.astimezone(ny_tz)
print(f"Current time in New York: {current_time_ny}")

# Example: Calculate due date for a book borrowed in Tokyo time
borrow_date_tokyo = datetime(2024, 6, 15, 10, 0, tzinfo=tokyo_tz)
borrowing_period = timedelta(days=14)
due_date_tokyo = borrow_date_tokyo + borrowing_period
print(f"Book borrowed in Tokyo on: {borrow_date_tokyo}")
print(f"Due date in Tokyo time: {due_date_tokyo}")

# Convert the due date to UTC
due_date_utc = due_date_tokyo.astimezone(pytz.utc)
print(f"Due date in UTC: {due_date_utc}")
