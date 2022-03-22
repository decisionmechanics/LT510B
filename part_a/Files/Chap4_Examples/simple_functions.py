"""Sample code for Chapter 4 functions."""

# Simple Function Example
def print_one():
    """Displays 1."""

    n = 1
    print("the value of n is", n)


def print_two():
    """Displays 2."""

    n = 2
    print("the value of n is", n)


print_one()
print_two()
print("The print_one object", print_one)

# Passing Data Into a Function
def print_position(depart, arrive):
    """Display the departure and arrival airport codes.

    Args:
      depart: Departure airport code.
      arrive: Arrival airport code.
    """

    print("depart and arrive by position:", depart, arrive)


print_position("NRT", "HNL")

# Keyword Parameters
def print_key(depart, arrive):
    """Display the departure and arrival airport codes.

    Args:
      depart: Departure airport code.
      arrive: Arrival airport code.
    """

    print("depart and arrive by keyword:", depart, arrive)


def print_default(depart="LAX", arrive="HNL"):
    print("depart and arrive defaults:", depart, arrive)


print_key(arrive="HNL", depart="NRT")
print_default(depart="AMS")

# Variable-Length Parameter List Example
def print_arguments(*args, **kwargs):
    """Displays all the arguments passed in.

    Args:
      args: Tuple of positional arguments.
      kwargs: Dictionary of keyword arguments.
    """

    print("Positional", args)
    print("Keyword", kwargs)


print_arguments("Jean", 35, 97.85)
print_arguments(name="Jean", age=35, rate=97.85)
print_arguments("Employee", name="Jean", age=35, rate=97.85)

# The following would cause a syntax error
# SyntaxError: positional argument follows keyword argument
# print_arguments(name="Jean", age=35, rate=97.85, "Employee")

# Variable-Length Argument Lists
employee1 = ["Jean", 35, 97.85]
employee2 = {"name": "Jules", "age": 29, "rate": 89.99}
print_arguments(*employee1)
print_arguments(**employee2)
print_arguments(employee2)

# Parameters and Scope
def increment(number):
    """Increments and displays a value.

    Args:
      number: Initial value to be incremented.
    """

    number += 1
    print("function number is", number)


number = 5
increment(number)
print("global number is", number)

# Enclosed Functions
def log_data():
    """Log message to stdout.

    Displays "Beginning status", "Processing...", then "Ending status".
    """

    def print_header():
        print("Beginning status")

    def print_footer():
        print("Ending status")

    print_header()
    print("Processing...")
    print_footer()


log_data()


# Scope
var = "global"


def fun1():
    """Displays the values of shadowed variables."""

    var = "enclosing"

    def fun2():
        var = "local"
        print("enclosed var:", var)

    fun2()
    print("enclosing var:", var)


fun1()
print("global var:", var)

# global statement
var = "global"


def fun1():
    """Modifies and displays the value of a global variable."""

    var = "enclosing"

    def fun2():
        global var
        var = "local"
        print(var)

    fun2()
    print(var)


fun1()
print(var)

# nonlocal statement
var = "global"


def fun1():
    """Modifies and displays the value of a non-local variable."""

    var = "enclosing"

    def fun2():
        nonlocal var
        var = "local"
        print(var)

    fun2()
    print(var)


fun1()
print(var)

# Function return Example
def add_twice(item):
    """Add a value to itself.

    Args:
      item: value that supports "+" operations

    Returns:
      The supplied value added to itself.
    """

    return item + item


def double_it(item):
    """Multiplies a value by 2.

    Args:
      item: value that supports "*" operations

    Returns:
      A tuple of the supplied value and the supplied value multiplied by 2.
    """
    return item, item * 2


answer = add_twice(3)
print("answer is", answer)
first, second = double_it("a")
print("first is", first, "second is", second)

# Mutable and Immutable Arguments
def add_one(n, handle):
    """Adds "one" to supplied values.

    Adds 1 to the first argument and appends "ONE" to the second.

    Args:
      n: A numeric value.
      handle: A list.
    """

    n += 1
    handle.append("ONE")
    print("Inside", handle, n)


name = ["Sam"]
count = 0
add_one(count, name)
print("Outside", name, count)

# Functions and Polymorphism
def twice(item):
    """Add a value to itself.

    Args:
      item: value that supports "+" operations

    Returns:
      The supplied value added to itself.
    """

    return item + item


print("Try twice()", twice(5.5))
print("Try twice()", twice(["a", "list"]))
# The following will cause a Type exception to be raised
# print(twice({'first_name': 'Robert', 'last_name': 'Johnson'}))
