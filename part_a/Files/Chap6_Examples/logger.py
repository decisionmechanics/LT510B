"""Sample code for Chapter 6 logging."""

# Namespace Corruption

import sys


def log(message):
    print(message, file=sys.stderr)
