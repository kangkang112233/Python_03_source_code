from enum import Enum, unique


@unique
class Status(Enum):
    SUCCESS = 1
    ERROR = 2
    PENDING = 3


# Function to display status message
def display_status(status):
    if status == Status.SUCCESS:
        print("Operation was successful.")
    elif status == Status.ERROR:
        print("An error occurred.")
    elif status == Status.PENDING:
        print("Operation is pending.")
    else:
        print("Unknown status.")


# Using the enumeration
display_status(Status.SUCCESS)
display_status(Status.ERROR)
