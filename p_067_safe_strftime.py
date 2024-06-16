from datetime import datetime


# Function to format the current date and time safely
def safe_strftime(date_time, format_string):
    try:
        return date_time.strftime(format_string)
    except ValueError as e:
        return f"Error: {e}"


# Get the current date and time
current_datetime = datetime.now()

# Correct format
correct_format = "%Y-%m-%d %H:%M:%S"
formatted_datetime = safe_strftime(current_datetime, correct_format)
print(f"Formatted datetime (correct): {formatted_datetime}")

# Incorrect format
incorrect_format = "%Y-%m-%d %X %Q"
formatted_datetime = safe_strftime(current_datetime, incorrect_format)
print(f"Formatted datetime (incorrect): {formatted_datetime}")
