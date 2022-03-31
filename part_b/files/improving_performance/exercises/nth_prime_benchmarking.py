#!/bin/bash

"""This module calculates the nth prime number.

Args:
  Index of prime number to find.
"""

import math
import sys


def is_prime(value: int) -> bool:
    """Checks for primeness.

    Args:
      value: Number to check.

    Returns:
      True if value is prime. False otherwise.
    """

    for i in range(2, int(math.sqrt(value) + 1)):
        if value % i == 0:
            return False

    return True


def get_number_suffix(value: int) -> str:
    """Gets the correct order suffix for a number.

    e.g. st, nd, rd, th.

    Args:
      value: The number on which the suffix should be based.

    Returns:
      The correct suffix for the value.
    """

    if 11 <= value <= 13:
        return "th"
    if value % 10 == 1:
        return "st"
    if value % 10 == 2:
        return "nd"
    if value % 10 == 3:
        return "rd"
    return "th"


def find_nth_prime(index: int) -> int:
    """Calculates the nth prime number.

    Args:
      index: Index of prime number to find.

    Returns
      The nth (index) prime number.
    """

    candidate = 1

    while index > 0:
        candidate += 1

        if is_prime(candidate):
            index -= 1

    return candidate


def main() -> None:
    """Calculates and reports the nth prime number."""

    index = int(sys.argv[1])

    prime = find_nth_prime(index)

    print(f"Calculated {index}{get_number_suffix(index)} prime to be {prime}")


if __name__ == "__main__":
    main()
