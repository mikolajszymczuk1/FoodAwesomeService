from flask import request, jsonify
from flask.typing import ResponseReturnValue
from . import auth

# Login Endpoint
@auth.post('/login')
def login() -> ResponseReturnValue:
    data = request.json
    return jsonify({ 'response': 'OK', 'data': data})
