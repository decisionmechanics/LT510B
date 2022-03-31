#!/bin/bash

"""This module calculates the nth prime number."""

import findprime


def main() -> None:
    """Calculates and reports the nth prime number."""

    index = int(input("Which (nth) prime do you wish to find? "))

    prime = findprime.find_nth_prime(index)

    print(f"The {index}th prime is {prime}")


if __name__ == "__main__":
    main()
