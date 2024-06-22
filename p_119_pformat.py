import pprint

# 日本語の説明:
# `pprint` モジュールの `pformat` 関数は、データ構造を整形して文字列として返す機能を提供します。

# English Explanation:
# The `pformat` function in the `pprint` module provides functionality to format data structures
# and return them as a string.

# Example data structure
books_data = {
    "Science": ["A Brief History of Time", "The Selfish Gene", "Silent Spring"],
    "Fiction": ["1984", "To Kill a Mockingbird", "The Great Gatsby"],
    "Biography": ["The Diary of a Young Girl", "Long Walk to Freedom"],
}

# Use pformat to get a formatted string
formatted_books = pprint.pformat(books_data)
print("Formatted books data:")
print(formatted_books)
print(books_data)
