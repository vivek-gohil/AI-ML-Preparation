import numpy as np

batch1 = np.array([[2, 70], [4, 80]])
batch2 = np.array([[5, 85], [6, 90]])

# Tasks:
# 1. Combine both batches using np.concatenate().
# 2. Choose the appropriate axis.
combine_batches = np.concatenate((batch1, batch2))


# 3. Print the combined array and its shape.
print(combine_batches)
print(combine_batches.shape)

# 4. Explain why you chose that axis.
# Selecting axis = 0 (default axis) as its more meaningfull for given array
# batch number 2 - has 70 students
# batch number 4 - has 80 students

print("-"*80)
#Exercise 2 — Add another feature
student_data = np.array([[2, 70], [4, 80], [5, 85]])
previous_scores = np.array([60, 75, 80])

# Tasks:
# 1. Use np.concatenate() to add the scores as a third column.
scores = previous_scores.reshape(3,1);
final_student_details = np.concatenate((student_data,scores), axis=1)

# 2. Print the final array and shape.
print(final_student_details)
print(final_student_details.shape)

# 3. Explain how each score remains associated with the correct student.

print("-"*80)
#Exercise 3 — Stack image samples
image1 = np.array([10, 20, 30, 40])
image2 = np.array([50, 60, 70, 80])
image3 = np.array([90, 100, 110, 120])

# Tasks:
# 1. Combine all three arrays using np.stack() with axis=0.
result = np.stack((image1,image2,image3))

# 2. Print the result and its shape.
print(result)
print(result.shape)

# 3. Repeat using axis=1.
result = np.stack((image1,image2,image3), axis=1)
print(result)
print(result.shape)


# 4. Explain the difference between the two output shapes.
# With axis = 0 = rows = Travel vertical
# With axis = 1 = columns = Travel horizontal
