#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastDigit = number % 10
else:
    lastDigit = ((number * -1) % 10) * -1

print("Last digit of {:d} is ".format(number), end="")

if lastDigit > 5:
    print("{:d} and is greater than 5".format(lastDigit))
elif lastDigit == 0:
    print("{:d} and is zero".format(lastDigit))
else:
    print("{:d} and is less than 6 and not 0".format(lastDigit))
