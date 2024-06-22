# 日本語の説明:
# default_factory引数にintを指定すると、デフォルト値が数値の0となります。
# 同様にdict、list、setを指定すると、空の辞書、リスト、セットがデフォルト値となるので便利です。

# English Explanation:
# When the default_factory argument is specified as int, the default value will be 0.
# Similarly, if specified as dict, list, or set,
# the default value will be an empty dictionary, list, or set, making it very convenient.

from collections import defaultdict

# Using int as the default factory
int_dict = defaultdict(int)
int_dict["apple"] += 1
int_dict["banana"] += 2
print(f"Count for 'orange' (int): {int_dict['orange']}")
print("All int counts:", dict(int_dict))

# Using list as the default factory
list_dict = defaultdict(list)
list_dict["fruits"].append("apple")
list_dict["fruits"].append("banana")
print(f"List for 'vegetables': {list_dict['vegetables']}")
print("All lists:", dict(list_dict))

# Using set as the default factory
set_dict = defaultdict(set)
set_dict["fruits"].add("apple")
set_dict["fruits"].add("banana")
print(f"Set for 'vegetables': {set_dict['vegetables']}")
print("All sets:", dict(set_dict))

# Using dict as the default factory
dict_dict = defaultdict(dict)
dict_dict["fruits"]["apple"] = 1
dict_dict["fruits"]["banana"] = 2
print(f"Dict for 'vegetables': {dict_dict['vegetables']}")
print("All dicts:", dict(dict_dict))
