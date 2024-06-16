import sys

# List comprehension
list_comp = [i for i in range(10000000)]

# Generator expression
gen_expr = (i for i in range(10000000))

# Print sizes
print(f"Size of list comprehension: {sys.getsizeof(list_comp)} bytes")
print(f"Size of generator expression: {sys.getsizeof(gen_expr)} bytes")
