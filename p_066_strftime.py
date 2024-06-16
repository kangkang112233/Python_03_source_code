from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Format the date and time in different ways using strftime
formatted_datetime_1 = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
formatted_datetime_2 = current_datetime.strftime("%d/%m/%Y %I:%M %p")
formatted_datetime_3 = current_datetime.strftime("%A, %B %d, %Y")

# Print the formatted date and time
print(f"Formatted datetime (YYYY-MM-DD HH:MM:SS): {formatted_datetime_1}")
print(f"Formatted datetime (DD/MM/YYYY HH:MM AM/PM): {formatted_datetime_2}")
print(f"Formatted datetime (Weekday, Month Day, Year): {formatted_datetime_3}")
