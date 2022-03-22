"""Starting point for Exercise 7.2a Managing Files.

In this exercise, you will learn to create data accessors from several types of files.

To do this, you will:

- Read data from a text file in a CSV format
- Write data to a text file in a CSV format
"""

import sys


def main():
    """Initializes variables."""

    file = r"/home/student/course/part_a/Data/flights.csv"
    search_flight = "1587"


try:
    main()
except IOError as err:
    print("Read or Write error on file", err.args, file=sys.stderr)
