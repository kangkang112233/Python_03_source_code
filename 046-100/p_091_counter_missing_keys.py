# 日本語の説明:
# 辞書で存在しないキーを指定して値を取得しようとするとKeyErrorが発生しますが、
# Counterでは0を返します。また、値が存在しない場合は初期値に0が設定されるので、
# forループで発生回数を数えるとき初期化が不要です。

# English Explanation:
# In a dictionary, attempting to access a non-existent key raises a KeyError,
# but in a Counter, it returns 0. Additionally, if a value does not exist, it defaults to 0,
# so there's no need for initialization when counting occurrences in a for loop.

from collections import Counter

# Example dictionary
book_counts_dict = {"The Catcher in the Rye": 4, "To Kill a Mockingbird": 2}

# Attempt to access a non-existent key in a dictionary
try:
    print(book_counts_dict["1984"])
except KeyError:
    print("KeyError: '1984' does not exist in the dictionary")

# Example Counter
book_counts_counter = Counter({"The Catcher in the Rye": 4, "To Kill a Mockingbird": 2})

# Access a non-existent key in a Counter
print(book_counts_counter["1984"])  # Outputs 0 instead of raising an error

# Counting occurrences without initialization
new_books = ["1984", "1984", "To Kill a Mockingbird", "The Great Gatsby"]
for book in new_books:
    book_counts_counter[book] += 1

print(book_counts_counter)
