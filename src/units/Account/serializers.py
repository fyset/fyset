from flask_restplus import fields

from .namespace import account


get = account.model('Account:GET', {
    'id': fields.Integer,
    'email': fields.String,
    'role': fields.String
})

post = account.model('Account:POST', {
    'email': fields.String,
    'password': fields.String,
    'role': fields.String
})

put = account.model('Account:PUT', {
    'email': fields.String,
    'password': fields.String,
    'role': fields.String
})
