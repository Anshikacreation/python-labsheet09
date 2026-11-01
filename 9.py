# Save student data
file = open("students.txt", "w")

n = int(input("Enter number of students: "))

for i in range(n):
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    file.write(roll + "," + name + "," + marks + "\n")

file.close()

print("Student data saved successfully!")

# Read student data
file = open("students.txt", "r")

print("\nStudent Records:")

for line in file:
    print(line, end="")

file.close()