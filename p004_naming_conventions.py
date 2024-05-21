# Variable and function naming (snake_case)
def calculate_sum(a, b):
    total_sum = a + b  # Variable in snake_case
    return total_sum


# Class naming (CamelCase)
class MathOperations:
    def multiply(self, x, y):
        return x * y


# Constant naming (UPPERCASE with underscores)
MAX_LIMIT = 100

# Module and package naming should be in lowercase (example in comments)
# mymodule.py
# mypackage

# Usage examples
result = calculate_sum(5, 3)
print("Sum:", result)

math_ops = MathOperations()
product = math_ops.multiply(4, 6)
print("Product:", product)
print("Max Limit:", MAX_LIMIT)
