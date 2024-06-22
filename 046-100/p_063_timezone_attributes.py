from datetime import datetime, timezone, timedelta

# Create a datetime object with timezone information
dt_with_tz = datetime(
    2024, 6, 15, 12, 0, tzinfo=timezone(timedelta(hours=9))
)  # JST (UTC+9)

# Get the timezone name
tz_name = dt_with_tz.tzname()
print(f"Timezone name: {tz_name}")

# Get the tzinfo object
tz_info = dt_with_tz.tzinfo
print(f"Timezone info: {tz_info}")

# Create a datetime object with fold attribute to handle ambiguous times
dt_with_fold = datetime(
    2024, 11, 1, 1, 30, fold=1, tzinfo=timezone(timedelta(hours=9))
)  # Example with fold
fold_value = dt_with_fold.fold
print(f"Fold value: {fold_value}")
