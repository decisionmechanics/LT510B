"""Sample code for Chapter 8 updating records."""

# Updating Data
import sqlite3

connection = sqlite3.connect(r"/home/student/course/part_a/Data/airline.db")
cursor = connection.cursor()

update_plane1 = (7, "Blimp")
update_plane2 = ("Bell430", 6)

cursor.execute("UPDATE aircraft SET aircraftcode = ? WHERE name = ?", update_plane1)

cursor.execute("UPDATE aircraft SET name = ? WHERE aircraftcode = ?", update_plane2)

connection.commit()
connection.close()
