"""Sample code for Chapter 6 importing multiple modules."""

# Multiple Imports
import circles
import volumes

radius = 1.0
length = 2.0
area = circles.area(radius)
print(f"circle area {area}")
volume = volumes.cylinder_volume(radius, length)
print(f"cylinder volume {volume}")
