""""Set membership quiz solution (Chapter 3).

Given the dictionaries below:

- Create a list of the keys in the codes dictionary that are also keys in the caps dictionary
- Create a list of the keys in the codes dictionary that are not keys in the caps dictionary

Hint 1: Use set operators & and -.
Hint 2: Shortcut, use set operators directly on the keys.
"""

# Given the following dictionaries:

codes = {"France": 33, "Japan": 81, "Great Britain": 44, "USA": 1}
caps = {"France": "Paris", "Cuba": "Havana", "Japan": "Tokyo"}

# Create a list of the keys in the codes dictionary
# that are also keys in the caps dictionary

match = list(set(codes.keys()) & set(caps.keys()))
print("set intersection", match)

# Or, use dictionary keys directly
match = list(codes.keys() & caps.keys())
print("keys intersection", match)

# Create a list of the keys in the codes dictionary
# that are not keys in the caps dictionary

match = list(set(codes.keys()) - set(caps.keys()))
print("set difference", match)

# Or, use dictionary keys directly
match = list(codes.keys() - caps.keys())
print("keys difference", match)

# HINT 1: Use set operators & and -
# HINT 2: Shortcut, use set operators directly on the keys
