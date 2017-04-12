#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        print("No result")
    if len(sys.argv) > 1 and type(sys.argv[1]) is int:
        print("No result")
    elif len(sys.argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]
        data = {'q': letter}
        r = requests.post(url, data=data)
        try:
            print("[{}] {}".format(r.json()['id'], r.json()['name']))
        except:
            if r.json()['id'] is None:
                print("No result")
            else:
                print("Not a valid JSON")
