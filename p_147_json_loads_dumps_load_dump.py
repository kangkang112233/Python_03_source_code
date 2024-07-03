# `loads`関数は、文字列からPythonのデータ構造に変換するプロセスです。
# 主に、保存されたデータや受信したデータを使用可能な形式に変換するために使用されます。
#
# The `loads` function is used to convert a string into a Python data structure.
# It is mainly used to convert stored or received data into a usable format.
#
# `dumps`関数は、Pythonのデータ構造を文字列に変換するプロセスです。
# 主に、データの保存や転送のために使用されます。
#
# The `dumps` function is used to convert a Python data structure into a string.
# It is mainly used for saving or transmitting data.
#
# `load`関数は、ファイルからPythonのデータ構造に変換するプロセスです。
# 主に、ファイルから保存されたデータを読み込み、使用可能な形式に変換するために使用されます。
#
# The `load` function is used to convert a file into a Python data structure.
# It is mainly used to read saved data from a file and convert it into a usable format.
#
# `dump`関数は、Pythonのデータ構造をファイルに保存するプロセスです。
# 主に、データの保存のために使用されます。
#
# The `dump` function is used to save a Python data structure to a file.
# It is mainly used for saving data.

import json

# Example book data
book_data = {
    "title": "Python Programming",
    "author": "John Doe",
    "year": 2020,
    "isbn": "123-456-789",
}

# Serialize the book data to a JSON string using dumps
book_data_json = json.dumps(book_data, indent=4)
print("Serialized book data (using dumps):\n", book_data_json)

# Deserialize the JSON string back to a Python dictionary using loads
deserialized_book_data = json.loads(book_data_json)
print("\nDeserialized book data (using loads):")
for key, value in deserialized_book_data.items():
    print(f"{key}: {value}")


# Application in a library management system
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def save_to_file(self, filename):
        # Save the list of books to a file as a JSON string using dump
        with open(filename, "w") as file:
            json.dump(self.books, file, indent=4)

    def load_from_file(self, filename):
        # Load the list of books from a file and convert it back to a Python list using load
        with open(filename, "r") as file:
            self.books = json.load(file)


# Create library instance and add a book
library = Library()
library.add_book(book_data)

# Save library to a file
library.save_to_file("library.json")

# Load library from a file
library.load_from_file("library.json")
print("\nLibrary books loaded from file (using load):")
for book in library.books:
    print(book)
