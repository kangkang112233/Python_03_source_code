# 日本語の説明:
# `reversed` 関数は、与えられた iterable オブジェクトの逆順のイテレータを返します。
# 元のオブジェクトは変更されず、順番を逆にするだけで、ソートは行われません。
# 例えば、リストやタプルの順序を逆にする際に使用されます。

# English Explanation:
# The `reversed` function returns a reverse iterator of the given iterable object.
# The original object is not modified, and it only reverses the order without sorting.
# It is used to reverse the order of lists or tuples, for example.

# Example list of book titles
books_list = [
    "The Catcher in the Rye",
    "To Kill a Mockingbird",
    "1984",
    "Pride and Prejudice",
    "The Great Gatsby",
]

# Reverse the list using reversed
reversed_books_list = list(reversed(books_list))
print("Reversed list of books:")
print(reversed_books_list)

# Original list remains unchanged
print("Original list of books:")
print(books_list)

# Example tuple of book titles
books_tuple = (
    "The Catcher in the Rye",
    "To Kill a Mockingbird",
    "1984",
    "Pride and Prejudice",
    "The Great Gatsby",
)

# Reverse the tuple using reversed
reversed_books_tuple = tuple(reversed(books_tuple))
print("Reversed tuple of books:")
print(reversed_books_tuple)

# Original tuple remains unchanged
print("Original tuple of books:")
print(books_tuple)
