import numpy as np

print("\nExercise 1 — Basic Reshape")
arr = np.array([1, 2, 3, 4, 5, 6])
print("\nReshape it into 2 rows × 3 columns")
newarr = arr.reshape(2,3)
print("Orignal Array")
print(arr)
print(arr.shape)
print("Reshaped Array")
print(newarr)
print(newarr.shape)

print("\nExercise 2 — 3D Reshape")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Reshape it into 2 block 3 rows per block 2 columns per row")
newarr = arr.reshape(2,3,2)
print(arr)
print(arr.shape)
print("Reshaped Array")
print(newarr)
print(newarr.shape)

print("\nExercise 3 — Check the Number of Elements")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr.reshape(3, 4) # working
arr.reshape(2, 6) # working
arr.reshape(4, 3) # working
# arr.reshape(5, 3) # Not working bcos it will try to reshape the array 5 rows and 3 colums which is 5 * 3 = 15 but our orignal arr contains only 12 elements 

print("\nExercise 4 — Unknown Dimension")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1) # This will reshape the array to (2, 2, 2)
print(newarr)
print(newarr.shape)

print("\nExercise 5 — Flattening")
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("Convert it into a 1-D array using:reshape(-1)")
arr.reshape(-1)

print("\nExercise 6 — ML-Oriented")
data = np.array([
    [25, 2, 40000],
    [30, 5, 55000],
    [35, 8, 70000],
    [40, 12, 90000]
])

print(data)
print(data.shape)
print("\nQ1. How many samples?")
print(data.shape[0])
print("\nQ2. How many features?")
print(data.shape[1])
print("Now reshape the same data into:(2, 6)")
newdata = data.reshape(2,6);
print(newdata)
print(newdata.shape)
print("\nWill the reshape work : Yes")
print("\n Why?")
print("Bcos the number of elements are remain same 6*2 = 12 and orignal array shape is 4*3 = 12")
print("\nHow many total values are there before and after")
print("it is same 12 values")

print("\nExercise 7 — ML Thinking")
print("Suppose X = np.arange(20)")
x = np.arange(20)
print(x)
print("Valid reshape shapes are")
x.reshape(4,5) # 4*5 = 20 reshape will work
x.reshape(5,4) # 5*5 = 20 reshape will work
x.reshape(10,2) # 10*2 = 20 reshape will work
x.reshape(2,10) # 2*10 = 20 reshape will work


#x.reshape(3,6) will not work bocs 3*6 = 18 
#x.reshape(4,6) will not work bocs 4*6 = 24 
x.reshape(2, 5, 2)  #  2*5*2 = 20 reshape will work


X = np.arange(24)

print(X)
print(X.shape)

X = X.reshape(6, 4)

print(X)
print(X.shape)1