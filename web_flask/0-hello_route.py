#!/usr/bin/python3

"""   setting up my first server with flask   """

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    """ return Hello HBNB! """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
