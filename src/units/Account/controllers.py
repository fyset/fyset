from flask_restplus import Resource
from flask import request

from src.plugins import wrap, sqla, jwt

from . import validators, serializers
from .model import Account
from .namespace import account


@account.route('/accounts')
class AccountsCollection(Resource):

    @account.doc(security='jwt')
    @account.marshal_with(serializers.get)
    @jwt.required
    def get(self):
        return Account.query.all()

    @account.expect(serializers.post)
    @account.marshal_with(serializers.get)
    @jwt.required
    @jwt.allowed(['admin'])
    @wrap(validators.create)
    def post(self):
        account = Account.create(request.json)
        sqla.session.commit()
        return account


@account.route('/accounts/<int:id>')
class AccountID(Resource):

    @account.doc(security='jwt')
    @account.marshal_with(serializers.get)
    @jwt.required
    def get(self, id: int):
        return Account.query.get(id)

    @account.doc(security='jwt')
    @wrap(validators.update)
    @jwt.required
    def put(self, id: int):
        account = Account.query.get(id)
        account.update(request.json)
        sqla.session.commit()
        return account

    @account.doc(security='jwt')
    @wrap(validators.delete)
    @jwt.required
    def delete(self, id: int):
        account = Account.query.get(id)
        account.delete()
        sqla.session.commit()
        return {'message': f'Account {id} deleted'}
