from enum import Enum


class BookCategory(Enum):
    FICTION = 1
    NONFICTION = 2
    SCIFI = 3
    FANTASY = 4


# 日本語の説明:
# 列挙型は、一連の定数に名前を付けるための方法です。
# 定数を呼び出すために、ドット表記、定数名、または定数値を使用することができます。

# English Explanation:
# An enumeration type is a way to name a set of constants.
# Constants can be called using dot notation, constant name, or constant value.


# Function to display book category
def display_book_category(category):
    if category == BookCategory.FICTION:
        print("Fiction")
    elif category == BookCategory.NONFICTION:
        print("Nonfiction")
    elif category == BookCategory.SCIFI:
        print("Science Fiction")
    elif category == BookCategory.FANTASY:
        print("Fantasy")
    else:
        print("Unknown category")


# Using dot notation
display_book_category(BookCategory.FICTION)  # Output: Fiction

# Using constant name
display_book_category(BookCategory["NONFICTION"])  # Output: Nonfiction

# Using constant value
display_book_category(BookCategory(3))  # Output: Science Fiction
