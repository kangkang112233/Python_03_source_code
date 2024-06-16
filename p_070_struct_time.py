import time

# Get the current time in seconds since the Epoch
current_time_seconds = time.time()
print(f"Current time in seconds since the Epoch: {current_time_seconds}")

# Convert the current time to a struct_time object in UTC
current_time_utc = time.gmtime(current_time_seconds)
print(f"Current time in UTC: {time.strftime('%Y-%m-%d %H:%M:%S', current_time_utc)}")

# Convert the current time to a struct_time object in local time
current_time_local = time.localtime(current_time_seconds)
print(
    f"Current time in local time: {time.strftime('%Y-%m-%d %H:%M:%S', current_time_local)}"
)

# Accessing elements of struct_time
year = current_time_local.tm_year
month = current_time_local.tm_mon
day = current_time_local.tm_mday
hour = current_time_local.tm_hour
minute = current_time_local.tm_min
second = current_time_local.tm_sec
print(
    f"Local Time - Year: {year}, Month: {month}, Day: {day}, Hour: {hour}, Minute: {minute}, Second: {second}"
)
