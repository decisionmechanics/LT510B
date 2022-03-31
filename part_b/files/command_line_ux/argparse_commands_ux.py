#!/bin/bash

"""Describes the UI for a hypothetical data exporting app."""

import argparse


def export_text(args):
    """Exports data as text."""

    print("Exporting as text")
    print(args)


def export_json(args):
    """Exports data as JSON."""

    print("Exporting as JSON")
    print(args)


def parse_arguments():
    """Extracts the command line arguments.

    Returns:
      The parsed command line arguments.
    """

    parser = argparse.ArgumentParser()
    parser.set_defaults(func=lambda args: parser.print_help())
    subparsers = parser.add_subparsers()

    text_parser = subparsers.add_parser(
        name="text",
        help="Export as text file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    text_parser.set_defaults(func=export_text)
    text_parser.add_argument("file_path", type=str, help="Path to output file")
    text_parser.add_argument(
        "--delimiter",
        "-d",
        type=str,
        default=",",
        help=r"Delimiter to use---e.g. ',', '|'",
    )

    json_parser = subparsers.add_parser(
        name="json",
        help="Export as JSON document",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    json_parser.set_defaults(func=export_json)
    json_parser.add_argument("file_path", type=str, help="Path to output file")
    json_parser.add_argument(
        "--indent",
        "-i",
        type=int,
        default=None,
        help="Indentation level for pretty printing",
    )

    return parser.parse_args()


def main():
    """Performs the main task of the script."""

    args = parse_arguments()

    print(args)

    args.func(args)


if __name__ == "__main__":
    main()
