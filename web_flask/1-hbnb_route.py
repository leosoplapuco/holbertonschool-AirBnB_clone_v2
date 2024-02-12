#!/usr/bin/python3

"""   Adding route hbnb   """

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    """ return Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ return HBNB """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
