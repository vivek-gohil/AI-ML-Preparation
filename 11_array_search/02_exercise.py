import numpy as np

# Exercise 1 — Find matching indexes
arr = np.array([12, 25, 12, 40, 12, 55])

# Find all indexes where the value is 12
print("Find all indexes where the value is 12")

x = np.where(arr == 12)

print(x)

print("-" * 80)

# Exercise 2 — Find values greater than 50
print("Exercise 2 — Find values greater than 50")

marks = np.array([35, 78, 45, 92, 60, 28])

x = np.where(marks > 50)

print(x)

print("-" * 80)

# Exercise 3 — Sorted insertion
print("Exercise 3 — Sorted insertion")

arr = np.array([10, 20, 30, 40, 50])

# Find the insertion position for 35
print("Find the insertion position for 35")
x = np.searchsorted(arr, 35)

print(x)


print("-" * 80)

# Find the insertion positions for [15, 25, 45]
print("Find the insertion positions for [15, 25, 45]")

arr = np.array([10, 20, 30, 40, 50])

x = np.searchsorted(arr, [15, 25, 45])

print(x)

print("-" * 80)

# Exercise 4 — ML-oriented practice
# Given this array of model prediction scores:
scores = np.array([0.25, 0.85, 0.45, 0.95, 0.70])
x = np.where(scores >= 0.80)

print(x)
