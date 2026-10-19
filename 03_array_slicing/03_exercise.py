import numpy as np

students = np.array([
    [101,  "Rahul",  85,  90,  88],
    [102,  "Amit",   78,  82,  80],
    [103,  "Priya",  92,  95,  94],
    [104,  "Neha",   88,  85,  90],
    [105,  "Vikas",  75,  80,  78],
    [106,  "Sneha",  95,  93,  96]
])

print("\nLevel 1 — Basic indexing")
print("\n1. Get the complete first student.")
print(students[0])

print("\n2. Get the name of the third student.")
print(students[2,1])

print("\n3. Get the Science marks of the fourth student.")
print(students[3,-2])

print("\n4. Get the English marks of the last student using negative indexing.")
print(students[-1,-1])

print("\nLevel 2 — Slicing rows")
print("\n5. Get the first three students.")
print(students[:3][2])