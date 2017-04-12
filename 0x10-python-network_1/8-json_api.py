#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 2:
        letter = ""
    elif sys.argv[1] not str:
        print("No result")
        return
    else:
        letter = sys.argv[1]

    data = {'q': letter}
    r = requests.post(url, data=data)
    try:
        rjs = r.json()
        if rjs['id'] is None:
            print("No result")
        else:
            print("[{}] {}".format(rjs['id'], rjs['name']))
    except:
            print("Not a valid JSON")
