
from .create_account import create_account
from .create_unit import create_unit
from .delete_unit import delete_unit


def init(app):
    app.cli.command('create:account')(create_account)
    app.cli.command('create:unit')(create_unit)
    app.cli.command('delete:unit')(delete_unit)
