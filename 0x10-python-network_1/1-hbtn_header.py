#!/usr/bin/python3
import sys
import urllib.request
"""
Takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response
"""

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1])as r:
        header = r.info()
    print(header['X-Request-Id'])