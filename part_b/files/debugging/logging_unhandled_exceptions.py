#!/bin/bash

"""Logging uncaught exceptions demonstration."""

import logging
import logging.config
import sys

logging.config.fileConfig(fname="logging.ini")
logger = logging.getLogger("appLogger")


def handle_exception(exc_type, exc_value, exc_traceback):
    """Handles exceptions.

    Args:
      exc_type: Type of exception.
      exc_value: Value of exception.
      exc_traceback: Call stack at time of exception.
    """

    # Allow a console program to exit with ^C in the interpreter
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)

        return

    logger.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception


def main():
    """Performs the main task of the script."""

    print(f"Not a number: {1 / 0}")


if __name__ == "__main__":
    main()
