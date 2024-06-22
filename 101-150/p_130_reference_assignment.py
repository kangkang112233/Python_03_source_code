# 日本語の説明:
# 変数への代入のみを行うと、参照が作成されます。
# 同じオブジェクトを参照しているため、一方を変更すると他方も変更されます。

# English Explanation:
# When assigning to a variable, a reference is created.
# Since both refer to the same object, modifying one will also modify the other.

# Example demonstrating variable assignment and reference creation
book_list_original = ["Book A", "Book B", "Book C"]
book_list_reference = book_list_original

# Modify the reference list
book_list_reference.append("Book D")

# Both lists are affected
print("Original book list:")
print(book_list_original)

print("Reference book list:")
print(book_list_reference)
