# Define a list of books
original_books = ["Book A", "Book B", ["Book C1", "Book C2"]]

# Create a shallow copy of the list using slicing
copied_books = original_books[:]

# Modify the copied list at the top level
copied_books[0] = "Modified Book A"

# Print original and copied lists to show the effect of shallow copy
print("Original books:", original_books)
print("Copied books:", copied_books)
# 如果你只是对浅拷贝的列表中的顶层元素进行更改，而不涉及嵌套的子元素，原始列表将不会受到影响。
