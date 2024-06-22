from itertools import permutations, product

# 日本語の説明:
# `permutations` 関数は、指定されたイテラブルのすべての順列を生成します。
# `product` 関数は、指定されたイテラブルのデカルト積を生成します。

# English Explanation:
# The `permutations` function generates all permutations of the specified iterable.
# The `product` function generates the Cartesian product of the specified iterables.

# Example list of book titles
books = ["Book A", "Book B", "Book C"]

# Generate all permutations of the book titles
all_permutations = list(permutations(books))
print("Permutations of books:")
for perm in all_permutations:
    print(perm)

# Example lists for Cartesian product
list1 = ["A", "B"]
list2 = [1, 2]

# Generate the Cartesian product of the lists
cartesian_product = list(product(list1, list2))
print("\nCartesian product of list1 and list2:")
for prod in cartesian_product:
    print(prod)
