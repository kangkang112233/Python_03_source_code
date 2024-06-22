# 日本語の説明:
# 名前付きタプルは、タプルの各値に意味を割り当てて、
# インデックスの代わりに属性名で値にアクセスできるようになります。
# namedtuple() 関数を呼び出して名前付きタプルを作成します。

# English Explanation:
# A named tuple assigns meaning to each value in a tuple,
# allowing access to values by attribute name instead of index.
# Use the namedtuple() function to create a named tuple.

from collections import namedtuple

# Create a named tuple type called 'Book'
Book = namedtuple("Book", "title author year")

# Create an instance of the named tuple
book = Book(title="1984", author="George Orwell", year=1949)

# Access fields by name
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Year: {book.year}")

# Use defaults
BookWithDefaults = namedtuple("Book", "title author year", defaults=["Unknown", 1900])
book_with_defaults = BookWithDefaults(title="Brave New World")
print(f"Title: {book_with_defaults.title}")
print(f"Author: {book_with_defaults.author}")
print(f"Year: {book_with_defaults.year}")

# Rename fields
BookRenamed = namedtuple("Book", "title author year title", rename=True)
book_renamed = BookRenamed("1984", "George Orwell", 1949, "Another Title")
print(book_renamed)
