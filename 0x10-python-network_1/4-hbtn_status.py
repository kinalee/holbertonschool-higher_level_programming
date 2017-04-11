#!/usr/bin/python3
import requests
"""
Fetches https://intranet.hbtn.io/status using requests package
"""


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t - type: {:}".format(type(r.content)))
    print("\t - content: {:}".format(r.content))
