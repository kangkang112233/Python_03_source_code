def divide(x, y):
    try:
        result = x / y
    except Exception as e:
        # Catch all exceptions using the base class Exception
        print(f"Error: {type(e).__name__} - {e}")
    else:
        print("Result:", result)  # This is executed if no exceptions occur


# Call the function with different parameters to see the exception handling
divide(10, 2)  # This should print the result
divide(10, 0)  # This should print the error message for ZeroDivisionError
divide(10, "a")  # This should print the error message for TypeError
