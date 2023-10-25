#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(var):
    storage.close()


@app.route("/cities_by_states")
def cities():
    states = storage.all(State)
    cities = storage.all(City)
    file_n = '8-cities_by_states.html'
    return render_template(file_n, states=states, cities=cities)


if __name__ == '__main__':
    app.run()
