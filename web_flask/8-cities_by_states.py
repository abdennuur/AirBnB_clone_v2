#!/usr/bin/python3
"""Flask web app
"""

from flask import Flask, render_template
from models import *
from models import storage
my_App = Flask(__name__)


@my_App.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """To display states and cities listed in alphabet order"""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@my_App.teardown_appcontext
def teardown_db(exception):
    """To close storage on teardown"""
    storage.close()

if __name__ == '__main__':
    my_App.run(host='0.0.0.0', port='5000')
