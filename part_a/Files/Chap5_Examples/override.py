"""Sample code for Chapter 5 overriding methods."""

# Overriding Methods
class Trip:
    """Describes a trip (journey).

    Attributes:
      departure_day: The day of the week (e.g. Sunday) the trip begins/departs.
      arrival_day: The day of the week (e.g. Sunday) the trip ends/arrives.
    """

    def __init__(self, departure_day=None, arrival_day=None):
        """Initializes a Trip with no departure or arrival day (by default)."""

        self.departure_day = departure_day
        self.arrival_day = arrival_day

    def print_trip(self):
        """Displays the departure day."""

        print("Schedule is", self.departure_day, self.arrival_day)


class Cruise(Trip):
    """Describes a cruise.

    Attributes:
      ship: The name of the ship.
    """

    def __init__(self, ship=None, *args, **kwargs):
        """Initializes a Cruise with no ship (by default)."""

        self.ship = ship
        super().__init__(*args, **kwargs)

    def print_trip(self):
        """Displays the name of the ship."""

        print("Ship is", self.ship)


day1 = Cruise(departure_day="Friday", arrival_day="Saturday", ship="Moonbeam")
day1.print_trip()

# Overriding Methods - Continued
class Trip:
    """Describes a trip (journey).

    Attributes:
      departure_day: The day of the week (e.g. Sunday) the trip begins/departs.
      arrival_day: The day of the week (e.g. Sunday) the trip ends/arrives.
    """

    def __init__(self, departure_day=None, arrival_day=None):
        """Initializes a Trip with no departure or arrival day (by default)."""

        self.departure_day = departure_day
        self.arrival_day = arrival_day

    def print_trip(self):
        """Displays the departure and arrival days."""

        print("Schedule is", self.departure_day, self.arrival_day, end=" ")


class Cruise(Trip):
    """Describes a cruise."""

    def __init__(self, ship=None, *args, **kwargs):
        """Initializes a Cruise with no ship (by default)."""

        self.ship = ship
        super().__init__(*args, **kwargs)

    def print_trip(self):
        """Displays the departure and arrival days, and the name of the ship."""

        super().print_trip()
        print("Ship is", self.ship)


travels = [
    Cruise(departure_day="Friday", arrival_day="Saturday", ship="Moonbeam"),
    Cruise(departure_day="Wednesday", arrival_day="Friday", ship="Golden Sun"),
]

for travel in travels:
    travel.print_trip()
