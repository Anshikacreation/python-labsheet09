employees = {}

# Create
employees[101] = {"name": "Amit", "salary": 25000}
employees[102] = {"name": "Riya", "salary": 30000}

print("Employee Records:", employees)

# Read
print("\nEmployee Details:")
for emp_id, details in employees.items():
    print(emp_id, details)

# Update
employees[101]["salary"] = 35000
print("\nAfter Update:", employees)

# Delete
del employees[102]
print("\nAfter Delete:", employees)