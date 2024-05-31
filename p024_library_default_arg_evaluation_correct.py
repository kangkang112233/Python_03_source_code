class Library:
    def __init__(self):
        self.books = []

    # Correct method with default argument value as None
    def add_book(self, title, author, categories=None):
        if categories is None:
            categories = []
        book = {"title": title, "author": author, "categories": categories}
        self.books.append(book)
        print(
            f"Added book: Title='{title}', Author='{author}', Categories={categories}"
        )

    def list_books(self):
        for book in self.books:
            print(
                f"Title='{book['title']}', Author='{book['author']}', Categories={book['categories']}"
            )


# Create an instance of Library
library = Library()

# Add books without specifying categories (using default)
library.add_book("1984", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")

# Add a category to the first book's categories list
library.books[0]["categories"].append("Dystopian")

# Add another book without specifying categories
library.add_book("The Great Gatsby", "F. Scott Fitzgerald")

# List all books
library.list_books()

# Correct usage: Default value (mutable object) is not shared between calls
