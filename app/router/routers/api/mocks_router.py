from app.models.models.http_method import HTTPMethod
from app.utils.utils_api import response_dumps


class MocksRouter(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app

    def init_router(self):
        # mocks
        @self.flask_app.route('/api/mocks', methods=[HTTPMethod.GET.value])
        def get_settings():
            return response_dumps(self.flask_app)
