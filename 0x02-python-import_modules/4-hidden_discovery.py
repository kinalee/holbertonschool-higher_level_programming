#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    count = 0
    for i in dir(hidden_4):
        if count > 7:
            print(i)
        count += 1
