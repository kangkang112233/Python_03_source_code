import contextlib
import os

# Example 1: Suppress FileNotFoundError when attempting to remove a file
file_path = "non_existent_file.txt"
with contextlib.suppress(FileNotFoundError):
    os.remove(file_path)

print(f"Tried to remove {file_path}, but no error was raised.")

# Example 2: Suppress multiple exceptions
#  (FileNotFoundError and PermissionError)
file_path = "another_non_existent_file.txt"
with contextlib.suppress(FileNotFoundError, PermissionError):
    os.remove(file_path)

print(
    f"Tried to remove {file_path} with multiple exception suppression,"
    "but no error was raised."
)
