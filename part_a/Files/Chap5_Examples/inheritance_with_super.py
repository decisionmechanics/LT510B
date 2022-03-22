"""Sample code for Chapter 5 inheritance calling base class constructor."""

# Subclass Instance Initialization Using super()
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

    def print_departure(self):
        """Displays the departure day."""

        print("Trip leaves on", self.departure_day)


class Cruise(Trip):
    """Describes a cruise.

    Attributes:
      ship: The name of the ship.
    """

    def __init__(self, departure_day, arrival_day, ship=None):
        """Initializes a Cruise with a departure and arrival day, and no ship (by default)."""

        self.ship = ship
        super().__init__(departure_day=departure_day, arrival_day=arrival_day)

    def print_schedule(self):
        """Displays the departure and arrival days."""

        print("Cruise", self.departure_day, "to", self.arrival_day)


voyage = Cruise(departure_day="Friday", arrival_day="Monday", ship="Sea Breeze")
voyage.print_departure()
voyage.print_schedule()

# Calling Superclass Methods Using *args and **kwargs
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

    def print_departure(self):
        """Displays the departure day."""

        print("Trip leaves on", self.departure_day)


class Cruise(Trip):
    """Describes a cruise.

    Attributes:
      ship: The name of the ship.
    """

    def __init__(self, ship=None, *args, **kwargs):
        """Initializes a Cruise with no ship (by default)."""

        self.ship = ship
        super().__init__(*args, **kwargs)

    def print_schedule(self):
        """Displays the departure and arrival days."""

        print("Cruise", self.departure_day, "to", self.arrival_day)


voyage = Cruise(departure_day="Friday", arrival_day="Monday", ship="Sea Breeze")
voyage.print_departure()
voyage.print_schedule()
