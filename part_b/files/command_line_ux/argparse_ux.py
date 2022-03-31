#!/bin/bash

"""Echoes the script filename and any supplied arguments."""

import argparse


def parse_arguments():
    """Extracts the command line arguments.

    Returns:
      The parsed command line arguments.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="Path to file.")
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        choices=["CSV", "TSV", "JSON"],
        default="CSV",
        help=r"File format.",
    )

    return parser.parse_args()


def main():
    """Performs the main task of the script."""

    args = parse_arguments()

    print(args)


if __name__ == "__main__":
    main()
