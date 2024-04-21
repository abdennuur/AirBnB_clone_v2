#!/usr/bin/python3
"""Flask web app
"""
from models import storage
from flask import Flask
from flask import render_template

my_App = Flask(__name__)


@my_App.route("/hbnb", strict_slashes=False)
def hbnb():
    """To displays main HBNB filter HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@my_App.teardown_appcontext
def teardown(exc):
    """To remove current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    my_App.run(host="0.0.0.0")
