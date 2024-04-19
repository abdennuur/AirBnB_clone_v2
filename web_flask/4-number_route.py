#!/usr/bin/python3
"""Flask web app
"""

from flask import Flask
my_App = Flask(__name__)


@my_App.route('/', strict_slashes=False)
def d_hello_hbnb():
    """display “Hello HBNB!”"""
    return "Hello HBNB!"


@my_App.route('/hbnb', strict_slashes=False)
def d_HBNB():
    """display “HBNB”"""
    return "HBNB"


@my_App.route('/c/<text>', strict_slashes=False)
def d_C(text):
    """display “C ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )"""
    return 'C ' + text.replace('_', ' ')


@my_App.route('/python', strict_slashes=False)
@my_App.route('/python/<text>', strict_slashes=False)
def d_P(text='is cool'):
    """display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )"""
    return 'Python ' + text.replace('_', ' ')


@my_App.route('/number/<int:n>', strict_slashes=False)
def is_nbr(n):
    """display “n is a number” only if n is an int"""
    return "{:d} is a number".format(n)


if __name__ == '__main__':
    my_App.run(host='0.0.0.0', port='5000')
