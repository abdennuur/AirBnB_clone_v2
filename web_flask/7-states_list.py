#!/usr/bin/python3
"""Flask web app
"""

from flask import Flask, render_template
from models import *
from models import storage
my_App = Flask(__name__)


@my_App.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all State objects"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@my_App.teardown_appcontext
def teardown_db(exception):
    """To Remove current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    my_App.run(host='0.0.0.0', port='5000')
