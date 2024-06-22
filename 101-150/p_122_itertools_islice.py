import itertools

# `itertools.islice` 関数は、イテラブルからスライスを取得するために使用されます。
# スライスは、開始位置、終了位置、ステップを指定して取得できます。
# これは、特定の条件でデータを効率的に抽出するために役立ちます。
# 例えば、大きなデータセットから一部の要素だけを取り出す場合に便利です。
# `itertools.islice` を使用して、これらのパラメーターを指定するだけでスライスを簡単に取得できます。

# The `itertools.islice` function is used to obtain slices from an iterable.
# Slices can be obtained by specifying the start position, end position, and step.
# This is useful for efficiently extracting data under specific conditions,
# such as retrieving certain elements from a large dataset.
# You can easily obtain slices by using `itertools.islice` and specifying these parameters.

# Example list of books
books = [
    "The Catcher in the Rye",
    "To Kill a Mockingbird",
    "1984",
    "Pride and Prejudice",
    "The Great Gatsby",
    "Moby-Dick",
    "War and Peace",
    "Ulysses",
    "The Odyssey",
    "Madame Bovary",
]

# Get a slice from the list of books
# Slice from index 2 to 7, with a step of 2
sliced_books = itertools.islice(books, 2, 7, 2)

print("Sliced books:")
for book in sliced_books:
    print(book)
