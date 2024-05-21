def divide(x, y):
    try:
        result = x / y
    except (ZeroDivisionError, TypeError):
        print("Error: Division by zero or invalid type.")
    else:
        print("Result:", result)


# Call the function with different parameters to see the exception handling
divide(10, 2)  # This should print the result
divide(10, 0)  # This should print the error message for ZeroDivisionError
divide(10, "a")  # This should print the error message for TypeError
