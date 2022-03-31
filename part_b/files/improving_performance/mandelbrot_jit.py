#!/bin/bash
# pylint: disable=invalid-name

"""This module times the generation of a JITed Mandelbrot set.

The code is adapted from https://bit.ly/3JFaK1h.
"""

import time
from typing import Tuple
import matplotlib.pyplot as plt
from matplotlib.pylab import imshow
from numba import jit
import numpy as np
import numpy.typing as npt


@jit(nopython=True)
def is_mandelbrot_candidate(x: float, y: float, maximum_iterations: int) -> int:
    """Determines if the point is in the set.

    Args:
      x: x coordinate of the point to test.
      y: y coordinate of the point to test.
      maximum_iterations: A bound on the depth of the calculation.

    Returns:
      A value representing the color to use in the image.
    """

    i = 0
    c = complex(x, y)
    z = 0.0j
    for i in range(maximum_iterations):
        z = z * z + c
        if (z.real * z.real + z.imag * z.imag) >= 4:
            return i

    return 255


@jit(nopython=True)
def create_fractal(
    image_size: Tuple[float, float, float, float], image, maximum_iterations: int
) -> npt.NDArray[np.uint8]:
    """Generates a Mandelbrot set image.

    Args:
      image_size: A tuple with the desired dimensions of the image.
      maximum_iterations: A bound on the depth of the calculation.

    Returns:
      A mandelbrot set image.
    """

    minimum_x, maximum_x, minimum_y, maximum_y = image_size

    height = image.shape[0]
    width = image.shape[1]

    pixel_size_x = (maximum_x - minimum_x) / width
    pixel_size_y = (maximum_y - minimum_y) / height

    for x in range(width):
        real = minimum_x + x * pixel_size_x
        for y in range(height):
            imaginary = minimum_y + y * pixel_size_y
            image[y, x] = is_mandelbrot_candidate(real, imaginary, maximum_iterations)

    return image


def main() -> None:
    """Creates a Mandelbrot image in a PNG file."""

    image_size = (-2.0, 1.0, -1.0, 1.0)
    image = np.zeros((500 * 2, 750 * 2), dtype=np.uint8)
    fractal = create_fractal(image_size, image, 20)

    start_time = time.perf_counter()
    create_fractal(image_size, image, 20)
    duration = time.perf_counter() - start_time
    print(f"2nd call to create_fractal executed in {duration:.2f} second(s)")

    imshow(fractal)
    plt.savefig("mandelbrot.png")


if __name__ == "__main__":
    main()
