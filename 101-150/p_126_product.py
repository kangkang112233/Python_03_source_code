from itertools import product

# 日本語の説明:
# `product` 関数は、指定されたイテラブルのデカルト積を計算し、
# すべての組み合わせを生成します。これは、異なるリストやシーケンスの
# すべての可能な組み合わせを見つけるのに便利です。

# English Explanation:
# The `product` function computes the Cartesian product of the specified
# iterables, generating all combinations. It is useful for finding all
# possible combinations of different lists or sequences.

# Example lists of book categories and authors
categories = ["Fiction", "Science", "History"]
authors = ["Author A", "Author B", "Author C"]

# Generate all combinations of categories and authors
combinations = list(product(categories, authors))

# Print the combinations
for combo in combinations:
    print(combo)
