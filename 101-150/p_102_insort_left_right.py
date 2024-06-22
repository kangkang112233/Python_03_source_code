# 日本語の説明:
# insort_left 関数は、ソート済みのシーケンスに値を挿入し、そのシーケンスの順序を維持するために使用されます。
# 値が既に存在する場合、左側に挿入されます。

# insort_right 関数も同様に、ソート済みのシーケンスに値を挿入しますが、値が既に存在する場合、右側に挿入されます。

# English Explanation:
# The insort_left function is used to insert a value into a sorted sequence
# while maintaining the order of the sequence. If the value already exists,
# it is inserted on the left.

# The insort_right function also inserts a value into a sorted sequence
# while maintaining the order of the sequence. If the value already exists,
# it is inserted on the right.

from bisect import insort_left, insort_right

# Create a sorted list of book publication years
book_years = [1984, 1990, 1995, 2000, 2005, 2010]

# Insert a new book year while maintaining order
insort_left(book_years, 2000)
print("After insort_left:")
print(book_years)

# Insert another new book year while maintaining order
insort_right(book_years, 2000)
print("After insort_right:")
print(book_years)
