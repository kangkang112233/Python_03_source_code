import bisect

# Create a sorted list of numbers
seq = [1000, 1001, 1001, 1002]
num = 1001

# Display the original sequence
print("Original sequence:")
print(seq)

# Insert using insort_left and show index
index_left = bisect.bisect_left(seq, num)
bisect.insort_left(seq, num)
print(f"After insort_left at index {index_left}:")
print(seq)  # Should insert before the existing 1001

# Reset the sequence to original
seq = [1000, 1001, 1001, 1002]

# Insert using insort_right and show index
index_right = bisect.bisect_right(seq, num)
bisect.insort_right(seq, num)
print(f"After insort_right at index {index_right}:")
print(seq)  # Should insert after the existing 1001s
