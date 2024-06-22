from pprint import pprint

# 日本語の説明:
# `pprint` 関数を使って、ネストした辞書と長いリストを整形して表示します。

# English Explanation:
# Using the `pprint` function to format and display nested dictionaries and long lists.

# Example nested dictionary representing book information
books = {
    "Fiction": {
        "To Kill a Mockingbird": {"author": "Harper Lee", "year": 1960, "copies": 3},
        "1984": {"author": "George Orwell", "year": 1949, "copies": 5},
    },
    "Non-Fiction": {
        "Sapiens": {"author": "Yuval Noah Harari", "year": 2011, "copies": 2},
        "Educated": {"author": "Tara Westover", "year": 2018, "copies": 4},
    },
}

# Example long list of book titles
book_titles = [
    "The Catcher in the Rye",
    "To Kill a Mockingbird",
    "1984",
    "Pride and Prejudice",
    "The Great Gatsby",
    "Moby Dick",
    "War and Peace",
    "The Odyssey",
    "Hamlet",
    "The Adventures of Huckleberry Finn",
]

# Format and print the nested dictionary
print("Formatted nested dictionary:")
pprint(books, width=1)

# Format and print the long list
print("\nFormatted long list:")
pprint(book_titles, width=1)
