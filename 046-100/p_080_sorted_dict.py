# 日本語の説明:
# `sorted` 関数は、与えられた iterable オブジェクトをソートし、新しいリストを生成します。
# 辞書の場合、`keys` メソッドを使用するとキーのリストが返され、`items` メソッドを使用するとキーと値のペアのリストが返されます。

# English Explanation:
# The `sorted` function sorts a given iterable object and generates a new list.
# For dictionaries, using the `keys` method returns a list of keys, and using the `items` method returns a list of key-value pairs.

# Example dictionary of books with publication years
books_dict = {
    "The Catcher in the Rye": 1951,
    "To Kill a Mockingbird": 1960,
    "1984": 1949,
    "Pride and Prejudice": 1813,
    "The Great Gatsby": 1925,
}

# Sort the dictionary by keys
sorted_keys = sorted(books_dict.keys())
print("Sorted keys:")
print(sorted_keys)

# Sort the dictionary by items (key-value pairs)
sorted_items = sorted(books_dict.items())
print("Sorted items by key-value pairs:")
print(sorted_items)

# Sort the dictionary items by value (publication year)
sorted_items_by_year = sorted(books_dict.items(), key=lambda item: item[1])
print("Sorted items by publication year:")
print(sorted_items_by_year)
