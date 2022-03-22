"""Starting point for Exercise 7.2b Managing Files.

In this exercise, you will learn to create data accessors from several types of files.

To do this, you will:

- Create class objects from text data files
"""

import csv
import sys
import airlineclasses


def main():
    """Initializes variables."""

    file = r"/home/student/course/part_a/Data/flights.csv"


try:
    main()
except IOError as e:
    print("Read or Write error on file", e.args, file=sys.stderr)
