"""Sample code for Chapter 3 query loop."""

creator = "Guido"
while (guess := input("Who is the creator of Python? ")) != creator:
    print("Sorry but", guess, "is not correct.  Try again")
else:
    print("Right, it is", creator)
