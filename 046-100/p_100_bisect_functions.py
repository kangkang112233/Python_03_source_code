# 日本語の説明:
# bisect_left と bisect_right 関数は、ソートされたリストに要素を挿入する位置を見つけるために使用されます。

# English Explanation:
# The bisect_left and bisect_right functions are used to find the positions to insert elements in a sorted list.

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
new_book = "The Great Gatsby"

# Find the insertion positions
left_position = bisect.bisect_left(books, new_book)
right_position = bisect.bisect_right(books, new_book)

# Insert the new book using the found positions
books_left_insert = books[:left_position] + [new_book] + books[left_position:]
books_right_insert = books[:right_position] + [new_book] + books[right_position:]

# Output the results
print("Books list after left insert:")
print(books_left_insert)

print("Books list after right insert:")
print(books_right_insert)
