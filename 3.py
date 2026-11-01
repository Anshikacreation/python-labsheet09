students = [
    {"roll": 1, "name": "Anshika", "marks": 90},
    {"roll": 2, "name": "Rahul", "marks": 85},
    {"roll": 3, "name": "Priya", "marks": 95}
]

name = input("Enter student name to search: ")

found = False

for student in students:
    if student["name"].lower() == name.lower():
        print("Student Found:", student)
        found = True

if not found:
    print("Student not found.")