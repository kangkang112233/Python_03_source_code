from enum import Enum, auto

# 日本語の説明:
# `enum.auto()` を使用すると、値を自動的に割り当てることができます。
# これにより、値の手動設定を省略できます。

# English Explanation:
# Using `enum.auto()` allows automatic assignment of values,
# eliminating the need for manual value assignment.


# Define the BookCategory enumeration with auto values
class BookCategory(Enum):
    FICTION = auto()
    NON_FICTION = auto()
    SCIENCE = auto()
    ART = auto()


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


# Using the enumeration
display_book_category(BookCategory.FICTION)
display_book_category(BookCategory(1))  # This will correctly display "Fiction Category"
display_book_category(BookCategory(2))  # This will correctly display "Non-fiction Category"
display_book_category(BookCategory(3))  # This will correctly display "Science Category"
display_book_category(BookCategory(4))  # This will correctly display "Art Category"
