"""Sample code for Chapter 6 importing modules."""

# Module Execution
import circles

print(circles)

# Module Attributes
radius = 1.0
print(circles.PI)
area = circles.area(radius)
print(f"circle is radius {radius} area {area}")
