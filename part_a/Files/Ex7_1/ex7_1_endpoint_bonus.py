"""Solution to Exercise 7.1 Exceptions bonus.

In this exercise, you will handle various types of exceptions.
"""

import sys


def print_fahrenheit_to_celsius(fahrenheit_temperatures):
    """Displays Fahrenheit temperatures in Celsius.

    Args:
      Sequence of (numeric) Fahrenheit temperatures.
    """

    if fahrenheit_temperatures:
        for fahrenheit_temperature in fahrenheit_temperatures:
            try:
                fahrenheit_temperature = float(fahrenheit_temperature)
            except ValueError as err:
                print(
                    "ValueError handled",
                    err.args,
                    "with temperature =",
                    fahrenheit_temperature,
                )
                print("Proceeding using 0.0 as temperature")
                fahrenheit_temperature = 0.0
            celsius_temperature = (fahrenheit_temperature - 32) * 5.0 / 9.0
            print(
                f"""Fahrenheit temperature {fahrenheit_temperature} is Celsius {
                    celsius_temperature:.2f}"""
            )
    else:
        raise IndexError("Zero length list")


temperature1 = ["123.0", "34.0", "5", "85"]
temperature2 = ["123.0", "34.0", "five", "85"]
temperature3 = []

try:
    print_fahrenheit_to_celsius(temperature1)
    print_fahrenheit_to_celsius(temperature2)
    print_fahrenheit_to_celsius(temperature3)
except ValueError as the_err:
    print("ValueError encountered in main program", the_err.args, file=sys.stderr)
except IndexError as the_err:
    print("IndexError encountered", the_err.args, file=sys.stderr)
