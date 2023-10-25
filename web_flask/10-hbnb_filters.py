#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(var):
    storage.close()


@app.route("/hbnb_filters")
def hbnb_filters():
    states = storage.all(State)
    amens = storage.all(Amenity)
    file_n = '10-hbnb_filters.html'
    return render_template(file_n, states=states, amens=amens)


if __name__ == '__main__':
    app.run()
