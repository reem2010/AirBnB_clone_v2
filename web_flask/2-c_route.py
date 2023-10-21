#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def route():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def C():
    return f"c {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run()
