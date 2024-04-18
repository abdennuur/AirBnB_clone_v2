#!/usr/bin/python3
"""
To start a Flask web app
"""

from flask import Flask
my_App = Flask(__name__)


@my_App.route('/', strict_slashes=False)
def index():
    """To display Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == '__main__':
    my_App.run(host='0.0.0.0', port=5000)
