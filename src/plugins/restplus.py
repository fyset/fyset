from flask_restplus import Api
from flask import request, render_template, url_for
import os

from src.plugins import env


# Custom method for automatic finding serializer models
# and register them
def register_serializer(namespace, serializer):
    for serializer_attr in serializer.__dict__:
        if serializer_attr.startswith('__'):
            continue
        namespace.model(
            serializer.__dict__[serializer_attr].name,
            serializer.__dict__[serializer_attr])


# Correct HTTPS handling
class CustomApi(Api):

    @property
    def specs_url(self):
        """Monkey patch for HTTPS"""
        return url_for(
            self.endpoint('specs'),
            _external=True,
            _scheme='http')

    def _ui_for(self, api):
        """Render a SwaggerUI for a given API"""
        ui = f'{request.args.get("ui") or "swagger"}-ui.html'
        return render_template(ui, title=api.title,
                               specs_url=api.specs_url)

    def render_doc(self):
        """Override this method to customize the documentation page"""
        if self._doc_view:
            return self._doc_view()
        elif not self._doc:
            self.abort(404)
        return self._ui_for(self)


# Configs
authorizations = {
    'jwt': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}


# Init
restplus = CustomApi(
    title='API',
    version=os.environ.get('VERSION'),
    description='Base project API',
    authorizations=authorizations,
    validate=True
)


# Attach namespaces
from src.units.Account.namespace import account
restplus.add_namespace(account)
from src.units.Auth.namespace import auth
restplus.add_namespace(auth)
