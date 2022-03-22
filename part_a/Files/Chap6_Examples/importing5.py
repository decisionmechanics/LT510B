"""Sample code for Chapter 6 namespace corruption."""

# Namespace Corruption

from logger import *

log("test 1 error message")

from math import *

log("test 2 error message")
