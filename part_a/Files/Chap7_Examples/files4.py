"""Sample code for Chapter 7 context manager."""

# Using with to Open and Close Files
try:
    with open("/home/student/course/part_a/Data/simple.txt", "r") as in_file:
        print(in_file.readline().rstrip())
        print(in_file.readlines())
        in_file.write("line 5\n")

except IOError as err:
    print("Read or Write error on file", err.args)
