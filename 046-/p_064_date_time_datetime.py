from datetime import date, time, datetime

# Use date for handling just dates
borrow_date = date(2024, 6, 15)
print(f"Borrow Date: {borrow_date}")

# Use time for handling just times
borrow_time = time(14, 30)
print(f"Borrow Time: {borrow_time}")

# Use datetime for handling both dates and times
borrow_datetime = datetime(2024, 6, 15, 14, 30)
print(f"Borrow Datetime: {borrow_datetime}")


# Example function to decide which type to use
def log_borrowing(book_title, borrow_datetime):
    # Use datetime for a comprehensive log entry
    print(f"Book '{book_title}' was borrowed on {borrow_datetime}")


# Logging a book borrowing event
log_borrowing("Python Programming", borrow_datetime)
