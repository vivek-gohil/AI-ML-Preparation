import numpy as np
arr = np.array([1,2,3,4]);

print("Get the data type of an array object:")
print(arr.dtype)

print("Get the data type of an array containing strings:")
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

print("Creating Arrays With a Defined Data Type")
print("Create an array with data type string:")
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

# i = integer
# b = boolean
# u = unsigned integer
# f = float
# c = complex float
# m = timedelta
# M = datetime
# O = object
# S = string
# For i, u, f, S, and U, you can write a number after the type to specify its size.
# i4  → integer, 4 bytes
# u4  → unsigned integer, 4 bytes
# f4  → float, 4 bytes
# S10 → byte string, 10 bytes
# U10 → Unicode string, 10 characters

# | NumPy dtype     | Meaning        | Example   |
# | --------------- | -------------- | --------- |
# | `int8`          | 8-bit integer  | `10`      |
# | `int16`         | 16-bit integer | `10`      |
# | `int32`         | 32-bit integer | `10`      |
# | `int64`         | 64-bit integer | `10`      |
# | `float16`       | 16-bit decimal | `10.5`    |
# | `float32`       | 32-bit decimal | `10.5`    |
# | `float64`       | 64-bit decimal | `10.5`    |
# | `bool`          | Boolean        | `True`    |
# | `str` / Unicode | Text           | `"Vivek"` |



# Change data type from float to integer by using 'i' as parameter value:
print("\nChange data type from float to integer by using 'i' as parameter value:")
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype("i");
print(arr)
print(arr.dtype)
print(newarr)
print(newarr.dtype)

# Change data type from float to integer by using int as parameter value:
print("\nChange data type from float to integer by using 'i' as parameter value:")
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int);
print(arr)
print(arr.dtype)
print(newarr)
print(newarr.dtype)

print("\nChange data type from integer to boolean:")
arr = np.array([1, 0, 3])
newarr = arr.astype(bool);
print(arr)
print(arr.dtype)
print(newarr)
print(newarr.dtype)

