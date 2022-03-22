"""Sample code for Chapter 6 testing __name__ attributes."""


class Person:
    """Describes a person.

    Attibutes:
      name: Person's name.
    """

    def __init__(self, name):
        """Initialize a Person with name."""
        self.name = name


def check_person():
    """Checks that Person objects are initialized with the correct name."""

    test_name = "Katrina"
    student = Person(test_name)
    if student.name == test_name:
        print("Person constructor ok")


if __name__ == "__main__":
    check_person()
