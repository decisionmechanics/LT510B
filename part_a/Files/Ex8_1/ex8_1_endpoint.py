"""Solution to Exercise 8.1 Accessing a MySQL database.

In this exercise you will write new data accessor functions to process data stored in a database.

To do this, you will

- Create data accessor functions for a database
- Execute SQL statements within the Python code
"""

import sys
import sqlite3
import os.path

new_flight = [99999, "HNL", "CDG", "2022-02-04 04:00", "2022-02-04", 599.95, 4]


def open_connection():
    """Opens a connection to the airline database.

    Returns:
      A connection to a SQLite3 database.
    """
    database_name = r"/home/student/course/part_a/Data/airline.db"
    if not os.path.isfile(database_name):
        raise IOError(database_name, "not found")
    return sqlite3.connect(database_name)


def search_database(connection):
    """Displays all the records in the database.

    Args:
      connection: SQLite3 database connection.
    """

    cursor = connection.cursor()
    for row in cursor.execute("SELECT * FROM flights"):
        print(row)


database_connection = None
try:
    database_connection = open_connection()
    search_database(database_connection)
except IOError as e:
    print("File problems here", e.args, file=sys.stdout)
except sqlite3.OperationalError as e:
    print("Something is wrong here", e.args, file=sys.stderr)
finally:
    if database_connection:
        database_connection.close()
