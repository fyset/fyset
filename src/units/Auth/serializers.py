from flask_restplus import fields

from .namespace import auth


post = auth.model('Login:POST', {
    'email': fields.String,
    'password': fields.String
})

get = auth.model('Token:GET', {
    'id': fields.Integer,
    'type': fields.String,
    'token': fields.String,
})
