# 日本語の説明:
# `itemgetter` 関数は、指定したインデックスまたはキーに基づいて要素を取得するための関数を生成します。
# この関数は、`sorted` 関数の `key` パラメータに渡して、リストやタプルの特定の要素に基づいて
# ソートを行うために使用できます。例えば、タプルのリストをインデックス 2 に基づいてソートすることができます。

# English Explanation:
# The `itemgetter` function generates a function that retrieves elements based on specified indices or keys.
# This function can be passed to the `key` parameter of the `sorted` function to sort lists or tuples based
# on specific elements. For example, it can sort a list of tuples based on index 2.

from operator import itemgetter

# Example data: list of tuples with 3 elements each
data = [(1, 40, 200), (3, 10, 100), (2, 20, 300), (1, 30, 300)]

# Sort without specifying the key (compares elements in index order)
sorted_data_default = sorted(data)
print("Sorted data without key specified:")
print(sorted_data_default)

# Sort by index 2
sorted_data_by_index_2 = sorted(data, key=itemgetter(2))
print("Sorted data by index 2:")
print(sorted_data_by_index_2)

# Sort by index 2, then by index 0 if elements at index 2 are the same
sorted_data_by_index_2_then_0 = sorted(data, key=itemgetter(2, 0))
print("Sorted data by index 2, then by index 0:")
print(sorted_data_by_index_2_then_0)
