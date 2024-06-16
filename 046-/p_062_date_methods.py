from datetime import date

# Get the current date
current_date = date.today()
print(f"Today's date: {current_date}")

# Get the weekday (0=Monday, 6=Sunday)
weekday = current_date.weekday()
print(f"Weekday (0=Mon, 6=Sun): {weekday}")

# Get the ISO weekday (1=Monday, 7=Sunday)
iso_weekday = current_date.isoweekday()
print(f"ISO Weekday (1=Mon, 7=Sun): {iso_weekday}")

# Get the date in ISO format
iso_format_date = current_date.isoformat()
print(f"ISO format date: {iso_format_date}")

# Create a date object from an ISO format string
date_from_iso = date.fromisoformat(iso_format_date)
print(f"Date from ISO format: {date_from_iso}")

# Format the date using strftime
formatted_date = current_date.strftime("%Y-%m-%d")
print(f"Formatted date: {formatted_date}")

# Get the year, month, and day
year = current_date.year
month = current_date.month
day = current_date.day
print(f"Year: {year}, Month: {month}, Day: {day}")
