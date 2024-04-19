#!/usr/bin/python3
"""Flask web app
"""

from flask import Flask
my_App = Flask(__name__)


@my_App.route('/', strict_slashes=False)
def display_hello_hbnb():
    """display “Hello HBNB!”"""
    return "Hello HBNB!"


@my_App.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """display “HBNB”"""
    return "HBNB"


@my_App.route('/c/<text>', strict_slashes=False)
def display_C(txt):
    """display “C ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )"""
    return 'C ' + txt.replace('_', ' ')


@my_App.route('/python', strict_slashes=False)
@my_App.route('/python/<text>', strict_slashes=False)
def display_P(text="is cool"):
    """display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )"""
    return 'Python ' + text.replace('_', ' ')

if __name__ == '__main__':
    my_App.run(host='0.0.0.0', port='5000')
