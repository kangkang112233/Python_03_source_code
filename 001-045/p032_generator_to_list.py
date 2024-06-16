# Example to demonstrate converting a generator object to a list in a student ID generation system


def student_id_generator(start_id=1):
    """Generator function to generate unique student IDs."""
    current_id = start_id
    while current_id < start_id + 1000000:
        yield current_id
        current_id += 1


# Create a generator object
id_gen = student_id_generator()

# Convert the generator object to a list
id_list = list(id_gen)

# Print the list of student IDs
print("List of Generated Student IDs:", id_list)
