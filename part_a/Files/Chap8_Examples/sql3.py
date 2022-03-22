"""Sample code for Chapter 8 inserting records."""

# Inserting a Row
import sqlite3

connection = sqlite3.connect(r"/home/student/course/part_a/Data/airline.db")
cursor = connection.cursor()

new_plane1 = (5, "Blimp")
new_plane2 = (6, "Helicopter")

cursor.execute("INSERT INTO aircraft VALUES (?, ?)", new_plane1)
cursor.execute("INSERT INTO aircraft VALUES (?, ?)", new_plane2)

connection.commit()
connection.close()
