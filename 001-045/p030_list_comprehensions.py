# Example to demonstrate list comprehensions in a student grade system

# List of student names
students = ["Alice", "Bob", "Charlie", "David"]

# Assign grades to students based on their position in the list
# Example: Assign a grade based on the index (e.g., index * 10)
grades = [index * 10 for index, student in enumerate(students, start=1)]

# Print student grades
for student, grade in zip(students, grades):
    print(f"Student: {student}, Grade: {grade}")
