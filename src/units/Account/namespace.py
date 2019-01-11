from flask_restplus import Namespace


account = Namespace('Account', path='/')


from .controllers import *