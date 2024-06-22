# `zip` 関数は、指定した複数のイテラブルオブジェクトから1つずつ値を取得し、
# タプルの要素として返すイテレーターを作成します。
# 複数のリストやシーケンスを同時に反復処理したい場合に便利です。
# 例えば、複数のデータセットを並行して処理する場合などに使われます。
# `zip` を使用するには、複数のイテラブルを引数として渡すだけです。

# The `zip` function creates an iterator that aggregates elements from each of the iterables.
# This is useful when you want to iterate over multiple lists or sequences in parallel,
# such as when processing multiple datasets concurrently.
# To use `zip`, simply pass multiple iterables as arguments.

# Example lists of book titles and authors
book_titles = ["The Catcher in the Rye", "To Kill a Mockingbird", "1984"]
book_authors = ["J.D. Salinger", "Harper Lee", "George Orwell"]

# Use zip to combine book titles and authors
books = zip(book_titles, book_authors)

# Print the combined list of books
print("Combined list of books:")
for title, author in books:
    print(f"{title} by {author}")
