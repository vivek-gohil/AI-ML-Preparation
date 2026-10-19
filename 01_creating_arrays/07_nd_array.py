import numpy as np
a = np.array(40)
b = np.array([1,2,3,4,5])
c = np.array([
        [1,2,3],
        [4,5,6]
    ])
d = np.array([
        [
            [1,2,3],[4,5,6]
        ],
        [
            [1,2,3],[4,5,6]
        ]
    ])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#Higher Dimensional Arrays
# An array can have any number of dimensions.
# When the array is created, you can define the number of dimensions by using the ndmin argument.
e = np.array([1,2,3,4],ndmin=5);
print(e)
print(f"Number of dimensions : { e.ndim}")