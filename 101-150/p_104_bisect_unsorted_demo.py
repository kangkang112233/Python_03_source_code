import bisect

# Create an unsorted list of numbers
unsorted_seq = [1001, 1000, 1002, 1001]
num = 1001

# Display the original unsorted sequence
print("Original unsorted sequence:")
print(unsorted_seq)

# Attempt to insert using insort_left and show the sequence and index
index_left = bisect.bisect_left(unsorted_seq, num)
bisect.insort_left(unsorted_seq, num)
print(f"After insort_left at index {index_left}:")
print(unsorted_seq)  # May not insert in the correct position due to unsorted data

# Reset the sequence to original unsorted
unsorted_seq = [1001, 1000, 1002, 1001]

# Attempt to insert using insort_right and show the sequence and index
index_right = bisect.bisect_right(unsorted_seq, num)
bisect.insort_right(unsorted_seq, num)
print(f"After insort_right at index {index_right}:")
print(unsorted_seq)  # May not insert in the correct position due to unsorted data
