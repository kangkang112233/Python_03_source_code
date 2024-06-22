from itertools import combinations, combinations_with_replacement

# 日本語の説明:
# `combinations` 関数は、指定されたイテラブルから長さ r のすべての組み合わせを生成します。
# `combinations_with_replacement` 関数は、指定されたイテラブルから長さ r の重複を許すすべての組み合わせを生成します。

# English Explanation:
# The `combinations` function generates all combinations of length r from the specified iterable.
# The `combinations_with_replacement` function generates all combinations of length r from the specified iterable, allowing repeated elements.

# Example list of book titles
books = ["Book A", "Book B", "Book C"]

# Generate all combinations of length 2
all_combinations = list(combinations(books, 2))
print("Combinations of books (length 2):")
for combo in all_combinations:
    print(combo)

# Generate all combinations with replacement of length 2
all_combinations_with_replacement = list(combinations_with_replacement(books, 2))
print("\nCombinations with replacement of books (length 2):")
for combo in all_combinations_with_replacement:
    print(combo)
