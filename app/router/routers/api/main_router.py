from app.models.models.http_method import HTTPMethod
from app.utils.env import Env
from app.utils.process import kill_process_on_port


class MainRouter(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app

    def init_router(self):
        @self.flask_app.route("/terminate", methods=[HTTPMethod.DELETE.value])
        def terminate():
            port = Env.MOCK_SERVER_FLASK_PORT
            kill_process_on_port(port)
            return ''
