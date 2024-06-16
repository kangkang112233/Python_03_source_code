from typing import TypeVar, Generic

# Define a type variable T that can be an int or str
T = TypeVar("T", int, str)


class Library(Generic[T]):
    def __init__(self):
        self.items = []

    def add_item(self, item: T):
        self.items.append(item)
        print(f"Added {item} to the library")

    def show_items(self):
        print("Library contains:", self.items)


# Example usage in a book management system
library = Library()
library.add_item("Harry Potter")
library.add_item(1984)
library.show_items()
