"""This script populates the airline SQLite3 database."""

import sqlite3
import csv
import os

os.chdir(r"/home/student/course/part_a/Data")
connection = sqlite3.connect("airline.db")
cursor = connection.cursor()

airports_csv = r"/home/student/course/part_a/Data/airports.csv"
with open(airports_csv, "r") as infile:
    line_reader = csv.reader(infile)
    for one_line in line_reader:
        cursor.execute("""insert into airports values(?,?)""", one_line)
connection.commit()

aircraft_csv = r"/home/student/course/part_a/Data/aircraft.csv"
with open(aircraft_csv, "r") as infile:
    line_reader = csv.reader(infile)
    for one_line in line_reader:
        cursor.execute("""insert into aircraft values(?,?)""", one_line)
connection.commit()

flights_csv = r"/home/student/course/part_a/Data/flights.csv"
with open(flights_csv, "r") as infile:
    line_reader = csv.reader(infile)
    for one_line in line_reader:
        cursor.execute("""insert into flights values(?,?,?,?,?,?,?,?,?,?)""", one_line)
connection.commit()

reservations_csv = r"/home/student/course/part_a/Data/reservations.csv"
with open(reservations_csv, "r") as infile:
    line_reader = csv.reader(infile)
    for one_line in line_reader:
        cursor.execute("""insert into reservations values(?,?,?)""", one_line)
connection.commit()
connection.close()
