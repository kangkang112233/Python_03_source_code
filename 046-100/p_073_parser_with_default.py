from datetime import datetime
from dateutil import parser


# Function to parse a date string into a datetime object with a default time
def parse_date_with_default(date_string, default_datetime):
    try:
        parsed_date = parser.parse(date_string, default=default_datetime)
        return parsed_date
    except ValueError as e:
        print(f"Error parsing date: {e}")
        return None


# Example date strings
date_string_1 = "2024-06-15"
date_string_2 = "June 15, 2024"
date_string_3 = "15/06/2024"

# Default datetime to use for missing time information
default_time = datetime(2024, 1, 1, 9, 0, 0)  # Default to 09:00:00 on any date

# Parse the date strings with the default time
parsed_date_1 = parse_date_with_default(date_string_1, default_time)
parsed_date_2 = parse_date_with_default(date_string_2, default_time)
parsed_date_3 = parse_date_with_default(date_string_3, default_time)

# Print the parsed dates
print(f"Parsed date 1: {parsed_date_1}")
print(f"Parsed date 2: {parsed_date_2}")
print(f"Parsed date 3: {parsed_date_3}")
