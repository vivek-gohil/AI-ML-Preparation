import numpy as np

print("\nExercise 1 — Basic")
arr = np.array([10, 20, 30, 40, 50])
print(f"ndim : {arr.ndim}")
print(f"shape : {arr.shape}")

print("\nExercise 2 — 2D Array")
arr = np.array([[10,20,30],[40,50,60],[70,80,90]]);
print(f"ndim : {arr.ndim}")
print(f"shape : {arr.shape}")
print(f"Number of rows : {arr.shape[0]}")
print(f"Number of column : {arr.shape[1]}")
print(f"Total number of elements : {arr.size}")

print("\nExercise 3 — ML Dataset")

employees = np.array([
    [25,  2,  40000],
    [30,  5,  55000],
    [35,  8,  70000],
    [40, 12,  90000],
    [45, 15, 120000]
])
print(f"\nndim : {employees.ndim}")
print(f"\nshape : {employees.shape}")
print(f"\nNumber of samples : {employees.shape[0]}")
print(f"\nNumber of features : {employees.shape[1]}")
print(f"\nTotal number of values : {employees.size}")

print("\nExercise 4 — Think Like an ML Developer")
print("Suppose X.shape == (500, 10)")
print("\nNumber of samples : 500")
print("\nNumber of features :10")
print("\nTotal number of values : 5000 ")

print("\nExercise 5 — ndmin")
arr = np.array([1, 2, 3, 4], ndmin=3)

print(arr) # It will print complete array - all elements - as [[[[1,2,3,4]]]]
print(arr.ndim) # It will print the dimention of an array - 3 dim 
print(arr.shape) # It will print the shape of an array - (1,1,4)