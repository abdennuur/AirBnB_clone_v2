#!/usr/bin/python3
"""Flask web app
"""

from flask import Flask, render_template
my_App = Flask(__name__)


@my_App.route('/', strict_slashes=False)
def d_HELLO_HBNB():
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
    return 'C {}'.format(text.replace('_', ' '))


@my_App.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@my_App.route('/python/<text>', strict_slashes=False)
def d_P(text):
    """display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )"""
    return 'Python {}'.format(text.replace('_', ' '))


@my_App.route('/number/<int:n>', strict_slashes=False)
def isnbr(n):
    """display “n is a nbr” only if n is int"""
    return "{} is a number".format(n)


@my_App.route('/number_template/<int:n>', strict_slashes=False)
def template_Nbr(n):
    """display HTML page only if n is int"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    my_App.run(host='0.0.0.0', port='5000')
