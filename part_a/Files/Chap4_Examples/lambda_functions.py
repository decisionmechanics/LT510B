"""Sample code for Chapter 4 lambda functions."""

# The sorted() Function
costs = (("YYZ", "35"), ("HNL", "100"), ("NRT", "52.5"))
print(sorted(costs))
print(sorted(costs, key=lambda p: p[1]))
print(sorted(costs, key=lambda p: float(p[1])))

# Functions as Arguments
def print_german():
    """Displays 'Good Morning' in German."""

    print("Guten Morgen")


def print_italian():
    """Displays 'Good Morning' in Italian."""

    print("Buon Giorno")


def print_greeting(lang, printer):
    """Displays a language and a message in that language.

    Args:
      lang: A string denoting a natural language.
      printer: A function that displays a message.
    """

    print("Good Morning in", lang, "is", end=" ")
    printer()


print_greeting("German", print_german)
print_greeting("Italian", print_italian)

# Hiding Function Calls in Lambda Expressions
def print_german(name):
    """Displays 'Good Morning' to a named person in German.

    Args:
      name: Name of person (string) to be wished a good morning.
    """

    print("Guten Morgen", name)


def print_italian(name):
    """Displays 'Good Morning' to a named person in Italian.

    Args:
      name: Name of person (string) to be wished a good morning.
    """

    print("Buon Giorno", name)


def print_greeting(lang, printer):
    """Displays a language and a greeting in that language.

    Args:
      lang: A string denoting a natural language.
      printer: A function that displays a message.
    """

    print("Good Morning in", lang, "is", end=" ")
    printer()


print_greeting("German", lambda: print_german("Hans"))
print_greeting("Italian", lambda: print_italian("Gina"))
