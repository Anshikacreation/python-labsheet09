students = [
    {"roll": 1, "name": "Anshika", "marks": 90},
    {"roll": 2, "name": "Rahul", "marks": 85},
    {"roll": 3, "name": "Priya", "marks": 95}
]

roll = int(input("Enter roll number to delete: "))

found = False

for student in students:
    if student["roll"] == roll:
        students.remove(student)
        print("Student deleted successfully!")
        found = True
        break

if not found:
    print("Student not found.")

print(students)