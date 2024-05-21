import contextlib
import io

# Create a string buffer to capture the output
buffer = io.StringIO()

# Use contextlib.redirect_stdout to redirect print statements to the buffer
with contextlib.redirect_stdout(buffer):
    print("This will be captured in the buffer.")
    print("Hello, world!")

# Get the content of the buffer
captured_output = buffer.getvalue()
print("Captured Output:", captured_output)

# Write the captured output to a file
with open("output.txt", "w") as f:
    with contextlib.redirect_stdout(f):
        print("This will be written to the file instead of the console.")
