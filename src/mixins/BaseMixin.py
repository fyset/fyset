
from src.plugins.sqla import sqla


class BaseMixin:
    """
    Extend basic models abilities
    for comfortable SQLAlchemy usage
    """

    @classmethod
    def create(cls, fields):
        obj = cls(**fields)
        sqla.session.add(obj)
        return obj

    def update(self, values):
        for k, v in values.items():
            setattr(self, k, v)
        return self

    def delete(self):
        sqla.session.delete(self)
