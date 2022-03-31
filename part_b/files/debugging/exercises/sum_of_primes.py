"""This script reports the total of the primes between 2 and 10 (inclusive)."""

import math


def sum_of_primes(maximum):
    """Checks for primeness.

    Args:
      value (int): Value to be checked.

    Returns:
      True is value is prime. False otherwise.
    """

    total = 0

    for i in range(2, maximum + 1):
        should_continue = False

        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                should_continue = True
                break

        if should_continue:
            continue

        total += i

    return total


def main():
    """Displays the total of the primes."""

    print(sum_of_primes(10))


if __name__ == "__main__":
    main()
