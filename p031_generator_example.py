# Example to demonstrate generators in a student ID generation system


def student_id_generator(start_id=1):
    """Generator function to generate unique student IDs."""
    current_id = start_id
    while True:
        yield current_id
        current_id += 1


# Create a generator object
id_gen = student_id_generator()

# Generate and print the first 10 student IDs
for _ in range(10):
    student_id = next(id_gen)
    print(f"Generated Student ID: {student_id}")
