#!/usr/bin/python3
from flask import Flask

"""   setting up my first server with flask   """

app = Flask(__name__)

@app.route("/")
def home():
    """ return Hello HBNB! """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
