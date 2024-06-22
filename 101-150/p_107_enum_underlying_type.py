from enum import Enum


# Define the BookCategory enumeration
class BookCategory(Enum):
    FICTION = 1
    NON_FICTION = 2
    SCIENCE = 3
    ART = 4


# Function to display book category based on enumeration
def display_book_category(category):
    if category == BookCategory.FICTION:
        print("Fiction Category")
    elif category == BookCategory.NON_FICTION:
        print("Non-fiction Category")
    elif category == BookCategory.SCIENCE:
        print("Science Category")
    elif category == BookCategory.ART:
        print("Art Category")
    else:
        print("Unknown Category")


# Using the enumeration value directly
display_book_category(BookCategory.FICTION)

# Using an integer value and converting it to enumeration
display_book_category(BookCategory(1))  # This will correctly display "Fiction Category"

# Trying to use an invalid integer value
try:
    display_book_category(BookCategory(5))  # This will raise a ValueError
except ValueError as e:
    print(f"Error: {e}")

# Demonstrating the underlying type
print(f"Type of BookCategory: {type(BookCategory)}")  # <enum 'BookCategory'>
print(
    f"Type of BookCategory.FICTION: {type(BookCategory.FICTION)}"
)  # <enum 'BookCategory'>
print(
    f"Is BookCategory.FICTION an instance of BookCategory? {isinstance(BookCategory.FICTION, BookCategory)}"
)  # True
