# Split an array containing numbers from 10 to 90 into 4 parts using np.array_split(). Print each part and its shape.
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

# Split the array into 4 parts
print("Split the array into 4 parts")
result = np.array_split(arr, 4)

# Print each subarray and its shape
for subarray in result:
    print(subarray)
    print(subarray.shape)

print("-" * 80)

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

# Split the array into 3 equal parts
print("Split the array into 3 equal parts")
result = np.split(arr, 3)

# Print each subarray
for subarray in result:
    print(subarray)

print("-" * 80)

arr = np.array([[10, 20], [30, 40], [50, 60], [70, 80], [90, 100], [110, 120]])

# Split into 2 arrays along axis 0
print("Split into 2 arrays along axis 0")
result = np.array_split(arr, 2, axis=0)

# Print each subarray and its shape
for subarray in result:
    print(subarray)
    print("Shape:", subarray.shape)
