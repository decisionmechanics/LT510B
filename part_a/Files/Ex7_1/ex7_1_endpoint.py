"""Solution to Exercise 7.1 Exceptions.

In this exercise, you will handle various types of exceptions.
"""

import sys


def print_fahrenheit_to_celsius(fahrenheit_temperatures):
    """Displays Fahrenheit temperatures in Celsius.

    Args:
      Sequence of (numeric) Fahrenheit temperatures.
    """

    for fahrenheit_temperature in fahrenheit_temperatures:
        celsius_temperature = (float(fahrenheit_temperature) - 32) * 5.0 / 9.0
        print(
            f"Fahrenheit temperature {fahrenheit_temperature} is Celsius {celsius_temperature:.2f}"
        )


temperatures1 = ["123.0", "34.0", "5", "85"]
temperatures2 = ["123.0", "34.0", "five", "85"]
temperatures3 = []

try:
    print_fahrenheit_to_celsius(temperatures1)
    print_fahrenheit_to_celsius(temperatures2)
except ValueError:
    print("ValueError encountered", file=sys.stderr)
