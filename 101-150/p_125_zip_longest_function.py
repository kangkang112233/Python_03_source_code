# `zip_longest` 関数は、指定した複数のイテラブルオブジェクトから1つずつ値を取得し、
# タプルの要素として返すイテレーターを作成します。
# 複数のリストやシーケンスを同時に反復処理したい場合に便利です。
# `zip` 関数と異なり、`zip_longest` は最長のイテラブルオブジェクトの長さまで反復処理を続け、
# 他のイテラブルオブジェクトの要素が尽きた場合は、デフォルト値で埋めます。
# 使用するには、`itertools.zip_longest` モジュールをインポートし、
# 複数のイテラブルオブジェクトとオプションのデフォルト値を引数として渡します。

# The `zip_longest` function creates an iterator that aggregates elements from each of the iterables.
# This is useful when you want to iterate over multiple lists or sequences of different lengths.
# Unlike the `zip` function, `zip_longest` continues until the longest iterable is exhausted,
# filling in missing values from shorter iterables with a specified default value.
# To use it, import the `itertools.zip_longest` module, and pass multiple iterables along with an optional default value.

from itertools import zip_longest

# Example lists of book titles and authors
book_titles = ["The Catcher in the Rye", "To Kill a Mockingbird", "1984"]
book_authors = ["J.D. Salinger", "Harper Lee"]

# Use zip_longest to combine book titles and authors, filling missing values with "Unknown"
books = zip_longest(book_titles, book_authors, fillvalue="Unknown")

# Print the combined list of books
print("Combined list of books using zip_longest:")
for title, author in books:
    print(f"{title} by {author}")
