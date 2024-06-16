import random


# Function to generate a random discount for a book
def generate_random_discount():
    # Generate a random discount percentage between 5% and 20%
    discount = random.uniform(5.0, 20.0)
    return round(discount, 2)  # Round to two decimal places


# Function to select a random book from a list
def select_random_book(books):
    # Select a random book from the list
    book = random.choice(books)
    return book


# List of books
books = ["Book1", "Book2", "Book3", "Book4"]

# Generate a random discount
discount = generate_random_discount()

# Select a random book
random_book = select_random_book(books)

# Print the results
print(f"Random discount: {discount}%")
print(f"Randomly selected book: {random_book}")
