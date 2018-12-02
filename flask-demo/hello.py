from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/test')
def hello_jack():
    return

@app.route('/<name>')
def get_name(name):
    return 'Hello, <i>{}</i>'.format(name.upper())
