"""Solution to Exercise 5.1 Classes and Initialization bonus.

In this exercise, you will gain experience with classes that define data used for an airline.

- Define attributes
- Add a new method
"""

# Part A


class Aircraft:
    """Describes a plane.

    Attributes:
      code: Aircraft code
      name: Aircraft name
    """

    def __init__(self, code=None, name=None):
        """Initializes an Aircraft with attributes defaulted to None."""

        self.code = code
        self.name = name


class Airport:
    """Describes a airport.

    Attributes:
      city_code: Airport code
      name: City name
    """

    def __init__(self, city_code=None, city=None):
        """Initializes an Airport with attributes defaulted to None."""

        self.city_code = city_code
        self.city = city


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


# Sample data for Trip
the_departure_city = "CUR"
the_arrival_city = "HNL"
departure_date_time = "2022-01-03 09:00"
arrival_date_time = "2022-01-03 16:00"
my_trip = Trip(
    departure_city=the_departure_city,
    arrival_city=the_arrival_city,
    departure_day_time=departure_date_time,
    arrival_day_time=arrival_date_time,
)

print(
    "my_trip",
    my_trip.departure_city,
    my_trip.arrival_city,
    my_trip.departure_day_time,
    my_trip.arrival_day_time,
)

print("The caribbean_list is", Trip.caribbean_list)
print("The hawaii_list is ", Trip.hawaii_list)

# test with a round trip
answer = "is" if my_trip.is_round_trip() else "is not"
print(my_trip.departure_city, "to", my_trip.arrival_city, answer, "a round trip")

# create second that is not a round trip
my_trip = Trip(
    departure_city=the_departure_city,
    arrival_city=the_departure_city,
    departure_day_time=departure_date_time,
    arrival_day_time=arrival_date_time,
)

# test if not a round trip
answer = "is" if my_trip.is_round_trip() else "is not"
print(my_trip.departure_city, "to", my_trip.arrival_city, answer, "a round trip")

# Part B

# Create list of Trip objects, pass list as positional args to constructor

all_trips = [
    Trip(*["HNL", "HKG", "2022-01-03 16:00", "2022-01-03 20:00"]),
    Trip(*["HNL", "HNL", "2022-01-03 08:30", "2022-01-03 15:40"]),
    Trip(*["HKG", "CDG", "2022-01-03 19:20", "2022-01-04 12:35"]),
    Trip(*["HKG", "GCM", "2022-01-03 16:50", "2022-01-04 09:30"]),
    Trip(*["HNL", "ITO", "2022-01-03 12:00", "2022-01-03 13:55"]),
]


def print_trip(trip):
    """Displays the details of a trip.

    Args:
      trip: A Trip object.
    """

    print(
        "Trip from",
        trip.departure_city,
        "to",
        trip.arrival_city,
        "Departs at",
        trip.departure_day_time,
        "Arrives at",
        trip.arrival_day_time,
    )


for a_trip in all_trips:
    print_trip(a_trip)
    if a_trip.is_round_trip():
        print("\tis RoundTrip")
    if a_trip.is_caribbean():
        print("\tis Caribbean")
    if a_trip.is_hawaiian():
        print("\tis Hawaiian")
    if a_trip.is_interisland():
        print("\tis Interisland")

# Part C

# Sample Data for Aircraft
# code is 1
# name is Canadian Regional Jet
#
# Sample Data for Airport
# code is HNL
# city is Honolulu

sample_aircraft = Aircraft(code=1, name="Canadian Regional Jet")
sample_airport = Airport(city_code="HNL", city="Honolulu")
print("sample_aircraft", sample_aircraft.code, sample_aircraft.name)
print("sample_airport", sample_airport.city_code, sample_airport.city)
