"""Sample code for Chapter 8 placeholder arguments."""

# Passing Arguments to SQL Statements
import sqlite3

connection = sqlite3.connect(r"/home/student/course/part_a/Data/airline.db")
cursor = connection.cursor()

craft_number = (2,)
airport = ("HNL",)

for line in cursor.execute(
    "SELECT * FROM aircraft WHERE aircraftcode = ?", craft_number
):
    print(line)

for line in cursor.execute("SELECT * FROM airports WHERE citycode = ?", airport):
    print(line)

connection.close()
