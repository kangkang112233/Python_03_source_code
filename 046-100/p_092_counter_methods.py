# 日本語の説明:
# `Counter` オブジェクトの `elements`、`most_common`、`update`、`subtract` メソッドは、
# カウントデータを操作するための便利な機能を提供します。`elements` はカウントの要素を列挙し、
# `most_common` は最も一般的な要素を返し、`update` は新しい要素を追加し、`subtract` はカウントを減らします。

# English Explanation:
# The `elements`, `most_common`, `update`, and `subtract` methods of the `Counter` object
# provide convenient functions for manipulating count data. `elements` enumerates count elements,
# `most_common` returns the most common elements, `update` adds new elements, and `subtract` reduces the count.

from collections import Counter

# Create a Counter object from a list of book titles
book_counts = Counter(
    [
        "1984",
        "1984",
        "To Kill a Mockingbird",
        "The Great Gatsby",
        "1984",
        "The Catcher in the Rye",
        "The Great Gatsby",
    ]
)

# elements method: list all elements in the Counter
print("Elements in the Counter:")
print(list(book_counts.elements()))

# most_common method: get the most common elements
print("Most common elements:")
print(book_counts.most_common(2))  # Top 2 most common elements

# update method: add counts from an iterable or another Counter
book_counts.update(["1984", "Pride and Prejudice"])
print("After update:")
print(book_counts)

# subtract method: subtract counts, keeping only positive counts
book_counts.subtract(["1984", "The Great Gatsby", "The Great Gatsby"])
print("After subtract:")
print(book_counts)
