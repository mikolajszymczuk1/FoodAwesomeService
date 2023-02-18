from flask import request, jsonify, make_response
from flask.typing import ResponseReturnValue
from flask import current_app as app
from . import auth
from .models import User
from .. import db
from datetime import datetime, timedelta
import jwt

# Login Endpoint : https://www.geeksforgeeks.org/using-jwt-for-user-authentication-in-flask/
@auth.post('/login')
def login() -> ResponseReturnValue:
    # Login data from request
    data = request.json

    if not data or not data['email'] or not data['password']:
        return make_response(jsonify({ 'authenticate': 'Could not verify' }), 401, { 'WWW-Authenticate' : 'Login required !' })

    email: str = data['email']
    password: str = data['password']

    user = User.query.filter_by(email=email).first()
    if not user:
        return make_response(jsonify({ 'authenticate': 'Could not verify' }), 401, { 'WWW-Authenticate' : 'User does not exist !' })

    if user.verify_password(password):
        token = jwt.encode({
            'id': user.id,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, app.config['SECRET_KEY'])

        return make_response(jsonify({ 'token': token }), 201)

    return make_response(jsonify({ 'authenticate': 'Could not verify' }), 403, { 'WWW-Authenticate': '"Wrong password !' })


# Register Endpoint
@auth.post('/register')
def register() -> ResponseReturnValue:
    # Data from request
    data = request.json
    username: str = data['username']
    email: str = data['email']
    password: str = data['password']
    repeat_password: str = data['repeatPassword']

    # Create new user
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify({ 'response': 'OK', 'message': 'User has been created' }), 200
