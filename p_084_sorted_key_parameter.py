# 日本語の説明:
# `sorted` 関数に `key` 引数を指定しない場合、要素そのものを小なり（<）で比較します。
# `key` 引数には、関数などの呼び出し可能オブジェクトを指定できます。
# 指定された関数などを使い、要素を変換などしてから小なり（<）で比較します。
# 例えば、`key` 引数に `str.lower` を指定すると、各文字列を小文字に変換して比較します。

# English Explanation:
# If the `key` parameter of the `sorted` function is not specified, the elements themselves are compared directly.
# The `key` parameter can specify a callable object, such as a function, which is used to transform the elements
# before comparing them. For example, specifying `str.lower` as the `key` parameter converts each string to
# lowercase before comparing.

# Example list of book titles with mixed case
books_list = [
    "The Catcher in the Rye",
    "to Kill a Mockingbird",
    "1984",
    "Pride and Prejudice",
    "the Great Gatsby",
]

# Sort the list without specifying the key parameter (case-sensitive)
sorted_books_case_sensitive = sorted(books_list)
print("Sorted list (case-sensitive):")
print(sorted_books_case_sensitive)

# Sort the list with the key parameter specified as str.lower (case-insensitive)
sorted_books_case_insensitive = sorted(books_list, key=str.lower)
print("Sorted list (case-insensitive):")
print(sorted_books_case_insensitive)

# Original list remains unchanged
print("Original list of books:")
print(books_list)
