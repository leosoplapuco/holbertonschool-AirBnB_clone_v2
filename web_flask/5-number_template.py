#!/usr/bin/python3

"""   render with templates   """

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_route():
    """ return Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb_route():
    """ return HBNB """
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    """ return c followed by the value """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/')
@app.route('/python/<text>')
def python_route(text="is cool"):
    """ return followed by the value of the text variable """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>')
def number_route(n):
    """display n is a number only if n is integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """display a HTML page"""
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
