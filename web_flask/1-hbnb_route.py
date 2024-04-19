#!/usr/bin/python3
"""Flask web app
"""

from flask import Flask

my_App = Flask(__name__)


@my_App.route('/', strict_slashes=False)
def hello_HBNB():
    """displays Hello HBNB!"""
    return "Hello HBNB!"


@my_App.route('/hbnb', strict_slashes=False)
def HBNB():
    """display HBNB"""
    return "HBNB"


if __name__ == '__main__':
    my_App.run(host='0.0.0.0', port=5000)
