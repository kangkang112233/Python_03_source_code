# 日本語の説明:
# `copy()` 関数は、1階層のみの浅いコピーに使用されます。
# コピー先の2階層目より深い層のオブジェクトを変更すると、コピー元のオブジェクトも変更されます。

# English Explanation:
# The `copy()` function is used for creating a shallow copy of an object.
# If deeper levels of the copied object are changed, the original object will also be changed.

import copy

# Original book list with nested lists
original_books = [["Book A", "Book B"], ["Book C", "Book D"]]
shallow_copied_books = copy.copy(original_books)

# Modify the nested list in the copied list
shallow_copied_books[0].append("Book E")

# Both lists are affected
print("Original book list:")
print(original_books)

print("Shallow copied book list:")
print(shallow_copied_books)
