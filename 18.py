import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college"
)

cursor = con.cursor()

cursor.execute("SELECT * FROM students ORDER BY name ASC")

records = cursor.fetchall()

print("Students in Alphabetical Order:")

for row in records:
    print(row)

con.close()