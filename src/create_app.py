from flask import Flask
from werkzeug.contrib.profiler import ProfilerMiddleware
import os

from src import plugins, commands


def create_app():

    # Create basic Flask app
    app = Flask(
            __name__,
            template_folder=f'{os.getcwd()}/templates',
            static_folder=f'{os.getcwd()}/static')

    # Init plugins
    plugins.init(app)

    # Init commands
    commands.init(app)

    # Profiler
    if os.environ.get('PROFILE'):
        app.wsgi_app = ProfilerMiddleware(
            app.wsgi_app,
            sort_by=('tottime',),
            restrictions=[os.environ.get('PROFILE_DEPTH') or 30])

    # Create tables if in-memory
    if os.environ.get('SQLALCHEMY_DATABASE_URI') == 'sqlite:///:memory:':
        with app.app_context():
            plugins.sqla.create_all()

    return app
