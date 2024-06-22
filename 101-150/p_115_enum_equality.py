from enum import Enum


class BookCategory(Enum):
    FICTION = 1
    NON_FICTION = 2
    SCIENCE = 3


# 日本語の説明:
# 定数は Enum から派生した列挙型のインスタンスです。
# 同じ列挙型に定義された定数同士を `==` 演算子で比較する場合、
# 値が同じであれば True と判定されます。
#
# 異なる列挙型に定義された定数、または列挙型以外の値と比較した場合、
# 値が同じであっても False と判定されます。

# English Explanation:
# Constants are instances of enum types derived from Enum.
# When comparing constants defined in the same enum type
# using the `==` operator, they are considered equal if their values match.
#
# When comparing constants defined in different enum types
# or values outside of the enum type, they are considered unequal
# even if their values are the same.

fiction = BookCategory.FICTION
non_fiction = BookCategory.NON_FICTION

# Comparison within the same enum type
print(fiction == BookCategory.FICTION)  # True


# Comparison with a different enum type (assuming another enum exists)
class AnotherCategory(Enum):
    FICTION = 1


another_fiction = AnotherCategory.FICTION

print(fiction == another_fiction)  # False

# Comparison with non-enum value
print(fiction == 1)  # False
