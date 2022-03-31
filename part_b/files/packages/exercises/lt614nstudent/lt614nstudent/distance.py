"""This package provides functions to convert distances from metric to imperial
units.

Attributes:
  km_to_miles (function): Converts km to miles.
  m_to_feet (function): Converts m to feet.
  mm_to_inches (function): Converts mm to inches.
"""


def km_to_miles(value: float) -> float:
    """Converts km to miles.

    Args:
      value: kms to convert.

    Returns:
      Distance in miles.
    """

    return value * 0.6213712


def m_to_feet(value: float) -> float:
    """Converts m to feet.

    Args:
      value: m to convert.

    Returns:
      Distance in feet.
    """

    return value / 0.3048


def mm_to_inches(value: float) -> float:
    """Converts mm to inches.

    Args:
      value: mm to convert.

    Returns:
      Distance in inches.
    """

    return value / 25.4
