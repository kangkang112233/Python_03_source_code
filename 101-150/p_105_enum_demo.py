from enum import Enum


# Enum for book categories
class BookCategory(Enum):
    FICTION = 1
    NON_FICTION = 2
    SCIENCE = 3
    HISTORY = 4


# 日本語の説明:
# 列挙型（Enum）は、名前付き定数の集合を定義するために使用されるデータ型です。
# これにより、コードの可読性が向上し、定数の使用を標準化できます。

# English Explanation:
# Enum type is a data type used to define a set of named constants.
# This improves code readability and standardizes the use of constants.


# Function to display book category
def display_book_category(category):
    if category == BookCategory.FICTION:
        print("Category: Fiction")
    elif category == BookCategory.NON_FICTION:
        print("Category: Non-Fiction")
    elif category == BookCategory.SCIENCE:
        print("Category: Science")
    elif category == BookCategory.HISTORY:
        print("Category: History")
    else:
        print("Unknown Category")


# Example usage
display_book_category(BookCategory.SCIENCE)
display_book_category(2)
