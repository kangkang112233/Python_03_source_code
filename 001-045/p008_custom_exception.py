class CustomError(Exception):
    """A custom exception class."""

    def __init__(self, message):
        self.message = message


def divide(x, y):
    if y == 0:
        raise CustomError("Division by zero is not allowed000.")
    return x / y


try:
    result = divide(10, 0)
except CustomError as e:
    print(f"CustomError: {e.message}")
else:
    print("Result:", result)

# Call the function with a valid input
try:
    result = divide(10, 2)
    print("Result:", result)
except CustomError as e:
    print(f"CustomError: {e.message}")
