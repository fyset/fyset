from sqlalchemy.ext.hybrid import hybrid_property

from src import mixins
from src.plugins import sqla, generate_hash


class Account(sqla.Model, mixins.BaseMixin):
    __tablename__ = 'accounts'

    id = sqla.Column(sqla.Integer, primary_key=True)
    email = sqla.Column(sqla.String, unique=True)
    _password = sqla.Column(sqla.String)
    role = sqla.Column(sqla.String)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_hash(value)
