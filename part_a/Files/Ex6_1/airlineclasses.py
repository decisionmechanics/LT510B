"""This module provides classes and functions for representing airline flights.

Provides a Flight class and a make_sample_trip_flight factory function.

  Typical usage example:

  flight = make_sample_trip_flight()
"""


class Trip:
    """Describes a trip (journey).

    Class attributes:
      caribbean_list: Codes of selected Caribbean airports.
      hawaii_list: Codes of selected Hawaiian airports.

    Attributes:
      departure_city: The city (code) that the trip leaves from.
      arrival_city: The city (code) that the trip arrives at.
      departure_day_time: The time (yyyy-mm-dd hh:mm) that the trip begins/departs.
      arrival_day_time: The time (yyyy-mm-dd hh:mm) that the trip ends/arrives.
    """

    caribbean_list = ["CUR", "GCM"]
    hawaii_list = ["HNL", "ITO"]

    def __init__(
        self,
        departure_city=None,
        arrival_city=None,
        departure_day_time=None,
        arrival_day_time=None,
    ):
        """Initializes a Trip with attributes defaulted to None."""

        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.departure_day_time = departure_day_time
        self.arrival_day_time = arrival_day_time

    def is_round_trip(self):
        """Determines if a trip starts and ends in the same place.

        Returns:
          - True if the departure city is the same as the arrival city.
          - False otherwise.
        """

        return self.arrival_city == self.departure_city

    def is_caribbean(self):
        """Determines if trip starts in the Caribbean.

        Returns:
          - True if the trip starts in the Caribbean.
          - False otherwise.
        """

        return self.arrival_city in Trip.caribbean_list

    def is_hawaiian(self):
        """Determines if trip starts in Hawaii.

        Returns:
          - True if the trip starts in Hawaii.
          - False otherwise.
        """

        return self.arrival_city in Trip.hawaii_list

    def is_interisland(self):
        """Determines if trip starts and ends in Hawaii.

        Returns:
          - True if the trip starts and ends in Hawaii.
          - False otherwise.
        """

        return (
            self.arrival_city in Trip.hawaii_list
            and self.departure_city in Trip.hawaii_list
        )


class Flight(Trip):
    """Describes a flight.

    Args:
      flight_number: Airline's flight number.
      cost: Cost of the flight ($).
      code: Identification code for the aircraft.
    """

    def __init__(self, flight_number, cost, code, *args, **kwargs):
        """Initializes a Flight."""

        self.flight_number = flight_number
        self.cost = cost
        self.code = code
        super().__init__(*args, **kwargs)

    def discount(self):
        """Applies a discount to the flight based on its itinerary."""

        discount = 0.0
        if self.is_interisland():
            discount = 0.05
        elif self.is_hawaiian():
            discount = 0.10
        elif self.is_caribbean():
            discount = 0.15
        self.cost -= self.cost * discount


def make_sample_trip_flight():
    """Create and display a sample Trip and Flight."""

    trip_attributes = (
        "departure_city",
        "arrival_city",
        "departure_day_time",
        "arrival_day_time",
    )
    trip_data = ("HNL", "HNL", "2022-01-03 08:30", "2022-01-03 15:40")
    flight_attributes = ("flightnum", "cost", "code")
    flight_data = (221, 399.99, 2)
    data = dict(zip(trip_attributes, trip_data))
    sample_trip = Trip(**data)
    print("Trip:", vars(sample_trip))  # vars() returns dictionary of attributes
    data = dict(zip(trip_attributes + flight_attributes, trip_data + flight_data))
    sample_flight = Flight(**data)
    print("Flight:", vars(sample_flight))


if __name__ == "__main__":
    print("Running as main")
    make_sample_trip_flight()
else:
    print("airlineclasses.py imported, no Trip or Flight created")
