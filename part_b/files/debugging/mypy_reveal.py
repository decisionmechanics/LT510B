#!/bin/bash
# pylint: disable=undefined-variable

"""Revealing Mypy types demonstration."""


def to_fahrenheit(deg_c: float) -> float:
    """Converts Celsius to Fahrenheit.

    Args:
      deg_c: Celcius temperature.

    Returns:
      Fahrenheit temperature.
    """

    return deg_c * 9.0 / 5.0 + 32.0


def main() -> None:
    """Performs the main task of the script."""

    deg_c = input("What temperature do you wish to convert? ")
    deg_f = to_fahrenheit(deg_c)

    print(f"{deg_c} degC is {deg_f} degF.")


if __name__ == "__main__":
    main()

# These are specific to Mypy and will fail in the interpreter
reveal_type(to_fahrenheit)
reveal_locals()
