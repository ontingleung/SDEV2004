from app import app
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World from Lab Class Week 1!"