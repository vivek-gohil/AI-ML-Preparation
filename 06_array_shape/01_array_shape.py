# The shape of an array is the number of elements in each dimension.

import numpy as np;
print("/nPrint the shape of a 2-D array:")
arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)

print("\nCreate an array with 5 dimensions using ndmin using vector with values 1,2,3,4 and that last dimension has value 4")
arr = np.array([1,2,3,4],ndmin=5);
print(arr)
print(arr.shape)