from itertools import permutations

# 日本語の説明:
# `permutations` 関数は、指定されたイテラブルのすべての順列を生成します。
# これは、要素のすべての順列を取得したい場合に便利です。

# English Explanation:
# The `permutations` function generates all permutations of the specified iterable.
# It is useful when you want to obtain all possible arrangements of the elements.

# Example list of book titles
books = ["Book A", "Book B", "Book C"]

# Generate all permutations of the book titles
all_permutations = list(permutations(books))

# Print the permutations
for perm in all_permutations:
    print(perm)
