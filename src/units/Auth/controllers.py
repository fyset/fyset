from flask_restplus import Resource
from flask import request, abort

from src.units.Account.model import Account
from src.plugins import generate_hash, jwt

from . import serializers
from .namespace import auth


@auth.route('/login')
class Login(Resource):

    @auth.expect(serializers.post)
    @auth.marshal_with(serializers.get)
    def post(self):
        # Find account
        account = Account.query.filter_by(
            email=request.json.get('email'),
            password=generate_hash(request.json.get('password'))
        ).first()
        # Handle no account case
        if not account:
            return abort(401)
        # Generate token
        jwt_token = jwt.generate(account.id)
        # Return
        return dict(
            id=account.id,
            type='jwt',
            token=jwt_token)
