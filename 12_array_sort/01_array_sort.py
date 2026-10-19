# Sorting Arrays
# Sorting means putting elements in an ordered sequence.

# Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.

# The NumPy ndarray object has a function called sort(), that will sort a specified array.

# Sort the array:
# Note: This method returns a copy of the array, leaving the original array unchanged.
import numpy as np

print("Sort the array:")
arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

print("-" * 80)
# Sort the array alphabetically:
print("Sort the array alphabetically:")

arr = np.array(["banana", "cherry", "apple"])

print(np.sort(arr))

print("-" * 80)

# Sort a boolean array:

print("Sort a boolean array:")
arr = np.array([True, False, True])

print(np.sort(arr))
