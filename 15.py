import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college"
)

cursor = con.cursor()

roll = int(input("Enter roll number: "))
marks = float(input("Enter new marks: "))

sql = "UPDATE students SET marks=%s WHERE roll=%s"

cursor.execute(sql, (marks, roll))

con.commit()

if cursor.rowcount > 0:
    print("Marks updated successfully!")
else:
    print("Student not found.")

con.close()