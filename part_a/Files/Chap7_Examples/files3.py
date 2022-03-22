"""Sample code for Chapter 7 handling IO exceptions."""

# Data Handling Exceptions
try:
    in_file = open("/home/student/course/part_a/Data/simple.txt", "r")
    try:
        print(in_file.readline().rstrip())
        print(in_file.readlines())
        in_file.write("line 5\n")
    except IOError:
        print("Read or Write error on file")
    finally:
        in_file.close()
except IOError as err:
    print("Failed to open the file", err.args)
