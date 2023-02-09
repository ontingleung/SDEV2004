from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():

    return render_template("index.html", title = "Week 3 Index", content = "Example of template inheritance.")

@app.route('/about')
def about():

    return render_template("about.html", title = "About Week 3 App", content = "Example template inheritance using a navigation bar.")

@app.route('/test')
def test():

    return render_template("test.html", title = "Week 3 Test")
