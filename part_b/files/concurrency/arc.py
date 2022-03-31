#!/bin/bash
# pylint: disable=invalid-name

"""Demonstrates reference counting."""

from typing import Any, List, Optional

import sys


def main() -> None:
    """Performs the main task of the script."""

    a: Optional[List[Any]] = []
    b = a
    c = b

    # [] is referenced by a, b, c and getrefcount's argument
    print(f"a has {sys.getrefcount(a)} ref(s)")

    c = None

    print(f"c is now {c}")

    # [] is referenced by a, b and getrefcount's argument
    print(f"a has {sys.getrefcount(a)} ref(s)")


if __name__ == "__main__":
    main()
