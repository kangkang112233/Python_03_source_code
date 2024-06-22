# 日本語の説明:
# OrderedDictは挿入順序を保持する辞書です。
# `move_to_end` メソッドは指定したキーを辞書の末尾または先頭に移動します。
# `popitem` メソッドは指定した位置（末尾または先頭）から要素を取り出します。

# English Explanation:
# OrderedDict is a dictionary that maintains the insertion order.
# The `move_to_end` method moves the specified key to the end or beginning of the dictionary.
# The `popitem` method pops an element from the specified position(end or beginning).

from collections import OrderedDict

# Create an OrderedDict
ordered_dict = OrderedDict()
ordered_dict["apple"] = 1
ordered_dict["banana"] = 2
ordered_dict["cherry"] = 3

print("Original OrderedDict:")
print(ordered_dict)

# Move 'banana' to the end
ordered_dict.move_to_end("banana")
print("After moving 'banana' to the end:")
print(ordered_dict)

# Move 'banana' to the beginning
ordered_dict.move_to_end("banana", last=False)
print("After moving 'banana' to the beginning:")
print(ordered_dict)

# Pop item from the end
popped_item_end = ordered_dict.popitem()
print("After popping item from the end:")
print(f"Popped item: {popped_item_end}")
print(ordered_dict)

# Pop item from the beginning
popped_item_beginning = ordered_dict.popitem(last=False)
print("After popping item from the beginning:")
print(f"Popped item: {popped_item_beginning}")
print(ordered_dict)
