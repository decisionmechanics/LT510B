#!/bin/bash
# pylint: disable=invalid-name

"""This module estimates PI using naive simulation."""

from random import random
import sys
from typing import Tuple


def generate_random_point() -> Tuple[float, float]:
    """Generates a random point in a bounded square.

    Returns:
      A random point (x, y).
    """

    x = random() * 2.0 - 1.0
    y = random() * 2.0 - 1.0

    return x, y


def is_inside_circle(x: float, y: float) -> bool:
    """Checks whether a point is inside a given circle.

    Args:
      x: x-coordinate of the point
      y: y-coordinate of the point

    Returns:
      True if the point is within the circle. False otherwise.
    """

    return x * x + y * y <= 1.0


def calculate_pi(number_of_samples: int, number_of_samples_inside_circle: int) -> float:
    """Estimates PI using the sampling data.

    Args:
      number_of_samples: Number of samples that were taken.
      number_of_samples: Number of samples that fell inside the defined circle.

    Returns:
      Estimate of PI.
    """

    return (number_of_samples_inside_circle / number_of_samples) * 4


def estimate_pi(number_of_samples: int) -> float:
    """Estimates PI.

    Uses a naive simulation approach. More samples leads to greater precision.

    Args:
      number_of_samples: Number of samples to take.

    Returns:
      Estimate of PI.
    """

    number_of_samples_inside_circle = 0

    for _ in range(number_of_samples):
        x, y = generate_random_point()

        if is_inside_circle(x, y):
            number_of_samples_inside_circle += 1

    return calculate_pi(number_of_samples, number_of_samples_inside_circle)


def main() -> None:
    """Estimates and displays the value of PI."""

    number_of_samples = 1_000_000

    if len(sys.argv) > 1:
        number_of_samples = int(sys.argv[1])

    pi = estimate_pi(number_of_samples)

    print(f"PI is esimated to be {pi:.4f} (using {number_of_samples} sample(s))")


if __name__ == "__main__":
    main()
