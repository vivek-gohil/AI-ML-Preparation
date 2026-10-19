import numpy as np

employees = np.array([
    [25, 50000, 5],
    [30, 60000, 7],
    [35, 75000, 10],
    [40, 90000, 12]
])

# Age | Salary | Experience

# 1. Get the age of the first employee.
print("\nGet the age of the first employee")
print(f"{employees[0,0]}")

# 2. Get the salary of the third employee.
print("\nGet the salary of the third employee")
print(f"{employees[2,1]}")

# 3. Get the experience of the fourth employee.
print("\nGet the experience of the fourth employee.")
print(f"{employees[3,2]}")

# 4. Get the complete second employee.
print("\nGet the complete second employee.")
print(f"{employees[1]}")

# 5. Get the complete fourth employee.
print("\nGet the complete fourth employee.")
print(f"{employees[3]}")

# 6. Get the age of the fourth employee.
print("\nGet the age of the fourth employee")
print(f"{employees[3,0]}")

# 7. Get the salary of the first employee.
print("\nGet the salary of the first employee")
print(f"{employees[0,1]}")

# 8. Get the last value of the array using negative indexing.
print("\nGet the last value of the array using negative indexing.")
print(f"{employees[-1,-1]}")

# 9. Get the last employee using negative indexing.
print("\nGet the last employee using negative indexing")
print(f"{employees[-1]}")

# 10. Get the third employee's experience.
print("\nGet the third employee's experience")
print(f"{employees[2,2]}")