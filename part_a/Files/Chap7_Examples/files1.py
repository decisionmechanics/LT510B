"""Sample code for Chapter 7 opening files."""

# Opening Files and Exceptions
try:
    in_file = open("incorrect_filename")
except IOError as err:
    print("Unable to open the file")
    print("Error number", err.args[0])
    print("Message", err.args[1])
    print("Filename in error", err.filename)
