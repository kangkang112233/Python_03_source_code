# Book management system example for demonstrating unpacking and dictionary usage
class BookManagementSystem:
    def __init__(self):
        # Initialize a list of books as tuples (id, title, author)
        self.books = [
            (1, "1984", "George Orwell"),
            (2, "Brave New World", "Aldous Huxley"),
        ]

    def display_books(self):
        # Unpack each book tuple and print details
        for book in self.books:
            book_id, title, author = book
            print(f"Book ID: {book_id}, Title: '{title}', Author: '{author}'")

    def get_book_details(self):
        # Return a dictionary with book titles as keys and authors as values
        return {title: author for _, title, author in self.books}


# Create instance and use methods
bms = BookManagementSystem()
bms.display_books()
print(bms.get_book_details())

# Output format adjusted for clarity
# Output will display each book followed by the dictionary of book details
