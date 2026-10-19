# Iterating Arrays
# Iterating means going through elements one by one.

import numpy as np
# Iterate on the elements of the following 1-D array:
arr = np.array([1, 2, 3])
print("Iterate on the elements of the following 1-D array")
for i in arr:
    print(i)

# Iterating 2-D Arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("\nIterating 2-D Arrays")
for x in arr:
  print(x)
  
# Iterating 3-D Arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("\nIterating 3-D Arrays")
for x in arr:
  print(x)
  
# Iterate down to the scalars:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("\nIterate down to the scalars:")
for i in arr:
    for j in i:
        for k in j:
            print(k)
            
# Iterating Arrays Using nditer()
# Iterating on Each Scalar Element
# In basic for loops, iterating through each scalar of an array we need to use n for loops which can be difficult to write for arrays with very high dimensionality.
print("\nIterating Arrays Using nditer()")
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for i in np.nditer(arr):
    print(i)
    
# Iterating Array With Different Data Types
print("\nIterating Array With Different Data Types")
arr = np.array([1, 2, 3])
for i in np.nditer(arr,flags=['buffered'],op_dtypes=['S']):
    print(i)
    
#Iterating With Different Step Size
print("\nIterating With Different Step Size")
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x)

# Enumerated Iteration Using ndenumerate()
# Enumeration means mentioning sequence number of somethings one by one.
# Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.
print("\nEnumerated Iteration Using ndenumerate()")
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for index,x in np.ndenumerate(arr):
    print(f"index : {index} value  : {x}")
