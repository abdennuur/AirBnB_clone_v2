#!/usr/bin/python3
"""
Flask web app
"""

from flask import Flask, render_template
from models import *
from models import storage
my_App = Flask(__name__)


@my_App.route('/hbnb_filters', strict_slashes=False)
def filters():
    """To display HTML page lk 6-index.html frm static"""
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@my_App.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    my_App.run(host='0.0.0.0', port='5000')
