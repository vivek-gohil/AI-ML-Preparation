# Imagine we have this dataset:
# Age   Experience   Salary
# 25       2         40000
# 30       5         55000
# 35       8         70000
# 40      12         90000

# Create a NumPy array for this dataset and answer:

# 1. How many samples?
# 2. How many features?
# 3. What is the shape?
# 4. How many total values?
# 5. What is the dtype?

import numpy as np

employees = np.array([
    [ 25, 2, 40000],
    [ 30, 5, 55000],
    [ 35, 8, 70000],
    [ 40, 12, 90000]
])

print(employees)
print("\nHow many samples")
print(employees.shape[0])

print("\nHow many features")
print(employees.shape[1])

print("\nWhat is the shape")
print(employees.shape)

print("\nHow many total values")
print(employees.size)

print("\nWhat is the dtype")
print(employees.dtype)
