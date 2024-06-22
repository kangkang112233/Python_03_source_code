from enum import Enum

# 日本語の説明:
# `enum.unique` を使用しない場合、列挙型に重複する値を持つことができます。

# English Explanation:
# Without using `enum.unique`, you can have multiple enumeration members with the same value.


class BookCategory(Enum):
    FICTION = 1
    NON_FICTION = 2
    SCIENCE = 3
    ART = 4
    DUPLICATE_FICTION = 1  # 重複する値


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
    elif category == BookCategory.DUPLICATE_FICTION:
        print("Duplicate Fiction Category")
    else:
        print("Unknown Category")


# Using the enumeration
display_book_category(BookCategory.FICTION)
display_book_category(BookCategory.DUPLICATE_FICTION)
