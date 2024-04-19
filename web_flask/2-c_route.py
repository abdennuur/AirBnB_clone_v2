#!/usr/bin/python3
"""Flask web app
"""
from flask import Flask

my_App = Flask(__name__)


@my_App.route("/", strict_slashes=False)
def hello_world():
    """Displays Hello HBNB!
    """
    return "Hello HBNB!"


@my_App.route("/hbnb", strict_slashes=False)
def HBNB():
    """Displays HBNB"""
    return "HBNB"


@my_App.route('/c/<text>', strict_slashes=False)
def text(text):
    """display “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    my_App.run(host='0.0.0.0', port='5000')
