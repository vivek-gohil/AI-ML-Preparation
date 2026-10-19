#Reshaping Arrays

#Reshape does NOT change the data — it changes how we organize/view the data
#Reshaping means changing the shape of an array
#The shape of an arrays is the number of elements in each dimension.
#By reshaping we can add or remove dimensions or change number of elements in each dimension

#Reshape from 1-D to 2-D
#Convert the following 1-D array with 12 elements into a 2-D array.
import numpy as np
print("\nReshape from 1-D to 2-D")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4,3);
print(arr)
print(arr.shape)
print(newarr)
print(newarr.shape)

print("\nReshape From 1-D to 3-D")
newarr = arr.reshape(2,3,2);
print(arr)
print(arr.shape)
print(newarr)
print(newarr.shape)

# Can We Reshape Into any Shape?
# Yes, as long as the elements required for reshaping are equal in both shapes.
print("\nCheck if the returned array is a copy or a view:")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2,4).base)
print("\nThe example above returns the original array, so it is a view.")

# Unknown Dimension
# You are allowed to have one unknown dimension
# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method
# pass -1 as the value and numPy will calculate number for you
print("\nUnknown Dimension")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

print("\n Flattening the arrays")
print("Convert the array into a 1D array:")
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(arr)
print(newarr)
