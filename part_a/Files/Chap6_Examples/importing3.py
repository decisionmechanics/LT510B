"""Sample code for Chapter 6 chaining module imports."""

# Chained Imports
import volumes

radius = 1.0
length = 2.0
area = volumes.circles.area(radius)
print(f"circle area {area}")
volume = volumes.cylinder_volume(radius, length)
print(f"cylinder volume {volume}")
