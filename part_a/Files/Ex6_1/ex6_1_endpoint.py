"""Solution to Exercise 6.1 Modules.

In this exercise, you will gain experience in taking advantage of module importing to use existing
code by creating a module file for use in another program.
"""

import airlineclasses as ac

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
    "Displays the attributes of a flight object."

    data_dictionary = dict(zip(flight_attributes, flight_data))
    flight = ac.Flight(**data_dictionary)
    print("Sample flight", vars(flight))


if __name__ == "__main__":
    main()
