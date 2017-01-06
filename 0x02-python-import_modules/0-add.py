#!/usr/bin/python3
from add_0 import add
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

a = 1
b = 2
res = add(a, b)
print("{:d} + {:d} = {:d}".format(a, b, res))
