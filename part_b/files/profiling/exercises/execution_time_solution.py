#!/bin/bash
# pylint: disable=line-too-long

"""Compares the performance off looking up values in lists and sets."""

from statistics import mean, stdev
import time
import timeit

LIST = list(range(100_000))
SET = set(range(100_000))


def lookup_in_list(value: int) -> bool:
    """Looks up a value in a list.

    Args:
      value: item to find.

    Returns:
      Whether the item is in the list.
    """

    return value in LIST


def lookup_in_set(value: int) -> bool:
    """Looks up a value in a set.

    Args:
      value: item to find.

    Returns:
      Whether the item is in the set.
    """

    return value in SET


def time_using_perf_counter() -> None:
    """Times and reports lookups in the list and set.

    Uses time.perf_counter for timing.
    """

    print("*** Using time.perf_counter ***")
    start = time.perf_counter()
    lookup_in_list(50_000)
    duration = time.perf_counter() - start
    print(f"Looking up list took {duration} second(s)")

    start = time.perf_counter()
    lookup_in_set(50_000)
    duration = time.perf_counter() - start
    print(f"Looking up set took {duration} second(s)")


def time_using_timeit() -> None:
    """Times and reports lookups in the list and set.

    Uses timeit for timing.
    """

    print("*** Using timeit ***")
    duration = timeit.repeat(stmt=lambda: lookup_in_list(50_000), number=1)
    print(f"Looking up list took {mean(duration)} second(s) (sd={stdev(duration)})")

    duration = timeit.repeat(stmt=lambda: lookup_in_set(50_000), number=1)
    print(f"Looking up set took {mean(duration)} second(s) (sd={stdev(duration)})")


def main() -> None:
    """Conducts performance timings using both time.perf_counter and timeit."""

    time_using_perf_counter()
    time_using_timeit()


if __name__ == "__main__":
    main()

# CLI commands
# python -m timeit --setup="import execution_time_solution" "execution_time_solution.lookup_in_list(50_000)"
# python -m timeit --setup="import execution_time_solution" "execution_time_solution.lookup_in_set(50_000)"
