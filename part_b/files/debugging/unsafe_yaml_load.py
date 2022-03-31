#!/bin/bash
# pylint: disable=no-value-for-parameter

"""Conducting a security audit with Bandit demonstration."""

import yaml


def to_yaml(data):
    """Serialize data to YAML.

    Args:
      data: Dictionary to be serialized.

    Returns:
      Data formatted as YAML (str).
    """

    return yaml.dump(data)


def from_yaml(text):
    """Deserialize YAML.

    Args:
      text: YAML document (str).

    Returns:
      Dictionary of properties/values from the YAML document.
    """

    return yaml.load(text)


def main():
    """Performs the main task of the script."""

    text = to_yaml({"customer": "ARM", "course": "614N", "title": "Advanced Python"})
    course = from_yaml(text)

    print(course)


if __name__ == "__main__":
    main()
