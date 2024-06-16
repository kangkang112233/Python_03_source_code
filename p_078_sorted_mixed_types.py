# Example list with mixed types
mixed_list = ["book", 42, "library", 7, "chapter", 19]


# Function to convert items to a common type (string) for comparison
def custom_sort_key(item):
    return str(item)


# Sort the list using the custom sort key to handle mixed types
try:
    sorted_mixed_list = sorted(mixed_list, key=custom_sort_key)
    print("Sorted mixed list:")
    print(sorted_mixed_list)
except TypeError as e:
    print(f"Error sorting mixed list: {e}")

# Original list remains unchanged
print("Original list:")
print(mixed_list)

# Example: Sorting a list of book titles and publication years
books_with_mixed_types = [
    {"title": "The Catcher in the Rye", "year": "1951"},
    {"title": "To Kill a Mockingbird", "year": 1960},
    {"title": 1984, "year": 1949},
    {"title": "Pride and Prejudice", "year": "1813"},
    {"title": "The Great Gatsby", "year": 1925},
]

# Sort the books by title using the custom sort key
sorted_books = sorted(books_with_mixed_types, key=lambda x: custom_sort_key(x["title"]))
print("Sorted books by title:")
for book in sorted_books:
    print(f"{book['title']} ({book['year']})")
