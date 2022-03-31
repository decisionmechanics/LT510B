#!/bin/bash

"""Tracing demonstration."""


def do_a():
    """Does A."""

    print("Doing A")

    do_b()


def do_b():
    """Does B."""

    print("Doing B")

    do_c()


def do_c():
    """Does C."""

    print("Doing C")


def do_d(operation_id):
    """Does D.

    Args:
      operation_id: Operation ID.
    """
    print(f"Doing D{operation_id}")


def naive_factorial(value):
    """Calculates factorials.

    The factorial of 0 or negative numbers is assumed to be 1.

    Args:
      value (int): The value for which the factorial is required.

    Returns:
      Factorial of the value.
    """

    if value < 1:
        return 1

    return value * naive_factorial(value - 1)


def main():
    """Performs the main task of the script."""

    do_a()

    for i in range(0, 5):
        do_d(i + 1)

    print(naive_factorial(6))


if __name__ == "__main__":
    main()
