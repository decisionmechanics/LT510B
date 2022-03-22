"""Exercise 8.1 Accessing a MySQL database.

This module describes the exercise airline database.
"""

import sys
import sqlite3
import os.path
import re


def open_connection():
    """Opens a connection to the airline database.

    Returns:
      A connection to a SQLite3 database.
    """

    database_name = r"/home/student/course/part_a/Data/airline.db"
    if not os.path.isfile(database_name):
        raise IOError(database_name, "not found")
    connection = sqlite3.connect(database_name)
    return connection


def describe_tables():
    "Describes the tables in the SQLite3 database."

    cursor = database_connection.cursor()
    for line in cursor.execute("SELECT * from sqlite_master"):
        if line[0] == "table":
            print("Table name is", line[1])
            for column in re.findall(r"\n[a-z]+ ", line[4]):
                print("Column name is", re.sub(r"\n", "", column))
            print("Created with:", re.sub(r"\n", " ", line[4]))
            print("=" * 110)


database_connection = None
try:
    database_connection = open_connection()
    describe_tables()
except IOError as err:
    print("File problems here", err.args, file=sys.stdout)
except sqlite3.OperationalError as err:
    print("Something is wrong here", err.args, file=sys.stderr)
finally:
    if database_connection:
        database_connection.close()
