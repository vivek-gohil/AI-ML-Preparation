import numpy as np
# Get the first element from the following array:
arr = np.array([1, 2, 3, 4])
print(arr[0])

# Get the second element from the following array:
print(arr[1])

#Get third and fourth elements from the following array and add them.
print(arr[2] + arr[3])

# Access 2-D Arrays
arr = np.array([
        [1,2,3,4,5], [6,7,8,9,10]
    ])
# Access the element on the first row, second column:
print(arr[0][1])

# Access the element on the 2nd row, 5th column:
print(arr[1][4])

# Access 3-D Arrays
arr = np.array([
    [
        [1, 2, 3], [4, 5, 6]
    ], 
    [
        [7, 8, 9], [10, 11, 12]
    ]
])

# Access the third element of the second array of the first array:
print(arr[0][1][2])

# Negative Indexing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr)

# Print the last element from the 2nd dim:
print(arr[1][-1])
print(arr[1,-1])
