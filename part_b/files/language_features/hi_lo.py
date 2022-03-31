#!/bin/bash

"""Simple number guessing game."""

import random


def main():
    """Plays one round of the HiLo number guessing game."""

    secret = random.randint(1, 100)

    guess = 0
    attempts = 0

    while guess != secret:
        guess = int(input("What number am I thinking of? "))

        attempts += 1

        if guess < secret:
            print(f"It's bigger than {guess}. Try again.")
        elif guess > secret:
            print(f"It's smaller than {guess}. Try again.")

    print(
        "Congratulations. "
        f"You correctly guessed I was thinking of {secret} in {attempts} attempt(s)."
    )


if __name__ == "__main__":
    main()
