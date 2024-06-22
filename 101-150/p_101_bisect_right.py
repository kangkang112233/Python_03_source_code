# 日本語の説明:
# bisect_right 関数は、ソートされたリストに要素を挿入する位置を見つけるために使用されます。
# もしリストにその要素が既に存在する場合、最後のその要素の次の位置を返します。

# English Explanation:
# The bisect_right function is used to find the position to insert an element in a sorted list.
# If the element is already present, it returns the position after the last occurrence of the element.

import bisect

# Example sorted list of book titles
books = [
    "1984",
    "Brave New World",
    "Pride and Prejudice",
    "The Catcher in the Rye",
    "To Kill a Mockingbird",
]

# Book to be inserted
new_book = "Brave New World"

# Find the insertion position using bisect_right
right_position = bisect.bisect_right(books, new_book)
print(right_position)

# Insert the new book using the found position
books_right_insert = books[:right_position] + [new_book] + books[right_position:]

# Output the results
print("Books list after right insert:")
print(books_right_insert)
