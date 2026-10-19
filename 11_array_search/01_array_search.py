# Searching Arrays
# You can search an array for a certain value, and return the indexes that get a match.

# To search an array, use the where() method.
# Find the indexes where the value is 4:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

print("Find the indexes where the value is 4:")
x = np.where(arr == 4)

print(x)

print("-" * 80)


# Find the indexes where the values are odd:

arr = np.array([10, 14, 93, 41, 8, 7])

print("Find the indexes where the values are odd:")
x = np.where(arr % 2 == 1)

print(x)

print("-" * 80)

# Search Sorted
# There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.

# Find the indexes where the value 7 should be inserted:
arr = np.array([4,5,6, 8, 9])

print("Find the indexes where the value 7 should be inserted")
x = np.searchsorted(arr, 7)

print(x) # print 3

print("-" * 80)

# Search From the Right Side
arr = np.array([4,5,6, 8, 9, 20])

print("Search From the Right Side")
x = np.searchsorted(arr, 7, side="right")

print(x) # print 3

print("-" * 80)
# Multiple Values
# To search for more than one value, use an array with the specified values.
# Find the indexes where the values 2, 4, and 6 should be inserted:

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print("Find the indexes where the values 2, 4, and 6 should be inserted:")
print(x)