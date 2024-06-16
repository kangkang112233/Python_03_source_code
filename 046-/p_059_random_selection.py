import random


# Function to randomly select a book
def select_random_book(books):
    return random.choice(books)


# Function to select multiple random books with replacement
def select_multiple_books_with_replacement(books, k):
    return random.choices(books, k=k)


# Function to select multiple random books without replacement
def select_multiple_books_without_replacement(books, k):
    return random.sample(books, k)


# Function to shuffle the book list
def shuffle_books(books):
    random.shuffle(books)
    return books


# Example book list
book_list = ["Book1", "Book2", "Book3", "Book4", "Book5"]

# Randomly select a book
random_book = select_random_book(book_list)
print("Randomly selected book:", random_book)

# Select multiple random books with replacement
multiple_books_with_replacement = select_multiple_books_with_replacement(book_list, 3)
print("Multiple books with replacement:", multiple_books_with_replacement)

# Select multiple random books without replacement
multiple_books_without_replacement = select_multiple_books_without_replacement(
    book_list, 3
)
print("Multiple books without replacement:", multiple_books_without_replacement)

# Shuffle the book list
shuffled_books = shuffle_books(book_list[:])  # Use a copy to preserve original order
print("Shuffled book list:", shuffled_books)
