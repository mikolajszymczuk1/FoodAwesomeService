from flask import Response, request
from . import auth

# Login Endpoint
@auth.post('/login')
def login() -> Response:
    data = request.json
    return data
