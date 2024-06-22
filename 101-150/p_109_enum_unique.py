from enum import Enum, unique, auto

# 日本語の説明:
# `enum.unique` を使用すると、列挙型に重複する値を持つことができなくなります。
# 同じ値を持つ定数を定義しようとすると、`ValueError` が送出されます。

# English Explanation:
# Using `enum.unique` prevents an enumeration from having duplicate values.
# If you try to define constants with the same value, it raises a `ValueError`.


@unique
class BookCategory(Enum):
    FICTION = auto()
    NON_FICTION = auto()
    SCIENCE = auto()
    ART = auto()
    # Uncommenting the following line will raise a ValueError
    # DUPLICATE = 1


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
display_book_category(BookCategory.SCIENCE)
