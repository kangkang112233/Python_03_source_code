from datetime import datetime, timedelta

# Define a borrowing period of 14 days
borrowing_period = timedelta(days=14)

# Record the current date and time when the book is borrowed
borrow_date = datetime.now()
print(f"Borrow Date: {borrow_date}")

# Calculate the due date by adding the borrowing period to the borrow date
due_date = borrow_date + borrowing_period
print(f"Due Date: {due_date}")


# Function to check if a book is overdue
def is_overdue(return_date, due_date):
    return return_date > due_date


# Example return date
return_date = borrow_date + timedelta(days=16)
print(f"Return Date: {return_date}")

# Check if the book is overdue
overdue = is_overdue(return_date, due_date)
print(f"Is the book overdue? {'Yes' if overdue else 'No'}")
