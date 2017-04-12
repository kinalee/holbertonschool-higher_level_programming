#!/usr/bin/python3
"""
Takes in a string and sends a search request to the Star Wars API
"""
import sys
import requests


if __name__ == "__main__":
    swapi = "https://swapi.co/api/people/?search=" + sys.argv[1]
    req = requests.get(swapi)
    r = req.json()
    print("Number of result: {}".format(r['count']))

    for data in r['results']:
        print(data['name'])
