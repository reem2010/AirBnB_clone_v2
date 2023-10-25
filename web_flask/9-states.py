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


@app.route("/states")
@app.route("/states/<id>")
def states(id=None):
    states = storage.all(State).values()
    file_n = '9-states.html'
    return render_template(file_n, states=states, id_1=id)


if __name__ == '__main__':
    app.run()
