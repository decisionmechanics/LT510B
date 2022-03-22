"""Sample code for Chapter 8 deleting records."""

# Deleting Data
import sqlite3

connection = sqlite3.connect(r"/home/student/course/part_a/Data/airline.db")
cursor = connection.cursor()

plane_code = (6,)
plane_type = ("Blimp",)

cursor.execute("DELETE FROM aircraft WHERE aircraftcode = ?", plane_code)

cursor.execute("DELETE FROM aircraft WHERE name = ?", plane_type)

connection.commit()
connection.close()
