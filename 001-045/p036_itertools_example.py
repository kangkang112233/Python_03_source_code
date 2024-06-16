import itertools


# Example 1: Infinite iterator
def generate_student_ids(start_id=1):
    """Generate an infinite sequence of student IDs starting from start_id."""
    for student_id in itertools.count(start_id):
        yield student_id


# Example 2: Finite iterator
students = ["Alice", "Bob", "Charlie", "tom"]
student_ids = list(itertools.islice(generate_student_ids(), len(students)))

# Example 3: Combinatoric iterators
pairs = list(itertools.combinations(students, 2))

# Print results
print(f"Student IDs: {student_ids}")
print(f"Student Pairs: {pairs}")
