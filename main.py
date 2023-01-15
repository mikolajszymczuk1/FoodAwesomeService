from os import getenv
from app import create_app
from flask import Flask

app: Flask = create_app(getenv('FLASK_CONFIG') or 'default')
