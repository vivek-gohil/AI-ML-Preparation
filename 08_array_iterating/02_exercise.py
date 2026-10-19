import numpy as np

print("\nExercise 1 — 1-D Iteration")
arr = np.array([10, 20, 30, 40, 50])
for x in arr:
    print(x)
    
print("How many iterations will the loop perform = 5")

print("What will be the first value : 10")
print(arr[0])
print("What will be the first value : 50")
print(arr[-1])

print("\nExercise 2 — 2-D Iteration")
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

for x in arr:
    print(x)
    
print("How many iterations = 2")
print("What is the value of x during the first iteration")
print(arr[0])
print("What is the value of x during the second iteration?")
print(arr[1])
print("Is x a scalar or an array : its an array")

print("\nExercise 3 — nditer()")
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

for x in np.nditer(arr):
    print(x)

print("How many values will be printed : all (scalar) value will be printed")
print("What is the first value : 10")
print("What is the last value : 60")
print("Why does nditer() print individual values whereas the normal for loop printed rows : iterating through each scalar of an array we need to use n for loops which can be difficult to write for arrays with very high dimensionality")

print("\nExercise 4 — ML-oriented")
x = np.array([
    [25, 50000, 5],
    [30, 60000, 7],
    [35, 75000, 10],
    [40, 90000, 12]
])

print(x.shape) # (4 ,3)
print(f"How many samples {x.shape[0]}")
print(f"How many features {x.shape[1]}")
print("What will this print?") # it will print the each row 
for sample in x:
    print(sample)
print("How many times will the loop execute : 4")

print("\nExercise 5 — ndenumerate()")
arr = np.array([
    [10, 20],
    [30, 40]
])

# below for loop will print the index and the value on that index bcos we are iterating array using ndenumerate method
for index, value in np.ndenumerate(arr):
    print(index, value)