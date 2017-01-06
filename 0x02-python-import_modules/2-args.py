#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 0:
        print("{:d} argument.".format(len(argv) - 1))
    else:
        if len(agv) == 1:
            print("{:d} argument.".format(len(argv) - 1))

        print("{:d} arguments.".format(len(argv) - 1))
        for i in range(1, len(argv)):
            print("{:d}: {:s}".format(i, argv[i]))
