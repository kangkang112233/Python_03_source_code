import sys

# Define different types of objects
list_obj = [i for i in range(100)]
dict_obj = {i: i * 2 for i in range(100)}
str_obj = "a" * 100
gen_expr = (i for i in range(100))

# Get the size of each object
list_size = sys.getsizeof(list_obj)
dict_size = sys.getsizeof(dict_obj)
str_size = sys.getsizeof(str_obj)
gen_size = sys.getsizeof(gen_expr)

# Print sizes
print(f"Size of list object: {list_size} bytes")
print(f"Size of dict object: {dict_size} bytes")
print(f"Size of string object: {str_size} bytes")
print(f"Size of generator expression: {gen_size} bytes")
print(str_obj)

for i in range(20):
    print(i * "*")
    i = i + 1
