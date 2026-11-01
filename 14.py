import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college"
)

cursor = con.cursor()

roll = int(input("Enter roll number to search: "))

cursor.execute(
    "SELECT * FROM students WHERE roll=%s",
    (roll,)
)

record = cursor.fetchone()

if record:
    print("Student Found:", record)
else:
    print("Student not found.")

con.close()