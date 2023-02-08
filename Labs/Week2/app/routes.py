from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Onting'}
    # return "Welcome to Lab Class WEEK TWO -Let the fun begin!"
    labclasses = [
        {
            'weekno': 'one',
            'content': 'Getting started with Flask!'
        },
        {
            'weekno': 'two',
            'content': 'Doing more with templates!'
        }
    ]
    return render_template('index.html', title='LabTWO', user=user, labclasses=labclasses)

# @app.route('/data_input/', methods=('GET', 'POST'))
# def data_input():
#     user = {'username': request.form.get('username')}
#     return render_template('index.html', title='Week 2', user=user)