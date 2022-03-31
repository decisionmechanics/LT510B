#!/bin/bash

"""Counts the number of lines in a file.

This script counts the number of lines in the file supplied as it first,
and only, parameter.
"""

import sys


def main():
    """Performs the main task of the script."""

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file path>")
    else:
        file_path = sys.argv[1]

        with open(file_path, encoding="utf8") as input_file:
            lines = input_file.readlines()
            print(f"{file_path} contains {len(lines)} line(s).")


if __name__ == "__main__":
    main()
