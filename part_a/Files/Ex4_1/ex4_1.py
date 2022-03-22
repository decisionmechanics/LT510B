"""Starting point for Exercise 4.1: Creating and Calling Functions.

In this exercise, you will gain experience creating and calling a function, passing arguments,
and capturing the function's returned value.

- Create a function using the def statement
- Call a function passing in an argument list
- Return results from functions
"""

# Data for the exercise
# Please do not modify these dictionaries

# Description of city data
#
# Airport Code : Airport Name

city_code_dictionary = {
    "HNL": "Honolulu",
    "ITO": "Hilo",
    "LHR": "London/Heathrow",
    "ARN": "Stockholm/Arlanda",
    "HKG": "Hong Kong",
    "YYZ": "Toronto",
    "CDG": "Paris/Charles de Gaulle",
    "NRT": "Tokyo/Narita",
    "GCM": "Grand Cayman BWI",
    "CUR": "Curacao Netherland Antilles",
}

# Description of flight data
#
# Flight Number : [
#     Departure City,
#     Arrival City,
#     Departure Day/Time,
#     Arrival Day/Time,
#     Cost,
#     Code
# ]

flight_dictionary = {
    102: ["HNL", "HKG", "2022-01-03 16:00", "2022-01-03 20:00", 99.95, 4],
    132: ["HNL", "HNL", "2022-01-03 08:30", "2022-01-03 15:40", 59.0, 2],
    276: ["HKG", "CDG", "2022-01-03 19:20", "2022-01-04 12:35", 233.99, 2],
    303: ["HKG", "ARN", "2022-01-03 16:50", "2022-01-04 13:30", 233.99, 2],
    498: ["NRT", "ITO", "2022-01-03 12:00", "2022-01-03 20:55", 159.99, 2],
    390: ["CUR", "CUR", "2022-01-03 09:00", "2022-01-03 16:30", 599.95, 3],
    465: ["NRT", "YYZ", "2022-01-03 20:15", "2022-01-04 09:45", 59.0, 3],
    1305: ["ITO", "ARN", "2022-01-03 18:50", "2022-01-04 10:00", 125.0, 2],
    375: ["HKG", "HNL", "2022-01-03 09:10", "2022-01-03 16:30", 299.99, 4],
    444: ["NRT", "LHR", "2022-01-03 23:15", "2022-01-04 13:20", 125.0, 3],
    1572: ["HNL", "HNL", "2022-01-03 09:40", "2022-01-03 16:10", 125.0, 2],
}

# Part A

# Part B

search_city = "HNL"
search_city = "CUR"
search_city = "ITO"

departure_city = "NRT"
arrival_city = "ITO"
