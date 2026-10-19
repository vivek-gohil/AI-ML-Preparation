import numpy as np;

arr = np.array([10,20,30,40,50]);

print(arr)
print(arr.dtype)

arr = np.array([10.5, 20.5, 30.5, 40.5])
print(arr)
print(arr.dtype)

arr = np.array([10, 20, 30, 40],dtype=np.float32)
print(arr)
print(arr.dtype)

arr = np.array([10, 20, 30, 40])
newarr = arr.astype(float)
print(arr)
print(arr.dtype)
print(newarr)
print(newarr.dtype)

houses = np.array([
    [800, 1, 15, 45],
    [1000, 2, 10, 60],
    [1200, 2, 8, 72],
    [1500, 3, 5, 95],
    [1800, 3, 3, 120],
    [2200, 4, 2, 155]
])

print("\nWhat is the original dtype : ")
print(houses.dtype)

print("\nConvert the complete array to float64 : ")
new_houses = houses.astype(float)
print(new_houses)
print("\nWhat is new dtype")
print(new_houses.dtype)
print("\nDid the shape change?")
print(houses.shape)
print(new_houses.shape)

print("New House Values - Float64")
print(new_houses)
