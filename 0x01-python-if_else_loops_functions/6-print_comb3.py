#!/usr/bin/python3
for i in range (100):
    if (i / 10 <  i % 10):
        if (i < 89):
            print("{:d}{:d},".format(i // 10, i % 10), end=" ")

        else:
            print("{:d}".format(i))
            break;
