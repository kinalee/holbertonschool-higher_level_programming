#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) != 2 or not sys.argv[1].isalpha():
        print("No result")
    else:
        letter = sys.argv[1]
        data = {'q': letter}
        r = requests.post(url, data=data)
        try:
            rjs = r.json()
            print("[{}] {}".format(rjs.get('id'), rjs.get('name')))
        except:
            print("Not a valid JSON")
