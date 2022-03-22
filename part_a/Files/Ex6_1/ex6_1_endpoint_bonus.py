"""Solution to Exercise 6.1 Modules bonus.

In this exercise, you will gain experience in taking advantage of module importing to use existing
code by creating a module file for use in another program.
"""

import shutil
import glob
import airlineclasses as ac
import reservationclass
import reservationdata

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
    "Displays the results of the bonus exercise."

    data_dictionary = dict(zip(flight_attributes, flight_data))
    flight = ac.Flight(**data_dictionary)
    print("\nSample flight:\n", vars(flight))

    reservation1 = reservationclass.Reservation(*reservationdata.reservation_data1)
    reservation2 = reservationclass.Reservation(*reservationdata.reservation_data2)
    print("\nSample Reservation 1:")
    print(vars(reservation1), vars(reservation1.flight_reference), sep="\n")
    print("\nSample Reservation 2:")
    print(vars(reservation2), vars(reservation2.flight_reference), sep="\n")

    shutil.copy("reservationdata.py", "reservationdata.backup")
    print("The python files")
    for name in glob.glob("*.py"):
        print(name)


if __name__ == "__main__":
    main()
