from datetime import datetime
from dateutil.relativedelta import relativedelta

# Current date
current_date = datetime.now()
print(f"Current date: {current_date}")

# Adding 1 month to the current date
one_month_later = current_date + relativedelta(months=1)
print(f"One month later: {one_month_later}")

# Subtracting 1 year from the current date
one_year_ago = current_date - relativedelta(years=1)
print(f"One year ago: {one_year_ago}")

# Adding 10 days and subtracting 2 months
custom_delta = current_date + relativedelta(days=10) - relativedelta(months=2)
print(f"10 days later and 2 months earlier: {custom_delta}")

# Example: Calculate due date for a book borrowed for 3 weeks
borrow_date = datetime(2024, 6, 15)
borrowing_period = relativedelta(weeks=3)
due_date = borrow_date + borrowing_period
print(f"Book borrowed on: {borrow_date}")
print(f"Due date: {due_date}")
