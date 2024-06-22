# 日本語の説明:
# defaultdictでデータのセットをグループ化する方法を説明します。
# defaultdictにsetを指定することで、
# 存在しないキーにアクセスすると空のセットがデフォルト値として返されます。
# これにより、データのグループ化が簡単に行えます。

# English Explanation:
# This explains how to use defaultdict to group data sets.
# By specifying set as the default factory function for defaultdict,
# accessing non-existent keys returns an empty set as the default value,
# making data grouping very easy.

from collections import defaultdict

# Create a defaultdict with default type as set
grouped_data = defaultdict(set)

# Add some data to groups
grouped_data["fruits"].add("apple")
grouped_data["fruits"].add("banana")
grouped_data["vegetables"].add("carrot")
grouped_data["vegetables"].add("lettuce")

# Access a non-existent group
print(
    f"Group 'dairy': {grouped_data['dairy']}"
)  # Initializes 'dairy' with an empty set

# Print all grouped data
print("All grouped data:")
for group, items in grouped_data.items():
    print(f"{group}: {items}")
