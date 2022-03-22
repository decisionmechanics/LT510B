"""This module provides sample Flight and Reservation objects."""

import airlineclasses


flight1 = airlineclasses.Flight(
    flight_number=257,
    departure_city="HNL",
    arrival_city="YYZ",
    departure_day_time="2022-01-03 08:30",
    arrival_day_time="2022-01-03 15:40",
    cost=783.50,
    code=1,
)

flight2 = airlineclasses.Flight(
    flight_number=258,
    departure_city="CDG",
    arrival_city="LGA",
    departure_day_time="2022-01-03 19:20",
    arrival_day_time="2022-01-04 12:35",
    cost=783.50,
    code=1,
)

reservation_data1 = ("Lars Olsen", "200X", flight1)
reservation_data2 = ("Paul LeBeau", "201Y", flight2)

if __name__ == "__main__":
    print(reservation_data1, vars(flight1))
    print(reservation_data2, vars(flight2))
else:
    print("reservationdata.py imported, no reservation created")
