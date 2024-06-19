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

# Format the current local time as a human-readable string
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time_local)
print(f"Formatted local time: {formatted_time}")
