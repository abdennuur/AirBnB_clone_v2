#!/usr/bin/python3
"""
Flask web app
"""

from flask import Flask, render_template
from models import *
from models import storage
my_App = Flask(__name__)


@my_App.route('/states', strict_slashes=False)
@my_App.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """display the states and cities listed in alphabetical order"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@my_App.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    my_App.run(host='0.0.0.0', port='5000')
