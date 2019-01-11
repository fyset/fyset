
from .wrap import wrap
from .hash import generate_hash

from .env import env
from .sqla import sqla
from .migrate import migrate
from .sqltap import sqltap
from .jwt import jwt
from .restplus import restplus


def init(app):
    env.init_app(app)
    sqla.init_app(app)
    migrate.init_app(app, sqla)
    sqltap.init_app(app)
    jwt.init_app(app)
    restplus.init_app(app)
