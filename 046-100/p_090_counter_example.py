# 日本語の説明:
# `Counter` オブジェクトは、要素の出現回数をカウントするためのコレクションです。
# 文字列やリストなどの反復可能オブジェクトを渡すと、各要素の出現回数をカウントします。
# 例えば、文字列の各文字の出現回数やリストの各要素の出現回数をカウントすることができます。

# English Explanation:
# The `Counter` object is a collection for counting the occurrences of elements.
# When given an iterable object such as a string or list, it counts the occurrences of each element.
# For example, it can count the occurrences of each character in a string or each element in a list.

# Shuffle the list to randomize the order
import random

from collections import Counter

# Create a Counter object from a string
c = Counter("supercalifragilisticexpialidocious")
print(c)  # Counter object showing the count of each character

# Create a list with repeated elements
li = ["spam"] * 100 + ["ham"] * 90 + ["egg"] * 110
print(len(li))  # Length of the list should be 300

random.shuffle(li)

# Create a Counter object from the list
li_counter = Counter(li)
print(li_counter)  # Counter object showing the count of each list element
