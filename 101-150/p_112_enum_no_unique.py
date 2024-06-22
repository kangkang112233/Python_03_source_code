from enum import Enum


class ErrorType(Enum):
    NETWORK_ERROR = 1
    TIMEOUT_ERROR = 1
    SERVER_ERROR = 2


# Function to display error message
def display_error(error_type):
    if error_type == ErrorType.NETWORK_ERROR:
        print("Network error occurred.")
    elif error_type == ErrorType.TIMEOUT_ERROR:
        print("Timeout error occurred.")
    elif error_type == ErrorType.SERVER_ERROR:
        print("Server error occurred.")
    else:
        print("Unknown error.")


# Using the enumeration
display_error(ErrorType.NETWORK_ERROR)
display_error(ErrorType.TIMEOUT_ERROR)
