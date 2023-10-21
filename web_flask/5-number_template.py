#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def route():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def c_lang(text):
    return f"C {text.replace('_', ' ')}"


@app.route("/python")
@app.route("/python/<text>")
def py_lang(text="is cool"):
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>")
def num(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def num_temp(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run()
