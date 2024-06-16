# Define a custom context manager
class CustomContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")
        if exc_type is not None:
            print(f"An exception occurred: {exc_type} - {exc_val}")
        return True  # Suppress the exception


# Use the custom context manager with 'with' statement
with CustomContextManager() as manager:
    print("Inside the context")
    # Uncomment the next line to test exception handling
    # raise ValueError("An example exception")

# Use the built-in context manager for file operations
with open("example.txt", "w") as file:
    file.write("Hello, world2114!")
