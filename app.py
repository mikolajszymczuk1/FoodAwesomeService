from flask import Flask

app = Flask(__name__)

@app.get('/')
def index() -> str:
    return '<h1>Food Awesome Service</h1>'
