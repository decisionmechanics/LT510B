#!/bin/bash

"""Runtime configuration files demonstration."""

import logging
import logging.config


def main():
    """Performs the main task of the script."""

    logging.config.fileConfig(fname="logging.ini")
    logger = logging.getLogger("appLogger")

    logger.debug("This is a debug message")


if __name__ == "__main__":
    main()
