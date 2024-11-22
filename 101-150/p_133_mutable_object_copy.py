# 日本語の説明:
# ループ処理中に要素の追加や変更を行いたい場合、ミュータブルオブジェクトのコピーを作成することで、
# 元のオブジェクトに影響を与えずに変更を行うことができます。

# English Explanation:
# Creating a copy of a mutable object during a loop allows for modifications without affecting the original object.

import copy

# Original book list
original_books = ["Book A", "Book B", "Book C"]
modified_books = copy.deepcopy(original_books)

# Loop through the copied list and add a new element
for book in modified_books:
    if book == "Book B":
        modified_books.append("Book D")

print("Original book list:")
print(original_books)

print("Modified book list:")
print(modified_books)
