from flask import request

from app.core.mocking_manager import MockingManager
from app.models.models.http_method import HTTPMethod


class ProxyRouter(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app

    def init_router(self):
        @self.flask_app.route('/', defaults={'path': ''})
        @self.flask_app.route('/<path:path>', methods=map(lambda item: item.value, HTTPMethod.supported_methods()))
        def proxy(path: str):
            path = f'/{path}'
            mocking_manager = MockingManager(self.flask_app)
            return mocking_manager.response(request, path)
