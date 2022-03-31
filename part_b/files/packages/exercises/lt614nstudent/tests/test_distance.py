"""This module tests the distance module."""

from conversion import distance


def test_km_to_miles_returns_0pt6213712_miles_for_1km() -> None:
    "Tests that 1 km is converted to approximately 0.62 miles."

    # Arrange

    # Act
    miles = distance.km_to_miles(1)

    # Assert
    assert miles == 0.6213712
