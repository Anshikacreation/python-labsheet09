students = [
    {"roll": 1, "name": "Anshika", "marks": 90},
    {"roll": 2, "name": "Rahul", "marks": 85},
    {"roll": 3, "name": "Priya", "marks": 95}
]

roll = int(input("Enter roll number: "))

found = False

for student in students:
    if student["roll"] == roll:
        marks = float(input("Enter new marks: "))
        student["marks"] = marks
        print("Marks updated successfully!")
        found = True

if not found:
    print("Student not found.")

print(students)