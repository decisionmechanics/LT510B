"""Sample code for Chapter 6 importing attributes directly into scope."""

# from Statement
from circles import area
from volumes import cylinder_volume as cv

radius = 1.0
length = 2.0
circle_area = area(radius)
print(f"circle area {circle_area}")
volume = cv(radius, length)
print(f"cylinder volume {volume}")
