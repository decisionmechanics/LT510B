"""Sample code for Chapter 7 reading text."""

# Reading a Text File Example
try:
    in_file = open("/home/student/course/part_a/Data/simple.txt", "r")
    print(in_file.readline().rstrip())
    print(in_file.readlines())
    in_file.close()
except IOError as err:
    print("Error number", err.args[0])
    print("Message", err.args[1])
