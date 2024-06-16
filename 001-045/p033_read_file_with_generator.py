# Example to demonstrate reading a file with a generator in a log processing system


def read_large_file(file_path):
    """Generator function to read a file line by line."""
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()


# Usage of the generator function
def process_log_file(file_path):
    log_lines = read_large_file(file_path)
    for line in log_lines:
        print(f"Processed Log Line: {line}")


# Assuming 'large_log_file.txt' is a large file in the current directory
process_log_file("example.txt")
