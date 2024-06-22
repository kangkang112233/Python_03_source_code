# 日本語の説明:
# Python のソートは安定ソートであり、比較対象が同じ場合、元の順番を維持します。
# これは、データの一部の属性に基づいてソートし、他の属性に基づいて追加のソートを行う際に特に有用です。
# 例えば、書籍を出版年でソートし、その後に著者名でソートする場合、出版年が同じ書籍は元の順番を維持します。

# English Explanation:
# Python's sorting is stable, meaning that if the comparison values are the same,
# the original order is maintained.
# This is particularly useful when sorting by one attribute and then by another.
# For example, when sorting books by publication year and then by author name,
# books with the same publication year will retain their original order.


# Define a class for books
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, year={self.year})"


# Example data: list of book objects
books = [
    Book("The Catcher in the Rye", "J.D. Salinger", 1951),
    Book("To Kill a Mockingbird", "Harper Lee", 1960),
    Book("1984", "George Orwell", 1949),
    Book("Pride and Prejudice", "Jane Austen", 1813),
    Book("The Great Gatsby", "F. Scott Fitzgerald", 1925),
    Book("Animal Farm", "George Orwell", 1945),
]

# First sort by year
books_sorted_by_year = sorted(books, key=lambda x: x.year)
print("Sorted books by publication year:")
print(books_sorted_by_year)

# Then sort by author while maintaining the order of the first sort
books_sorted_by_author = sorted(books_sorted_by_year, key=lambda x: x.author)
print("Sorted books by author (maintaining year order):")
print(books_sorted_by_author)
