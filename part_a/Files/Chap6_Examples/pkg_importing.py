"""Sample code for Chapter 6 importing packages."""

# Package Example
import geometry.two_d.circles as ci
from geometry.three_d.volumes import cylinder_volume as cv

radius = 1.0
length = 2.0
area = ci.area(radius)
print(f"circle area {area}")
volume = cv(radius, length)
print(f"cylinder volume {volume}")
