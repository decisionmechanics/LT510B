#!/bin/bash

"""Rolling log files demonstration."""

import logging
from logging import handlers
import sys
import time


def main():
    """Performs the main task of the script."""

    logger = logging.getLogger("timed_app")
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)

    file_handler = handlers.TimedRotatingFileHandler(
        "timed_app.log", when="M", interval=1
    )
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    count = 0

    while True:
        time.sleep(1)
        count += 1
        logger.debug("This is a debug message (%d)", count)


if __name__ == "__main__":
    main()
