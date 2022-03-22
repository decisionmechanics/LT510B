"""This module imports aircraft data from a CSV file and displays it."""

import csv


class Aircraft:
    """Describes a plane.

    Attributes:
      aircraft_code: (Numeric) Code for plane.
      name: Plane model.
    """

    def __init__(self, aircraft_code=None, name=None):
        """Initializes an Aircraft with attributes defaulted to None."""

        self.aircraftcode = aircraft_code
        self.name = name


AIRCRAFT_CSV = r"/home/student/course/part_a/Data/aircraft.csv"

with open(AIRCRAFT_CSV) as input_file:
    file_reader = csv.DictReader(input_file)
    for data_line in file_reader:  # iterate through the file
        plane = Aircraft(**data_line)
        print("One line as an Aircraft object", vars(plane))
