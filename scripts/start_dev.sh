#!/bin/bash

source ./../env/bin/activate

# Set base env variables
export FLASK_APP=../app.py
export FLASK_DEBUG=1
export FLASK_ENV=development

# Run app
flask run --port=5000
