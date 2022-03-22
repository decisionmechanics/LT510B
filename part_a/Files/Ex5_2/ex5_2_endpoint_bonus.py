"""Solution to 5.2 Inheritance bonus.

In this exercise, you will gain more experience using classes by creating a subclass that inherits
from its base class.

The new subclass will contain additional attributes and methods.

- Create subclasses
- Extend subclasses
"""

# Part A


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


# Part B

# Add the subclass below


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


class Reservation:
    """Describes a flight reservation.

    Args:
      name: Name of passenger.
      reservation_id: Passenger's reservation ID.
      flight_reference: Flight details.
    """

    def __init__(self, name=None, reservation_id=None, flight_reference=None):
        """Initializes a Reservation with attributes defaulted to None."""

        self.name = name
        self.reservation_id = reservation_id
        self.flight_reference = flight_reference


# Part C

# Sample data for Flight
the_flight_number = 221
the_cost = 399.99
craft_code = 2
the_departure_city = "CUR"
the_arrival_city = "HNL"
the_departure_day_time = "2022-01-03 09:00"
the_arrival_day_time = "2022-01-03 16:00"

my_flight = Flight(
    flight_number=the_flight_number,
    cost=the_cost,
    code=craft_code,
    departure_city=the_departure_city,
    arrival_city=the_arrival_city,
    departure_day_time=the_departure_day_time,
    arrival_day_time=the_arrival_day_time,
)

print("my_flight", vars(my_flight))

all_flights = [
    Flight(*[317, 99.95, 4, "HNL", "HKG", "2022-01-03 16:00", "2022-01-03 20:00"]),
    Flight(*[102, 199.99, 42, "HNL", "HNL", "2022-01-03 08:30", "2022-01-03 15:40"]),
    Flight(*[204, 299.99, 44, "HKG", "CDG", "2022-01-03 19:20", "2022-01-04 12:35"]),
    Flight(*[336, 199.99, 44, "HKG", "GCM", "2022-01-03 16:50", "2022-01-04 09:30"]),
    Flight(*[660, 299.99, 3, "HNL", "ITO", "2022-01-03 12:00", "2022-01-03 13:55"]),
]

for flight in all_flights:
    print(vars(flight))
    flight.discount()
    print(flight.cost, "after discount")

# Part D

reservations = [
    {
        "name": "Pat Holder",
        "reservation_id": "101A",
        "flight_reference": all_flights[0],
    },
    {
        "name": "Peter Smith",
        "reservation_id": "102B",
        "flight_reference": all_flights[1],
    },
    {
        "name": "Guy Gildersleeve",
        "reservation_id": "103C",
        "flight_reference": all_flights[2],
    },
    {
        "name": "Janet Rider",
        "reservation_id": "104D",
        "flight_reference": all_flights[1],
    },
    {
        "name": "Lynn Jasper",
        "reservation_id": "105E",
        "flight_reference": all_flights[3],
    },
    {
        "name": "Ian Rouselle",
        "reservation_id": "106F",
        "flight_reference": all_flights[0],
    },
]

for reservation_dictionary in reservations:
    reservation = Reservation(**reservation_dictionary)
    print(
        "Reservation",
        reservation.reservation_id,
        reservation.name,
        reservation.flight_reference.flight_number,
        reservation.flight_reference.cost,
    )
