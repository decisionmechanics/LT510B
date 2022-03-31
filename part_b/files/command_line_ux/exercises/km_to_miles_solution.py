#!/bin/bash
# pylint: disable=no-value-for-parameter

"""Converts between miles and km.

Usage:
  km_to_miles_solution.py 10
  km_to_miles_solution.py --units miles 1
"""

import click

KM_TO_MILES_FACTOR = 0.6213712


@click.version_option(version="1.0.0")
@click.command()
@click.argument("value", type=float)
@click.option(
    "-u",
    "--units",
    type=click.Choice(["km", "miles"]),
    default="km",
    help="Distance units to convert from.",
    show_default=True,
)
def main(value, units):
    "VALUE: Value to convert." ""

    if units == "km":
        print(f"{value} km(s) is {value * KM_TO_MILES_FACTOR:.2f} mile(s)")
    else:
        print(f"{value} miles(s) is {value / KM_TO_MILES_FACTOR:.2f} km(s)")


if __name__ == "__main__":
    main()
