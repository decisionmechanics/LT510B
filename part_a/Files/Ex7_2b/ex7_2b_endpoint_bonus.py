"""Solution to Exercise 7.2b Managing Files bonus.

In this exercise, you will learn to create data accessors from several types of files.

To do this, you will:

- Create class objects from text data files
"""

import csv
import sys
import airlineclasses


def main():
    """Reads CSV flight data and creates/displays Flight objects."""

    file = r"/home/student/course/part_a/Data/flights.csv"

    with open(file, "r") as inf:
        file_reader = csv.DictReader(inf)
        all_flights = [
            airlineclasses.Flight(**data_dictionary) for data_dictionary in file_reader
        ]

    print(len(all_flights), "flights created")
    print("Last flight", vars(all_flights[-1]))


try:
    main()
except IOError as e:
    print("Read or Write error on file", e.args, file=sys.stderr)
