# 日本語の説明:
# `list.sort` メソッドは、リストをその場でソートし、元のリストを変更します。
# `list.reverse` メソッドも同様に、リストの順序を逆にして、元のリストを変更します。
# これらの操作は破壊的操作と呼ばれ、元のリストが変更されるため、元の順序を保持する必要がある場合は注意が必要です。

# English Explanation:
# The `list.sort` method sorts the list in place, modifying the original list.
# The `list.reverse` method also reverses the list order in place, modifying the original list.
# These operations are called destructive operations, as they modify the original list,
# so caution is needed if the original order needs to be preserved.

# Example list of book titles
books_list = [
    "The Catcher in the Rye",
    "To Kill a Mockingbird",
    "1984",
    "Pride and Prejudice",
    "The Great Gatsby",
]

# Sort the list in place
books_list.sort()
print("Sorted list of books:")
print(books_list)

# Reverse the list in place
books_list.reverse()
print("Reversed sorted list of books:")
print(books_list)

# Since the original list is modified, if we need the original order, we should make a copy before sorting or reversing
books_list_original = [
    "The Catcher in the Rye",
    "To Kill a Mockingbird",
    "1984",
    "Pride and Prejudice",
    "The Great Gatsby",
]
books_list_copy = books_list_original.copy()

# Sort the copy of the list
books_list_copy.sort()
print("Sorted copy of the original list:")
print(books_list_copy)

# Original list remains unchanged
print("Original list remains unchanged:")
print(books_list_original)
