"""Solution to Chapter 6 pizza example."""

# Add import statements at the top of the source code

import itertools

toppings = [
    "pepperoni",
    "cheese",
    "ham",
    "bacon",
    "mushrooms",
    "peppers",
    "onions",
    "olives",
]

topping_count = 3

# Create a for loop to process the iterator

for three_toppings in itertools.combinations(toppings, topping_count):
    print("Pizza with", three_toppings)
