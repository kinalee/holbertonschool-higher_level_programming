#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and
displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    stat = r.status_code
    if stat >= 400:
        print("Error code: {}".format(stat))
    else:
        print(r.text)
