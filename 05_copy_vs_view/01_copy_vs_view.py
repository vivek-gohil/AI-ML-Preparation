# The Difference Between Copy and View
# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

# Copy = The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
# View = The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.copy();
print("\nOrignal Array")
print(arr)
print("\nCopy")
print(x)
print("changing orignal array")
arr[0] = 22;
print("\nOrignal Array")
print(arr)
print("\nCopy")
print(x)

print("\nCreating View")
y = arr.view();
print("\nOrignal Array")
print(arr)
print("\nView")
print(y)
print("changing orignal array")
arr[0] = 45
print("\nOrignal Array")
print(arr)
print("\nView")
print(y)