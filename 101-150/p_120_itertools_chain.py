import itertools

# 日本語の説明:
# `itertools.chain` 関数は、複数のイテラブルを1つに連結するためのイテレータを作成します。

# English Explanation:
# The `itertools.chain` function creates an iterator that links multiple iterables into a single sequence.

# Example lists of book categories
science_books = ["A Brief History of Time", "The Selfish Gene", "Silent Spring"]
fiction_books = ["1984", "To Kill a Mockingbird", "The Great Gatsby"]
biography_books = ["The Diary of a Young Girl", "Long Walk to Freedom"]

# Use itertools.chain to link the lists
all_books = itertools.chain(science_books, fiction_books, biography_books)

print("All books:")
for book in all_books:
    print(book)
