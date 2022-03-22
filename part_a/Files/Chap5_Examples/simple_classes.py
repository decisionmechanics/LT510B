"""Sample code for Chapter 5 simple classes."""

# The __init__() Method
class Cruise:
    """Describes a cruise.

    Attributes:
      ship: The name of the ship.
      cost: The accumulating cost ($) of the cruise.
      cabin: The passenger's cabin number.
    """

    def __init__(self, ship=None, cost=0.0, cabin=0):
        """Initializes a Cruise with no ship, $0 cost and cabin 0 (by default)."""

        self.ship = ship
        self.cost = cost
        self.cabin = cabin


# The self Parameter
my_vacation = Cruise(ship="Voyager", cabin=101)
your_vacation = Cruise(ship="Sundowner", cost=157.50, cabin=511)
print(my_vacation.ship, my_vacation.cabin, my_vacation.cost)
print(your_vacation.ship, your_vacation.cabin, your_vacation.cost)

# __init__() Parameter Styles
class Cruise:
    """Describes a cruise.

    Attributes:
      ship: The name of the ship.
      cost: The accumulating cost ($) of the cruise.
      cabin: The passenger's cabin number.
    """

    def __init__(self, ship_name, price, room):
        """Initializes a Cruise with no ship, $0 cost and cabin 0 (by default)."""

        self.ship = ship_name
        self.cost = price
        self.cabin = room


my_vacation = Cruise(shipname="Voyager", price=0, room=101)
your_vacation = Cruise("Sundowner", 157.50, 511)
print(my_vacation.ship, my_vacation.cabin, my_vacation.cost)
print(your_vacation.ship, your_vacation.cabin, your_vacation.cost)

# Modifying Instance Attributes
my_vacation.cost = 400.0
my_vacation.cabin = 104
print(my_vacation.ship, my_vacation.cabin, my_vacation.cost)
print(your_vacation.ship, your_vacation.cabin, your_vacation.cost)


# Methods
class Cruise:
    """Describes a cruise.

    Attributes:
      ship: The name of the ship.
      cost: The accumulating cost ($) of the cruise.
      cabin: The passenger's cabin number.
    """

    def __init__(self, ship=None, cost=0.0, cabin=0):
        """Initializes a Cruise with no ship, $0 cost and cabin 0 (by default)."""

        self.ship = ship
        self.cost = cost
        self.cabin = cabin

    def dine(self, amount):
        """Increments the cost of your cruise by the price of your meal.

        Args:
            amount: Price of the meal.
        """

        self.cost += amount


my_vacation = Cruise(ship="Voyager", cabin=101)
your_vacation = Cruise(ship="Sundowner", cost=157.50, cabin=511)
my_vacation.dine(125.0)
your_vacation.dine(215.50)
print("my_vacation", my_vacation.cost)
print("your_vacation", your_vacation.cost)

# Class Attributes
class Cruise:
    """Describes a cruise.

    Attributes:
      ship: The name of the ship.
      cost: The accumulating cost ($) of the cruise.
      cabin: The passenger's cabin number.
    """

    premium_cabins = (101, 102, 105, 106, 109, 110)

    def __init__(self, ship=None, cost=0.0, cabin=0):
        """Initializes a Cruise with no ship, $0 cost ($50 for a premium cabin) and cabin 0 (by default)."""

        self.ship = ship
        self.cost = cost
        self.cabin = cabin
        self.charge_upgrade()

    def charge_upgrade(self):
        """Applies a surcharge if the customer is in a premium cabin."""

        if self.cabin in Cruise.premium_cabins:
            self.cost += 50.0


my_vacation = Cruise(ship="Voyager", cabin=101)
print(my_vacation.cost)
