#!/bin/bash
# pylint: disable=undefined-variable

"""This script is used to explore debugging using pdb."""

import random


def main():
    """Performs the main task of the script."""

    secret = random.randint(1, 100)

    guess = 0
    attempts = 0

    while guess != secret:
        guess = input("What number am I thinking of? ")

        tries += 1

        if guess <= secret:
            print(f"It's bigger than {guess}. Try again.")
        elif guess > secret:
            print(f"It's smaller than {guess}. Try again.")

    print(
        "Congratulations. "
        f"You correctly guessed I was thinking of {secret} in {attempts} attempt(s)."
    )


if __name__ == "__main__":
    main()
