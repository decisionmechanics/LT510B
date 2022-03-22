"""Starting point for Exercise 5.1 Classes and Initialization.

In this exercise, you will gain experience with classes that define data used for an airline.

- Define attributes
- Add a new method
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

    caribbean_list = ["GCM", "CUR"]
    hawaii_list = ["ITO", "HNL"]

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


# Sample data for Trip
the_departure_city = "CUR"
the_arrival_city = "HNL"
departure_date_time = "2022-01-03 09:00"
arrival_date_time = "2022-01-03 16:00"
# my_trip = Trip(
#     departure_city=departure_city,
#     arrival_city=arrival_city,
#     departure_day_time=departure_day_time,
#     arrival_day_time=arrival_day_time
# )

# Part B

# Create list of Trip objects, pass list as positional args to constructor

# all_trips = [
#     Trip(*["HNL", "HKG", "2022-01-03 16:00", "2022-01-03 20:00"]),
#     Trip(*["HNL", "HNL", "2022-01-03 08:30", "2022-01-03 15:40"]),
#     Trip(*["HKG", "CDG", "2022-01-03 19:20", "2022-01-04 12:35"]),
#     Trip(*["HKG", "GCM", "2022-01-03 16:50", "2022-01-04 09:30"]),
#     Trip(*["HNL", "ITO", "2022-01-03 12:00", "2022-01-03 13:55"]),
# ]


# def print_trip(trip):
#     print(
#         "Trip from",
#         trip.departure_city,
#         "to",
#         trip.arrival_city,
#         "Departs at",
#         trip.departure_day_time,
#         "Arrives at",
#         trip.arrival_day_time,
#         end=" ",
#     )


# Part C

# Sample Data for Aircraft
# code is 1
# name is Canadian Regional Jet
#
# Sample Data for Airport
# code is HNL
# city is Honolulu
