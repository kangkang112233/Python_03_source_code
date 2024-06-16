from dateutil import parser


# Function to parse a date string into a datetime object
def parse_date(date_string):
    try:
        parsed_date = parser.parse(date_string)
        return parsed_date
    except ValueError as e:
        print(f"Error parsing date: {e}")
        return None


# Example date strings
date_string_1 = "2024-06-15 10:00:00"
date_string_2 = "June 15, 2024 10:00AM"
date_string_3 = "15/06/2024 10:00"

# Parse the date strings
parsed_date_1 = parse_date(date_string_1)
parsed_date_2 = parse_date(date_string_2)
parsed_date_3 = parse_date(date_string_3)

# Print the parsed dates
print(f"Parsed date 1: {parsed_date_1}")
print(f"Parsed date 2: {parsed_date_2}")
print(f"Parsed date 3: {parsed_date_3}")
