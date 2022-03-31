"""This package provides functions to convert weights from metric to imperial
units.

Attributes:
  kg_to_lbs (function): Converts kg to lbs.
  g_to_oz (function): Converts g to oz.
"""


def kg_to_lbs(value: float) -> float:
    """Converts kg to lbs.

    Args:
      value: kg to convert.

    Returns:
      Weight in lbs.
    """

    return value / 0.4536


def g_to_oz(value: float) -> float:
    """Converts g to oz.

    Args:
      value: g to convert.

    Returns:
      Weight in oz.
    """

    return value * 0.035274
