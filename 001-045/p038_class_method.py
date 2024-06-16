class Book:
    total_books = 0  # class variable to keep track of the number of books

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1  # increment the book count when a new book is added

    @classmethod
    def display_total_books(cls):
        # Class method accessing class variable
        print(f"Total books in library: {cls.total_books}")

    @classmethod
    def create_books_from_list(cls, book_list):
        # Class method acting as a factory to create multiple books from a list
        books = []
        for title, author in book_list:
            books.append(cls(title, author))
        return books


# Create instances of Book using the factory method
books = Book.create_books_from_list(
    [
        ("1984", "George Orwell"),
        ("To Kill a Mockingbird", "Harper Lee"),
        ("The Great Gatsby", "F. Scott Fitzgerald"),
    ]
)

# Call class method to display the updated book count
Book.display_total_books()  # Output: Total books in library: 3

# Additional example of adding a new book
new_book = Book("Brave New World", "Aldous Huxley")

# Call class method to display the updated book count
Book.display_total_books()  # Output: Total books in library: 4
