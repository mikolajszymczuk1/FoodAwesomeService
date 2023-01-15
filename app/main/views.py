from flask import render_template
from . import main

# Base view
@main.get('/')
def index() -> str:
    msg: str = 'Food Awesome Service'
    return render_template('index.html', msg=msg)
