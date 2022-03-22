"""Solution to Chapter 6 date/time conversion example."""

# Using Standard Library and Documentation

import datetime

# Below are two strings that represent a date and time
departure_day_time = "2022-01-03 09:00"
arrival_day_time = "2022-01-03 16:00"

# Import the needed modules to convert both strings into datetime objects

# Compare these datetime objects using > to decide which is later

departure_day_time = datetime.datetime.fromisoformat(departure_day_time)
arrival_day_time = datetime.datetime.fromisoformat(arrival_day_time)

order = "Follows" if arrival_day_time > departure_day_time else "Precedes"
print(arrival_day_time, order, departure_day_time)
