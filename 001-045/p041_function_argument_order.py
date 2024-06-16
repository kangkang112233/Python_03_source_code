def add_book(title, author, *genres, published_year=2021, **extra_info):
    """
    Function to add a book to the library system.

    Parameters:
    title (str): The title of the book.
    author (str): The author of the book.
    *genres (str): Variable-length positional argument for genres.
    published_year (int): The year the book was published. Default is 2021.
    **extra_info (dict): Variable-length keyword arguments for any additional information.
    """
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Published Year: {published_year}")
    print(f"Genres: {', '.join(genres)}")
    for key, value in extra_info.items():
        print(f"{key.capitalize()}: {value}")


# Correct usage with all types of parameters
add_book(
    "1984",
    "George Orwell",
    "Dystopian",
    "Science Fiction",
    published_year=1949,
    pages=328,
    language="English",
)

# Output:
# Title: 1984
# Author: George Orwell
# Published Year: 1949
# Genres: Dystopian, Science Fiction
# Pages: 328
# Language: English

# Usage with default parameters and variable-length arguments
add_book(
    "To Kill a Mockingbird", "Harper Lee", "Fiction", "Classic", language="English"
)

# Output:
# Title: To Kill a Mockingbird
# Author: Harper Lee
# Published Year: 2021
# Genres: Fiction, Classic
# Language: English
