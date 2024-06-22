# 日本語の説明:
# 通常の辞書オブジェクトでは、存在しないキーを参照するとKeyError例外が発生します。
# defaultdictは辞書から派生したクラスですが、存在しないキーを参照したときにデフォルト値が返されます。

# English Explanation:
# In a standard dictionary object, referencing a non-existent key raises a KeyError exception.
# However, defaultdict is a class derived from the dictionary,
# which returns a default value when referencing a non-existent key.

from collections import defaultdict

# Create a defaultdict with default type as int
book_counts = defaultdict(int)

# Add some book counts
book_counts["1984"] += 1
book_counts["To Kill a Mockingbird"] += 2

# Access a non-existent key
print(f"Count for 'The Great Gatsby': {book_counts['The Great Gatsby']}")

# Print all book counts
print("All book counts:")
print(dict(book_counts))
