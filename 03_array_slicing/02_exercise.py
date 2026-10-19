import numpy as np

employees = np.array([
    [25, 50000, 5],
    [30, 60000, 7],
    [35, 75000, 10],
    [40, 90000, 12]
])

print("\n1. Get the first two employees.")
print(employees[:2])

print("\n2. Get the last two employees.")
print(employees[2:])

print("\n3. Get all employee ages.")
print(employees[:,0])

print("\n6. Get the first 3 employees' Age and Salary only.")
print(employees[:3,:2])

print("\n7. Get the last 2 employees' Age and Experience only.")
print(employees[2:,[0,2]])

print("\n8. Get every second employee")
print(employees[::2])

print("\n9. Every employee but only Salary and Experience")
print(employees[:,[1,2]])