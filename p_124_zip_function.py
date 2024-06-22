# `zip` 関数は、指定したイテラブルオブジェクトのいずれかがすべての値を返すと処理を終了します。
# 長さが異なるイテラブルオブジェクトを指定した場合は、短いほうの長さにそろえられるので注意してください。
# なお、Python 3.10では `zip` 関数に `strict` 引数が追加されました。
# `strict` 引数に `True` を指定し、長さが異なるイテラブルオブジェクトを指定した場合は `ValueError` 例外が送出されます。
# `zip` を使用するには、複数のイテラブルを引数として渡すだけです。

# The `zip` function stops processing when any one of the iterables is exhausted.
# If the iterables are of different lengths, it stops at the shortest length.
# Note that in Python 3.10, the `zip` function added a `strict` argument.
# When `strict` is set to `True`, a `ValueError` is raised if the iterables have different lengths.
# To use `zip`, simply pass multiple iterables as arguments.

# Example lists of book titles and authors
book_titles = ["The Catcher in the Rye", "To Kill a Mockingbird", "1984"]
book_authors = ["J.D. Salinger", "Harper Lee"]

# Use zip to combine book titles and authors
books = zip(book_titles, book_authors)

# Print the combined list of books
print("Combined list of books:")
for title, author in books:
    print(f"{title} by {author}")

# Using zip with strict argument in Python 3.10+
try:
    books_strict = zip(book_titles, book_authors, strict=True)
    print("Combined list of books with strict=True:")
    for title, author in books_strict:
        print(f"{title} by {author}")
except ValueError as e:
    print(f"ValueError: {e}")
