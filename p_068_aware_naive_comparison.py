from datetime import datetime, timezone, timedelta

# Create naive datetime object
naive_datetime = datetime(2024, 6, 15, 12, 0)
print(f"Naive datetime: {naive_datetime}")

# Create aware datetime object
aware_datetime = datetime(
    2024, 6, 15, 12, 0, tzinfo=timezone(timedelta(hours=9))
)  # JST (UTC+9)
print(f"Aware datetime: {aware_datetime}")

# Compare naive and aware datetime objects directly
try:
    comparison_equal = naive_datetime == aware_datetime
    print(f"Direct equality comparison result: {comparison_equal}")
except TypeError as e:
    print(f"Error in direct equality comparison: {e}")

try:
    comparison_greater = naive_datetime > aware_datetime
    print(f"Direct greater-than comparison result: {comparison_greater}")
except TypeError as e:
    print(f"Error in direct greater-than comparison: {e}")

try:
    difference = naive_datetime - aware_datetime
    print(f"Direct subtraction result: {difference}")
except TypeError as e:
    print(f"Error in direct subtraction: {e}")

# Convert naive datetime to aware datetime (assuming UTC for conversion)
naive_as_aware = naive_datetime.replace(tzinfo=timezone.utc)
print(f"Naive as aware (UTC): {naive_as_aware}")

# Compare aware datetime objects
comparison_equal_converted = naive_as_aware == aware_datetime
print(f"Equality comparison after conversion: {comparison_equal_converted}")

comparison_greater_converted = naive_as_aware > aware_datetime
print(f"Greater-than comparison after conversion: {comparison_greater_converted}")

difference_converted = naive_as_aware - aware_datetime
print(f"Subtraction result after conversion: {difference_converted}")
