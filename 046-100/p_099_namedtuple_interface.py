# 日本語の説明:
# namedtuple をインターフェースとして使用し、その上にクラスを作成してインスタンスを生成することができます。

# English Explanation:
# You can use namedtuple as an interface, creating a class on top of it and generating instances.

from collections import namedtuple

# Create a named tuple type called 'Book'
Book = namedtuple("Book", "title author year")


# Extend the named tuple with additional methods
class ExtendedBook(Book):
    def age(self):
        current_year = 2024
        return current_year - self.year


# Create an instance of the extended class
book = ExtendedBook(title="1984", author="George Orwell", year=1949)

# Access fields by name
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Year: {book.year}")

# Use the additional method
print(f"Age: {book.age()} years")

# Create another instance with different data
another_book = ExtendedBook(title="Brave New World", author="Aldous Huxley", year=1932)
print(f"Title: {another_book.title}")
print(f"Author: {another_book.author}")
print(f"Year: {another_book.year}")
print(f"Age: {another_book.age()} years")
