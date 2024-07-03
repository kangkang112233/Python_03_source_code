# 日本語の説明:
# インスタンスのDeepcopyとは、オブジェクトの全てのレベルで再帰的に新しいコピーを作成することで、
# 元のオブジェクトに影響を与えずに完全な独立したコピーを作成する方法です。

# English Explanation:
# Instance Deepcopy is a method of creating a completely independent copy of an object
# by recursively copying all levels of the object,
# ensuring the original object is unaffected.

import copy


# Define a class for a book
class Book:
    def __init__(self, title, authors):
        self.title = title
        self.authors = authors


# Original book instance
original_book = Book("Python Programming", ["Author A", "Author B"])

# Create a deep copy of the book instance
copied_book = copy.deepcopy(original_book)

# Modify the copied book instance
copied_book.title = "Advanced Python Programming"
copied_book.authors.append("Author C")

# Print original and copied book instances to show they are independent
print("Original book title:", original_book.title)
print("Original book authors:", original_book.authors)
print("Copied book title:", copied_book.title)
print("Copied book authors:", copied_book.authors)
