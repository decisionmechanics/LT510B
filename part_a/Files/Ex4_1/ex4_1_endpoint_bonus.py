"""Solution to Exercise 4.1: Creating and Calling Functions bonus.

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


def list_all_cities():
    """Displays all the airport codes and names."""

    for airport, city in city_code_dictionary.items():
        print("Airport code", airport, "Airport name", city)


def flights_per_city(airport_code):
    """Displays all flights departing from an airport.

    Args:
      airport_code: The departure airport code.
    """

    for code, flight in flight_dictionary.items():
        if flight[0] == airport_code:
            print("Flight", code, "on the schedule", flight)


def flights_per_cities(departure_code, arrival_code):
    """Displays all flights between two airports.

    Args:
      departure_code: The departure airport code.
      arrival_code: The arrival airport code
    """

    return [
        code
        for code, flight in flight_dictionary
        if flight[0] == departure_code and flight[1] == arrival_code
    ]


# Part B

print("The list of airport codes and airports is")
list_all_cities()

search_city = "HNL"
search_city = "CUR"
search_city = "ITO"

search_cities = ["HNL", "CUR", "ITO"]  # put into a list
for search_city in search_cities:
    print("The flights from", search_city)
    flights_per_city(search_city)

departure_city = "NRT"
arrival_city = "ITO"
print("The flights from", departure_city, "to", arrival_city)
flights = flights_per_cities(departure_city, arrival_city)
for a_flight in flights:
    print("Flight", a_flight, "travels from", departure_city, "to", arrival_city)

departure_city = "HKG"
arrival_city = "HNL"
print("The flights from", departure_city, "to", arrival_city)
flights = flights_per_cities(departure_code=departure_city, arrival_code=arrival_city)
for a_flight in flights:
    print("Flight", a_flight, "travels from", departure_city, "to", arrival_city)


def discount(price, discount_rate):
    """Calculates a discounted price.

    Args:
      price: The original price.
      discount_rate: The discount rate (as a proportion).

    Returns:
      The discounted price.
    """

    return price - (price * discount_rate)


# Build list of price and discount pairs
price_discount_list = [[100, 0.05], [299, 0.15], [399.95, 0.10]]
for original_price, the_discount_rate in price_discount_list:
    print(
        f"""Original = {original_price} discount = {the_discount_rate} discounted = {
            discount(original_price, the_discount_rate)}"""
    )


def discount_printer(prices, discount_rates):
    """Displays discounted prices.

    Discounts, and displays, a sequence of prices by a matching sequence of discount
    rates.

    Args:
      prices: A sequence of original prices.
      discount_rates: A sequence of discount rates (as proportions).
    """

    for price, discount_rate in zip(prices, discount_rates):
        print(
            f"""Original = {price} discount = {discount_rate} discounted = {
                discount(price, discount_rate)}"""
        )


price_list = [100, 299, 399.95]
discount_list = [0.05, 0.15, 0.10]
discount_printer(price_list, discount_list)
