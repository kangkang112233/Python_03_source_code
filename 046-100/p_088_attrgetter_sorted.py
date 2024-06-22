# 日本語の説明:
# `attrgetter` 関数を使用してオブジェクトの属性に基づいてソートする方法を説明します。
# `attrgetter` 関数は、指定した属性に基づいてオブジェクトを取得するための関数を生成します。
# この関数は、`sorted` 関数の `key` パラメータに渡して、オブジェクトの特定の属性に基づいて
# ソートを行うために使用できます。例えば、本のオブジェクトを出版年でソートすることができます。

# English Explanation:
# Explains how to use the `attrgetter` function to sort objects based on their attributes.
# The `attrgetter` function generates a function that retrieves objects based on specified attributes.
# This function can be passed to the `key` parameter of the `sorted` function to sort objects based on specific attributes.
# For example, it can sort book objects by publication year.

from operator import attrgetter


# Define a class for books
class Book:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __repr__(self):
        return f"Book(title={self.title}, year={self.year})"


# Example data: list of book objects
books = [
    Book("The Catcher in the Rye", 1951),
    Book("To Kill a Mockingbird", 1960),

    ("1984", 1949),
    Book("Pride and Prejudice", 1813),
    Book("The Great Gatsby", 1925),
]

# Sort the books by publication year
sorted_books_by_year = sorted(books, key=attrgetter("year"))
print("Sorted books by publication year:")
print(sorted_books_by_year)

# Original list remains unchanged
print("Original list of books:")
print(books)
