# 日本語の説明:
# `deepcopy()` 関数は、オブジェクトのすべての階層をコピーします。
# これにより、コピー元のオブジェクトに影響を与えずにコピー先のオブジェクトを変更できます。

# English Explanation:
# The `deepcopy()` function creates a deep copy of an object, copying all levels of the object.
# This allows changes to the copied object without affecting the original object.

import copy

# Original book list with nested lists
original_books = [["Book A", "Book B"], ["Book C", "Book D"]]
deep_copied_books = copy.deepcopy(original_books)

# Modify the nested list in the copied list
deep_copied_books[0].append("Book E")

# Only the copied list is affected
print("Original book list:")
print(original_books)

print("Deep copied book list:")
print(deep_copied_books)
