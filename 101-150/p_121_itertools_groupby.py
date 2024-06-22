import itertools

# 日本語の説明:
# `itertools.groupby` 関数は、指定されたキー関数に基づいて、連続する重複要素をグループ化するために使用されます。
# 入力のシーケンスはソートされている必要があります。

# English Explanation:
# The `itertools.groupby` function is used to group consecutive duplicate elements based on a specified key function.
# The input sequence must be sorted.

# Example list of books with genres
books_with_genres = [
    ("The Catcher in the Rye", "Fiction"),
    ("To Kill a Mockingbird", "Fiction"),
    ("A Brief History of Time", "Science"),
    ("The Selfish Gene", "Science"),
    ("1984", "Fiction"),
    ("The Great Gatsby", "Fiction"),
    ("Silent Spring", "Science"),
]

# Sort the list of books by genre
books_with_genres.sort(key=lambda x: x[1])

# Group books by genre using itertools.groupby
grouped_books = itertools.groupby(books_with_genres, key=lambda x: x[1])

print("Grouped books by genre:")
for genre, group in grouped_books:
    print(f"Genre: {genre}")
    for book in group:
        print(f"  {book[0]}")
