"""Sample code for Chapter 5 simple inheritance."""

# Class Inheritance
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
    """Describes a cruise."""

    def print_schedule(self):
        """Displays the departure and arrival days."""

        print("Cruise", self.departure_day, "to", self.arrival_day)


class Flight(Trip):
    """Describes a flight."""

    def print_arrival(self):
        """Displays the arrival day."""

        print("Flight arrives on", self.arrival_day)


voyage = Cruise(departure_day="Friday", arrival_day="Monday")
voyage.print_departure()
voyage.print_schedule()

flight_home = Flight(departure_day="Monday", arrival_day="Monday")
flight_home.print_departure()
flight_home.print_arrival()
