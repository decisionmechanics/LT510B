"""Starting point for Exercise 6.1 Modules.

In this exercise, you will gain experience in taking advantage of module importing to use existing
code by creating a module file for use in another program.
"""

flight_data = (221, "HNL", "HNL", "2022-01-03 08:30", "2022-01-03 15:40", 399.99, 2)

flight_attributes = (
    "flight_number",
    "departure_city",
    "arrival_city",
    "departure_day_time",
    "arrival_day_time",
    "cost",
    "code",
)


def main():
    "Displays a message."

    print("This is main()")


if __name__ == "__main__":
    main()
