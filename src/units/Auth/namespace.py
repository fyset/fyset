from flask_restplus import Namespace


auth = Namespace('Auth', path='/')


from .controllers import *
