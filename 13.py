import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college"
)

cursor = con.cursor()

cursor.execute("SELECT * FROM students")

records = cursor.fetchall()

print("All Student Records:")

for row in records:
    print(row)

con.close()