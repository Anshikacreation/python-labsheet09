import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college"
)

cursor = con.cursor()

roll = int(input("Enter roll number to delete: "))

cursor.execute(
    "DELETE FROM students WHERE roll=%s",
    (roll,)
)

con.commit()

if cursor.rowcount > 0:
    print("Student deleted successfully!")
else:
    print("Student not found.")

con.close()