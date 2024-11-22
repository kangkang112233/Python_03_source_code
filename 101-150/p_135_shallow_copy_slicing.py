# 日本語の説明:
# スライスを使用したリストの浅いコピーとは、リストの一部または全体をスライス記法を用いて新しいリストとしてコピーする方法です。
# この方法では、元のリストと同じオブジェクトへの参照が維持されるため、
# 元のリストのネストされた要素を変更すると、コピーにも影響が及びます。

# English Explanation:
# Shallow copying a list using slicing means creating a new list by using slice notation to copy part or all of the original list.
# This method maintains references to the same objects in the original list, so changes to nested elements in the original list affect the copy as well.

# Define a list of books
original_books = ["Book A", "Book B", ["Book C1", "Book C2"]]

# Create a shallow copy of the list using slicing
copied_books = original_books[:]

# Modify the copied list
copied_books[2][0] = "Modified Book C1"

# Print original and copied lists to show the effect of shallow copy
print("Original books:", original_books)
print("Copied books:", copied_books)
