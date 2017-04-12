#!/usr/bin/python3
"""
Takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import sys
import requests


if __name__ == "__main__":
    u = sys.argv[1]
    p = sys.argv[2]
    github = "https://api.github.com/user"
    req = requests.get(github, auth=(u, p)).json()
    print(req['id'])
