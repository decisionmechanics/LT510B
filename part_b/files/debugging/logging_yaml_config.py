#!/bin/bash

"""Runtime configuration files demonstration."""

import logging
import logging.config
import yaml


def main():
    """Performs the main task of the script."""

    with open("logging.yml", encoding="utf8") as yaml_file:
        config = yaml.safe_load(yaml_file.read())
        logging.config.dictConfig(config)

    logger = logging.getLogger("appLogger")

    logger.debug("This is a debug message")


if __name__ == "__main__":
    main()
