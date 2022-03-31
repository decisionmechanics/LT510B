"""This script reports the total of the primes between 2 and 10 (inclusive)."""

import math


def is_prime(value):
    """Checks for primeness.

    Args:
      value (int): Value to be checked.

    Returns:
      True is value is prime. False otherwise.
    """

    for i in range(2, int(math.sqrt(value) + 1)):
        if value % i == 0:
            return False

    return True


def sum_of_primes(maximum):
    """Calculates the total of the primes up to, and including, a limit.

    Args:
      maximum (int): Maximum value of the primes to be considered.

    Returns:
      Total (int) of the primes.
    """

    total = 0

    for i in range(2, maximum + 1):
        if not is_prime(i):
            continue

        total += i

    return total


def main():
    """Displays the total of the primes."""

    print(sum_of_primes(10))


if __name__ == "__main__":
    main()
