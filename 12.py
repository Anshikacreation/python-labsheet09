import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college"
)

cursor = con.cursor()

roll = int(input("Enter roll number: "))
name = input("Enter student name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))

sql = "INSERT INTO students VALUES (%s, %s, %s, %s)"

values = (roll, name, age, marks)

cursor.execute(sql, values)

con.commit()

print("Record inserted successfully!")

con.close()