# Example list of book titles
books = [
    "The Catcher in the Rye",
    "To Kill a Mockingbird",
    "1984",
    "Pride and Prejudice",
    "The Great Gatsby",
]

# Sort the list of books alphabetically
sorted_books = sorted(books)
print("Sorted books alphabetically:")
print(sorted_books)

# Original list remains unchanged
print("Original list of books:")
print(books)

# Sort the list of books by length of title
sorted_books_by_length = sorted(books, key=len)
print("Sorted books by length of title:")
print(sorted_books_by_length)

# Example: Sorting a list of dictionaries representing books by their publication year
books_with_year = [
    {"title": "The Catcher in the Rye", "year": 1951},
    {"title": "To Kill a Mockingbird", "year": 1960},
    {"title": "1984", "year": 1949},
    {"title": "Pride and Prejudice", "year": 1813},
    {"title": "The Great Gatsby", "year": 1925},
]

# Sort the books by publication year
sorted_books_by_year = sorted(books_with_year, key=lambda x: x["year"])
print("Sorted books by publication year:")
for book in sorted_books_by_year:
    print(f"{book['title']} ({book['year']})")
