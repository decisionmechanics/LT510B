"""Sample code for Chapter 7 reading text files line by line."""

# Using Loops and Iterators for File Access
try:
    with open("/home/student/course/part_a/Data/simple.txt", "r") as in_file:
        for line in in_file:
            print(line.rstrip())

except IOError as err:
    print("Read or Write error on file", err.args)
