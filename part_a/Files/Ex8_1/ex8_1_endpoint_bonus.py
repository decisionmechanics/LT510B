"""Solution to Exercise 8.1 Accessing a MySQL database bonus.

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
    """Displays all the records in the database matching a flight number.

    Args:
      connection: SQLite3 database connection.
    """

    cursor = connection.cursor()
    search_flight = input("Enter the flight number to retrieve -> ")
    cursor.execute("SELECT * from flights where flightnum = ?", (search_flight,))
    row = cursor.fetchone()
    if row is not None:
        print(row)
        for row in cursor:
            print(row)
    else:
        print("Nothing found for flight", search_flight)


def insert_row(connection):
    """Inserts the new_flight object into the database.

    Args:
      connection: SQLite3 database connection.
    """

    cursor = connection.cursor()
    sql = "INSERT INTO flights VALUES(?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(sql, new_flight)
    connection.commit()


def delete_row(connection):
    """Deletes the new_flight object from the database.

    Args:
      connection: SQLite3 database connection.
    """

    cursor = connection.cursor()
    sql = "DELETE FROM flights WHERE flightnum = ?"
    cursor.execute(sql, (new_flight[0],))
    connection.commit()


database_connection = None
try:
    database_connection = open_connection()
    insert_row(database_connection)
    search_database(database_connection)
    delete_row(database_connection)

except IOError as e:
    print("File problems here", e.args, file=sys.stdout)
except sqlite3.OperationalError as e:
    print("Something is wrong here", e.args, file=sys.stderr)
finally:
    if database_connection:
        database_connection.close()
