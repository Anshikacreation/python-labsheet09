import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college"
)

cursor = con.cursor()

cursor.execute("""
SELECT * FROM students
ORDER BY marks DESC
LIMIT 1
""")

student = cursor.fetchone()

if student:
    print("Highest Scoring Student:")
    print("Roll Number:", student[0])
    print("Name:", student[1])
    print("Age:", student[2])
    print("Marks:", student[3])
else:
    print("No student records found.")

con.close()