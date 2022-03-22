"""Sample code for Chapter 8 SQL query."""

# Example SQL Query
import sqlite3

connection = sqlite3.connect(r"/home/student/course/part_a/Data/airline.db")
cursor = connection.cursor()
for line in cursor.execute("SELECT * FROM aircraft"):
    print(line)
connection.close()
