# 日本語の説明:
# `reversed` 関数は、与えられた iterable オブジェクトの逆順のイテレータを返します。
# 元のオブジェクトは変更されず、逆順のイテレータが返されますが、リストではありません。
# このイテレータは一度しか使用できず、2回目に使うと空のリストになります。

# English Explanation:
# The `reversed` function returns a reverse iterator of the given iterable object.
# The original object is not modified, and a reverse iterator, not a list, is returned.
# This iterator can only be used once, and using it a second time results in an empty list.

# Example list of book titles
books_list = [
    "The Catcher in the Rye",
    "To Kill a Mockingbird",
    "1984",
    "Pride and Prejudice",
    "The Great Gatsby",
]

# Get the reverse iterator
reversed_books_iterator = reversed(books_list)

# Check the type of the reverse iterator
print("Type of reversed iterator:")
print(type(reversed_books_iterator))

# Convert the iterator to a list to display the reversed order
reversed_books_list = list(reversed_books_iterator)
print("Reversed list of books:")
print(reversed_books_list)

# Attempt to use the iterator again
reused_reversed_books_list = list(reversed_books_iterator)
print("Reused reversed iterator (should be empty):")
print(reused_reversed_books_list)

# Original list remains unchanged
print("Original list of books:")
print(books_list)
