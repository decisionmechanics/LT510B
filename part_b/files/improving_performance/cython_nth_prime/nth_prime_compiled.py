#!/bin/bash

"""This module calculates the nth prime number and profiles that calculation.

Args:
  Index of prime number to find.
"""

import sys
import time
import primes


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


def main() -> None:
    """Times the calculation of the nth prime nunber and reports the duration
    and result."""

    index = int(sys.argv[1])

    start_time = time.perf_counter()

    prime = primes.find_nth_prime(index)

    duration = time.perf_counter() - start_time

    suffixed_index = get_number_suffix(index)

    print(
        f"Calculated {index}{suffixed_index} prime to be {prime} in {duration:.2f} second(s)"
    )


if __name__ == "__main__":
    main()
