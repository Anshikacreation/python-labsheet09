import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password"
)

cursor = con.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS college")

cursor.execute("USE college")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    marks FLOAT
)
""")

print("Database and students table created successfully!")

con.close()