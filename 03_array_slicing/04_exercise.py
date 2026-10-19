import numpy as np

houses = np.array([
    [800, 1, 15, 45],
    [1000, 2, 10, 60],
    [1200, 2, 8, 72],
    [1500, 3, 5, 95],
    [1800, 3, 3, 120],
    [2200, 4, 2, 155]
])
print("\nPart 1\n")
print(houses);
print(f"Dimensions : {houses.ndim}")
print(f"Shape : {houses.shape}")
print(f"Size : {houses.size}")
print(f"Data Type : {houses.dtype}")

print("\nPart 2\n")
print("How many samples are there?")
print(houses.shape[0])
print("How many features are there?")
print(houses.shape[1])
print("What is the shape?")
print(houses.shape)
print("How many total values are there?")
x = houses[:,:3]
print(x)
print(x.shape)
print("What is the target variable?")
y = houses[:,3]
print(y)
print(y.shape)

print("\nPart 4\n")
print("Extract the first house")
print(houses[0])
print("Extract the last house")
print(houses[-1])
print("Extract all house prices")
print(houses[:,-1])
print("Extract the first three houses")
print(houses)
print()
print(houses[:3])

print("\nBonus Challenge\n")
print("Extract only the sized column")
print(houses[:,0])
print("Extract only the bedrooms column")
print(houses[:,1])

