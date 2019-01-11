from flask import request, abort, g
from time import time
import jwt as jwtlib
import os

from src.units.Account.model import Account


class JWT:

    def __init__(self):
        pass

    def init_app(self, app):
        pass

    def required(self, f):
        def wrapper(*args, **kwargs):
            # Extract
            auth = request.headers.get('Authorization')
            # Abort if token is not set
            if not auth:
                return abort(401)
            # Auth for JWT token
            if 'JWT' in auth:
                # Extract token
                token = auth.replace('JWT ', '')
                # Extract payload from token
                payload = jwtlib.decode(token, os.environ.get('SECRET'), algorithms=['HS256'])
                # Check timestamp
                if (time() - payload.get('timestamp')) > int(os.environ.get('JWT_LIFETIME')):
                    return abort(401, 'Token expired')
                # Extract account
                account = Account.query.get(payload.get('id'))
                # Handle no account case
                if not account:
                    return abort(401, 'Account does not exist')
                # Set global account
                g.account = account
                # Call controller
                return f(*args, **kwargs)
        return wrapper

    def allowed(self, roles):
        def outer_wrapper(f):
            def inner_wrapper(*args, **kwargs):
                if g.account.role not in roles:
                    return abort(403, 'Not allowed')
                return f(*args, **kwargs)
            return inner_wrapper
        return outer_wrapper

    def generate(self, user_id):
        return jwtlib.encode({'id': user_id, 'timestamp': time()}, os.environ.get('SECRET'), algorithm='HS256').decode('utf-8')


jwt = JWT()
