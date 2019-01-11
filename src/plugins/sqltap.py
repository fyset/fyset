from flask import request
import sqltap as tap
import os


class SQLTap:
    """Module for debugging SQL queries"""

    def __init__(self, app=None):
        if app is not None:
            raise NotImplementedError

    def init_app(self, app):
        if os.environ.get('SQLTAP'):
            app.before_request(self.before_request)
            app.after_request(self.after_request)

    def before_request(self):
        if request.path not in os.environ.get('SQLTAP_EXCLUDE'):
            self.processing = True
            self.profiler = tap.start()
        else:
            self.processing = False

    def after_request(self, resp):
        if self.processing:
            stats = self.profiler.collect()
            tap.report(
                stats,
                os.environ.get('SQLTAP_PATH'))
        return resp


sqltap = SQLTap()
