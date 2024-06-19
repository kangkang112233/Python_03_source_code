# 日本語の説明:
# `sorted` 関数は、与えられた iterable オブジェクトをソートし、新しいリストを生成します。
# タプルをソートする場合も、結果としてリストが返されます。元のタプルは変更されません。
# これは、タプルがイミュータブルであるためです。

# English Explanation:
# The `sorted` function sorts a given iterable object and generates a new list.
# When sorting tuples, the result is also a list, and the original tuple remains unchanged.
# This is because tuples are immutable.

# Example tuple of book titles and publication years
books_tuple = (
    ("The Catcher in the Rye", 1951),
    ("To Kill a Mockingbird", 1960),
    ("1984", 1949),
    ("Pride and Prejudice", 1813),
    ("The Great Gatsby", 1925),
)

# Sort the tuple by publication year
sorted_books_by_year = sorted(books_tuple, key=lambda x: x[1])
print("Sorted books by year:")
print(sorted_books_by_year)

# Original tuple remains unchanged
print("Original tuple:")
print(books_tuple)

# Sort the tuple by title
sorted_books_by_title = sorted(books_tuple, key=lambda x: x[0])
print("Sorted books by title:")
print(sorted_books_by_title)
