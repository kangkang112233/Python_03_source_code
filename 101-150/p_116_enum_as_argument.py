from enum import Enum


class BookCategory(Enum):
    FICTION = 1
    NON_FICTION = 2
    SCIENCE = 3


def display_book_category(category):
    """
    Display the book category.
    :param category: BookCategory Enum instance
    """
    # 日本語の説明:
    # 指定されたカテゴリを表示する関数です。
    # :param category: BookCategory Enum のインスタンス
    #
    # English Explanation:
    # Function to display the specified category.
    # :param category: BookCategory Enum instance

    if not isinstance(category, BookCategory):
        raise ValueError("Invalid category. Must be an instance of BookCategory Enum.")

    print(f"The selected book category is: {category.name}")


# Valid usage
display_book_category(BookCategory.FICTION)  # The selected book category is: FICTION

# Invalid usage (will raise ValueError)
try:
    display_book_category(1)
except ValueError as e:
    print(
        f"Error: {e}"
    )  # Error: Invalid category. Must be an instance of BookCategory Enum.
