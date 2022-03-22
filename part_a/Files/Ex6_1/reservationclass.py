"""This module provides classes and functions for representing airline reservations.

Provides a Reservation class.

  Typical usage example:

  reservation = Reservation(name="Guido von Rossum", reservation_id="XYZ123",
                            flight_reference=my_flight)
"""


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
