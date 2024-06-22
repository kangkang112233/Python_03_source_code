# 日本語の説明:
# `Counter` オブジェクト同士の計算ができます。
# `+`、`-` 演算子による足し算、引き算では、
# 同じキーの値を加減算します。
# さらに `&`、`|` 演算子による積集合と和集合の演算も可能で、
# その場合は対応するカウンターの最小値または最大値を返します。
# なお、演算の結果、カウンターが0以下になる場合は結果が出力されません。

# English Explanation:
# `Counter` objects can be computed together.
# Using the `+` and `-` operators adds or subtracts the values of the same keys.
# The `&` and `|` operators compute the intersection and union,
# returning the minimum or maximum values of the corresponding counters.
# Note that if the result of the operation is 0 or less, the result is not output.

from collections import Counter

# Create two Counter objects
counter1 = Counter(["book1", "book2", "book3", "book1", "book2"])
counter2 = Counter(["book2", "book3", "book4", "book2", "book4", "book4"])

# Addition
counter_add = counter1 + counter2
print("Addition of Counters:")
print(counter_add)

# Subtraction
counter_sub = counter1 - counter2
print("Subtraction of Counters:")
print(counter_sub)

# Intersection (minimum counts)
counter_and = counter1 & counter2
print("Intersection of Counters:")
print(counter_and)

# Union (maximum counts)
counter_or = counter1 | counter2
print("Union of Counters:")
print(counter_or)
