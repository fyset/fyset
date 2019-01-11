import click
import os


@click.option('-n', '--name', help='unit/namespace/model name')
@click.option('-t', '--table', help='database table name for model')
@click.option('-r', '--route', help='route for controllers')
def create_unit(name: str, table: str, route: str):
    pass

    # Define vars
    unit_path = f'./src/units/{name}'

    # Check dir
    if os.path.exists(unit_path):
        raise Exception('Unit already exist')

    # Create dir
    os.mkdir(unit_path)

    # Create namespace
    open(os.path.join(unit_path, 'namespace.py'), 'w').write(
        namespace_template.format(name, name.lower()))

    # Create base model
    open(os.path.join(unit_path, 'model.py'), 'w').write(
        model_template.format(name, table))

    # Create base serializers
    open(os.path.join(unit_path, 'serializers.py'), 'w').write(
        serializers_template.format(name.lower(), name))

    # Create base validators
    open(os.path.join(unit_path, 'validators.py'), 'w').write(
        validators_template)

    # Create base controllers
    open(os.path.join(unit_path, 'controllers.py'), 'w').write(
        controllers_template.format(name, name.lower(), route))

    # Add record to restplus
    open('./src/plugins/restplus.py', 'a').write(
        restplus_record.format(name, name.lower()))


# File templates

# 0 - Model name
# 1 - Namespace name
namespace_template = \
'''
from flask_restplus import Namespace


{1} = Namespace('{0}', path='/')


from .controllers import *
'''


# 0 - Model name
# 1 - Table name
model_template = \
'''

from src import mixins
from src.plugins import sqla


class {0}(sqla.Model, mixins.BaseMixin):
    __tablename__ = '{1}'

    id = sqla.Column(sqla.Integer, primary_key=True)
'''


# 0 - Namespace name
serializers_template = \
'''
from flask_restplus import fields

from .namespace import {0}


get = {0}.model('{1}:GET', {{
    'id': fields.Integer
}})

post = {0}.model('{1}:POST', {{
}})

put = {0}.model('{1}:PUT', {{
}})
'''


validators_template = \
'''

def create(func, *args, **kwargs):
    return func(*args, **kwargs)


def update(func, *args, **kwargs):
    return func(*args, **kwargs)


def delete(func, *args, **kwargs):
    return func(*args, **kwargs)

'''


# 0 - Model name
# 1 - Namespace name
# 2 - Route
controllers_template = \
'''
from flask_restplus import Resource
from flask import request

from src.plugins import wrap, sqla

from . import validators, serializers
from .model import {0}
from .namespace import {1}


@{1}.route('{2}')
class {0}Collection(Resource):

    @{1}.marshal_with(serializers.get)
    def get(self):
        return {0}.query.all()

    @{1}.expect(serializers.post)
    @{1}.marshal_with(serializers.get)
    @wrap(validators.create)
    def post(self):
        obj = {0}.create(request.json)
        sqla.session.commit()
        return obj


@{1}.route('{2}/<int:id>')
class {0}ID(Resource):

    @{1}.marshal_with(serializers.get)
    def get(self, id: int):
        return {0}.query.get(id)

    @wrap(validators.update)
    def put(self, id: int):
        obj = {0}.query.get(id)
        obj.update(request.json)
        sqla.session.commit()
        return obj

    @wrap(validators.delete)
    def delete(self, id: int):
        obj = {0}.query.get(id)
        obj.delete()
        sqla.session.commit()
        return {{'message': f'{0} {{id}} deleted'}}

'''


# 0 - Model name
# 1 - Namespace name
restplus_record = \
'''from src.units.{0}.namespace import {1}
restplus.add_namespace({1})
'''