# 日本語の説明:
# `itemgetter` 関数を使用して辞書の値でソートする方法を説明します。
# 辞書のキーではなく値に基づいてソートするためには、`itemgetter` 関数を `sorted` 関数の `key` パラメータに渡します。
# 例えば、書籍の辞書を出版年（値）でソートすることができます。

# English Explanation:
# Explains how to use the `itemgetter` function to sort a dictionary by its values.
# To sort by values rather than keys, pass the `itemgetter` function to the `key` parameter of the `sorted` function.
# For example, a dictionary of books can be sorted by publication year (value).

from operator import itemgetter

# Example dictionary of books with publication years
books_dict = {
    "The Catcher in the Rye": 1951,
    "To Kill a Mockingbird": 1960,
    "1984": 1949,
    "Pride and Prejudice": 1813,
    "The Great Gatsby": 1925,
}

# Sort the dictionary by its values (publication years)
sorted_books_by_year = sorted(books_dict.items(), key=itemgetter(1))
print("Sorted books by publication year:")
print(sorted_books_by_year)

# Original dictionary remains unchanged
print("Original dictionary of books:")
print(books_dict)
