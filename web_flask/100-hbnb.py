#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(var):
    storage.close()


@app.route("/hbnb")
def hbnb():
    states = storage.all(State)
    amens = storage.all(Amenity)
    places = storage.all(Place)
    file_n = '100-hbnb.html'
    return render_template(file_n, states=states, amens=amens, places=places)


if __name__ == '__main__':
    app.run()
