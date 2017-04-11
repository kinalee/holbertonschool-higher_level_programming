#!/usr/bin/python3
import sys
import urllib.request
import urllib.error
"""
Takes in a URL, sends a request to the URL
and displays the body of the response
"""


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as r:
            print(r.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {:d}".format(e.code))
