import click

from src.units.Account.model import Account
from src.plugins import sqla


@click.option('-e', '--email')
@click.option('--password', prompt=True, hide_input=True,
              confirmation_prompt=True)
@click.option('-r', '--role')
def create_account(**kwargs):
    Account.create(kwargs)
    sqla.session.commit()
    print('Account created')
