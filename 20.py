import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college"
)

cursor = con.cursor()

def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    marks = float(input("Enter Marks: "))

    sql = "INSERT INTO students VALUES (%s, %s, %s, %s)"

    cursor.execute(sql, (roll, name, age, marks))
    con.commit()

    print("Student added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")

    records = cursor.fetchall()

    print("\n--- Student Records ---")

    for row in records:
        print(row)

    if not records:
        print("No records found.")

def update_student():
    roll = int(input("Enter Roll Number: "))
    marks = float(input("Enter New Marks: "))

    sql = "UPDATE students SET marks=%s WHERE roll=%s"

    cursor.execute(sql, (marks, roll))
    con.commit()

    if cursor.rowcount > 0:
        print("Student updated successfully!")
    else:
        print("Student not found.")

def delete_student():
    roll = int(input("Enter Roll Number: "))

    cursor.execute(
        "DELETE FROM students WHERE roll=%s",
        (roll,)
    )

    con.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student not found.")

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")

cursor.close()
con.close()