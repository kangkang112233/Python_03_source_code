# 日本語の説明:
# `itemgetter` 関数をソートの `key` に使用する方法を説明します。
# 3 要素のタプルをソートする例を見ていきます。タプルのソートを `key` 指定せずに行うと、
# インデックスの要素から順番に比較します。
# `itemgetter` 関数を使うと、リストやタプルのソートに使う要素をインデックス値で指定できます。
# ここでは、`key` 指定なしでソートを実行し、
# 次にインデックス 2 でソートする方法を実行し、最後にインデックス 2 で比較要素が同じ場合には
# インデックス 0 でソートする方法を見ていきます。

# English Explanation:
# Explains how to use the `itemgetter` function as the `key` for sorting.
# An example of sorting a tuple with 3 elements is provided.
# Without specifying `key`, elements are compared in index order.
# The `itemgetter` function allows specifying sorting elements by index.
# First, sorting without `key`, then by index 2, and finally by index 0
# when index 2 elements are the same, are demonstrated.

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
