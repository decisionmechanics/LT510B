"""Solution for Exercise 7.2a Managing Files.

In this exercise, you will learn to create data accessors from several types of files.

To do this, you will:

- Read data from a text file in a CSV format
- Write data to a text file in a CSV format
"""
import sys


def main():
    """Reads, filters and writes CSV flight data."""

    file = r"/home/student/course/part_a/Data/flights.csv"
    search_flight = "1587"
    output_filename = r"search_flights.csv"
    with open(file, "r") as input_file:
        with open(output_filename, "w") as output_file:
            for line in input_file:
                # print(line) # display each string
                fields = line.split(",")
                # print(fields) # display each list of strings
                if fields[0] == search_flight:
                    print(fields)
                    output_file.write(",".join(fields))


try:
    main()
except IOError as err:
    print("Read or Write error on file", err.args, file=sys.stderr)
