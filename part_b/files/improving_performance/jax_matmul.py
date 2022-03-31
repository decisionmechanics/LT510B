#!/bin/bash

"""This module times the multiplication of large matrices."""

from __future__ import annotations

# Type annotations aren't used as there seems to be an issue with JAX types.

import time
import jax.numpy as jnp
from jax import random

KEY = random.PRNGKey(0)
SIZE = 10000


def main():
    """Times the multiplication of a matrix by its transpose."""

    numbers = random.normal(KEY, (SIZE, SIZE), dtype=jnp.float64)

    start_time = time.perf_counter()

    jnp.dot(numbers, numbers.T).block_until_ready()

    duration = time.perf_counter() - start_time

    print(f"JAX took {duration:.2f} second(s) to multiply the matrices")


if __name__ == "__main__":
    main()
