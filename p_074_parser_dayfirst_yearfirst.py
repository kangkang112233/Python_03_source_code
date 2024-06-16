from dateutil import parser


# Function to parse a date string into a datetime object with dayfirst and yearfirst options
def parse_date_with_options(date_string, dayfirst=False, yearfirst=False):
    try:
        parsed_date = parser.parse(date_string, dayfirst=dayfirst, yearfirst=yearfirst)
        return parsed_date
    except ValueError as e:
        print(f"Error parsing date: {e}")
        return None


# Example date strings
date_string_1 = "12/06/2024"  # Ambiguous date format
date_string_2 = "2024/06/12"  # ISO format but can be misinterpreted in some locales
date_string_3 = "06/12/2024"  # US format

# Parse the date strings with different options
parsed_date_1 = parse_date_with_options(date_string_1, dayfirst=True)
parsed_date_2 = parse_date_with_options(date_string_2, yearfirst=True)
parsed_date_3 = parse_date_with_options(date_string_3)

# Print the parsed dates
print(f"Parsed date 1 with dayfirst=True: {parsed_date_1}")
print(f"Parsed date 2 with yearfirst=True: {parsed_date_2}")
print(f"Parsed date 3 with default options: {parsed_date_3}")
