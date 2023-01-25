from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Onting Leung'}
    return render_template('index.html', title='Lab Class Week 1', user=user)