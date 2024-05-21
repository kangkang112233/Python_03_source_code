import contextlib


# Define a custom context manager using contextlib.contextmanager
@contextlib.contextmanager
def custom_context_manager():
    print("Entering the context")
    try:
        yield
    finally:
        print("Exiting the context")


# Use the custom context manager with 'with' statement
with custom_context_manager():
    print("Inside the context")
    # Uncomment the next line to test exception handling
    # raise ValueError("An example exception")


# Use contextlib.contextmanager for file operations
@contextlib.contextmanager
def open_file(file, mode):
    f = open(file, mode)
    try:
        yield f
    finally:
        f.close()


# Use the file context manager
with open_file("example.txt", "w") as file:
    file.write("Hello, world!")
