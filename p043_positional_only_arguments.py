def add_book(title, author, /, published_year=2021, is_available=True):
    """
    Function to add a book to the library system.

    Parameters:
    title (str): The title of the book.
    author (str): The author of the book.
    published_year (int, optional): The year the book was published. Default is 2021.
    is_available (bool, optional): Availability status of the book. Default is True.
    """
    status = "available" if is_available else "not available"
    print(
        f"Adding book: Title='{title}', Author='{author}', Published Year={published_year}, Status='{status}'"
    )


# Correct usage with positional-only arguments
add_book("1984", "George Orwell", published_year=1949, is_available=False)
# Output: Adding book: Title='1984', Author='George Orwell', Published Year=1949, Status='not available'

# Correct usage with positional-only arguments and default parameters
add_book("To Kill a Mockingbird", "Harper Lee")
# Output: Adding book: Title='To Kill a Mockingbird', Author='Harper Lee', Published Year=2021, Status='available'

# Incorrect usage with keyword for positional-only arguments
try:
    add_book(
        title="Brave New World",
        author="Aldous Huxley",
        published_year=1932,
        is_available=False,
    )
except TypeError as e:
    print("Error:", e)
# Output: Error: add_book() got some positional-only arguments passed as keyword arguments: 'title, author'
