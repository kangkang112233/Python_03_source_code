from enum import Enum


class BookCategory(Enum):
    FICTION = 1
    NONFICTION = 2
    SCIFI = 3
    FANTASY = 4


# 日本語の説明:
# 列挙型の定数の名前と値を取得するには、`.name` 属性と `.value` 属性を使用します。
# `.name` 属性は定数の名前を返し、 `.value` 属性は定数の値を返します。

# English Explanation:
# To get the name and value of an enumeration constant, use the `.name` and `.value` attributes.
# The `.name` attribute returns the constant's name, while the `.value` attribute returns the constant's value.


# Function to display book category details
def display_book_category_details(category):
    print(f"Category Name: {category.name}")
    print(f"Category Value: {category.value}")


# Example usage
display_book_category_details(BookCategory.FICTION)  # Output: Category Name: FICTION, Category Value: 1
display_book_category_details(BookCategory.SCIFI)  # Output: Category Name: SCIFI, Category Value: 3
