#!/bin/bash

"""This module reports the folders/files in the home directory."""

import subprocess


def main() -> None:
    """Reports the folders/files in the home directory."""

    result = subprocess.run(
        ["ls", "-l", "/home/andrew/"], check=True, capture_output=True
    )

    listing = result.stdout.decode("utf-8").split("\n")[1:]

    for entry in listing:
        if not entry:
            continue

        name = entry[45:]
        month = entry[32:35]
        day = entry[36:38].strip()
        time = entry[39:44]

        print(f"{name} was modified on {month} {day} at {time}.")


if __name__ == "__main__":
    main()
