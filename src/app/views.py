from flask import render_template

from app import app


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/statistics')
def about():
    return render_template("statistics.html")
