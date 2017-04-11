#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and
displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    try:
        print(r.text)
    except:
        err = r.status_code
        print("Error code: {:d}".format(err))
