def update_book(title, author, *, published_year=2021, is_available=True):
    """
    Function to update book information in the library system.

    Parameters:
    title (str): The title of the book.
    author (str): The author of the book.
    published_year (int, optional): The year the book was published. Default is 2021.
    is_available (bool, optional): Availability status of the book. Default is True.
    """
    status = "available" if is_available else "not available"
    print(
        f"Updating book: Title='{title}', Author='{author}', Published Year={published_year}, Status='{status}'"
    )


# Correct usage with keyword-only arguments
update_book("1984", "George Orwell", published_year=1949, is_available=False)
# Output: Updating book: Title='1984', Author='George Orwell', Published Year=1949, Status='not available'

# Usage with default keyword-only arguments
update_book("To Kill a Mockingbird", "Harper Lee")
# Output: Updating book: Title='To Kill a Mockingbird', Author='Harper Lee', Published Year=2021, Status='available'

# Incorrect usage without keyword for keyword-only arguments
try:
    update_book("Brave New World", "Aldous Huxley", 1932, False)
except TypeError as e:
    print("Error:", e)
# Output: Error: update_book() takes 2 positional arguments but 4 were given
