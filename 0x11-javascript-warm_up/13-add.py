#!/usr/bin/python3
""" Returns the addition of 2 integers """
from flask import Flask
app = Flask(__name__)

@app.route("/", methods=['GET'], strict_slashes=false)
def add(a, b):
    return a + b

if __name__ == "__main__":
    app.run()
