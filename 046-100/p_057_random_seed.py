import random


# Function to generate a fixed sequence of random numbers
def generate_fixed_random_books():
    # Seed the random number generator for reproducibility
    random.seed(
        42
    )  # Using the same seed value will produce the same sequence of random numbers

    # Randomly select books
    books = ["Book1", "Book2", "Book3", "Book4", "Book5"]
    selected_books = random.sample(books, 3)  # Randomly select 3 books from the list

    return selected_books


# Generate the fixed sequence of random books
fixed_random_books = generate_fixed_random_books()

# Print the selected books
print("Selected books:", fixed_random_books)
