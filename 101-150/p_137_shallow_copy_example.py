# list() は、リストの浅いコピーを作成するメソッドです。元のリストの要素の参照を新しいリストにコピーします。
# つまり、元のリストと新しいリストの間で要素は共有されます。

# `list()` is a method to create a shallow copy of a list. It copies the references of the elements from the
# original list to the new list. Thus, the elements are shared between the original and the new list.

# dict() は、辞書の浅いコピーを作成するメソッドです。元の辞書のキーと値の参照を新しい辞書にコピーします。
# つまり、元の辞書と新しい辞書の間でキーと値は共有されます。

# `dict()` is a method to create a shallow copy of a dictionary. It copies the references of the keys and values
# from the original dictionary to the new dictionary. Thus, the keys and values are shared between the original and the new dictionary.

# set() は、セットの浅いコピーを作成するメソッドです。元のセットの要素の参照を新しいセットにコピーします。
# つまり、元のセットと新しいセットの間で要素は共有されます。

# `set()` is a method to create a shallow copy of a set. It copies the references of the elements from the original set to the new set.
# Thus, the elements are shared between the original and the new set.

# Application: Library management system to demonstrate shallow copy of list, dict, and set

# Creating a shallow copy of a list
original_list = ["Book1", "Book2", "Book3"]
shallow_copied_list = list(original_list)
print("Original list:", original_list)
print("Shallow copied list:", shallow_copied_list)

# Modifying the original list
original_list[0] = "NewBook1"
print("Modified original list:", original_list)
print("Shallow copied list after modification:", shallow_copied_list)

# Creating a shallow copy of a dictionary
original_dict = {"title": "Book1", "author": "Author1"}
shallow_copied_dict = dict(original_dict)
print("\nOriginal dictionary:", original_dict)
print("Shallow copied dictionary:", shallow_copied_dict)

# Modifying the original dictionary
original_dict["title"] = "NewBook1"
print("Modified original dictionary:", original_dict)
print("Shallow copied dictionary after modification:", shallow_copied_dict)

# Creating a shallow copy of a set
original_set = {"Book1", "Book2", "Book3"}
shallow_copied_set = set(original_set)
print("\nOriginal set:", original_set)
print("Shallow copied set:", shallow_copied_set)

# Modifying the original set
original_set.remove("Book1")
print("Modified original set:", original_set)
print("Shallow copied set after modification:", shallow_copied_set)
