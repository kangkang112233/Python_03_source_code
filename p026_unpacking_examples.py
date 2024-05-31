# Example of Unpacking
# In this example, we demonstrate how to unpack elements from a tuple, list, and dictionary.

# Unpacking a tuple
tuple_example = (1, 2, 3)
a, b, c = tuple_example
print(f"Tuple unpacking: a={a}, b={b}, c={c}")

# Unpacking a list
list_example = [4, 5, 6]
d, e, f = list_example
print(f"List unpacking: d={d}, e={e}, f={f}")

# Unpacking a dictionary
dict_example = {"key1": 7, "key2": 8, "key3": 9}
g, h, i = dict_example.values()
print(f"Dictionary unpacking: g={g}, h={h}, i={i}")

# Additional Example: Ignoring Values
_, j, _ = list_example  # Only unpack the second element, ignoring the first and third
print(f"Ignoring values: j={j}")

# Additional Example: Unpacking with * (rest operator)
k, *rest = list_example  # k gets the first element, rest gets the remaining
print(f"Unpacking with rest operator: k={k}, rest={rest}")
