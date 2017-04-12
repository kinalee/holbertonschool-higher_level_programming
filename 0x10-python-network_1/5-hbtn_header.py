#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    try:
        print(r.headers['X-Request-Id'])
    except:
        return None
