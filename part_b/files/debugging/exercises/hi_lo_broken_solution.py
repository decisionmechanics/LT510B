#!/bin/bash
# pylint: disable=global-statement

"""Simple number guessing game."""

import logging
import logging.config
import random
import sys


LOGGER = None


def handle_exception(exc_type, exc_value, exc_traceback):
    """Handles exceptions.

    Args:
      exc_type: Type of exception.
      exc_value: Value of exception.
      exc_traceback: Call stack at time of exception.
    """

    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)

        return

    LOGGER.critical("uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


def configure_logging():
    """Configures the global logger."""

    global LOGGER

    logging.config.fileConfig(fname="hi_lo_logging.ini")
    LOGGER = logging.getLogger("appLogger")

    sys.excepthook = handle_exception


def main():
    """Performs the main task of the script."""

    configure_logging()

    secret = random.randint(1, 100)
    # Don't log secrets such as passwords and API keys
    LOGGER.debug("secret is %d", secret)

    guess = 0
    attempts = 0

    while guess != secret:
        guess = int(input("What number am I thinking of? "))
        LOGGER.debug("user guessed {%d}", guess)

        attempts += 1

        LOGGER.debug("{%d} attempt(s)", attempts)

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
