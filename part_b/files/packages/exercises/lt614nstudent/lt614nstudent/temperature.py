"""This package provides functions to convert between temperatures.

Attributes:
  celsius_to_fahrenheit (function): Converts degC to degF.
  celsius_to_kelvin (function): Converts degC to degK.
"""


def celsius_to_fahrenheit(value: float) -> float:
    """Converts degC to degF.

    Args:
      value: degC to convert.

    Returns:
      Temperature in degF.
    """

    return value * 9.0 / 5.0 + 32.0


def celsius_to_kelvin(value: float) -> float:
    """Converts degC to degK.

    Args:
      value: degC to convert.

    Returns:
      Temperature in degK.
    """

    return value - 273.15
