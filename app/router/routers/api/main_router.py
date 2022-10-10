from app.models.models.http_method import HTTPMethod
from app.utils.env import Env
from app.utils.process import kill_process_on_port


class MainRouter(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app

    def init_router(self):
        @self.flask_app.route("/api/terminate", methods=[HTTPMethod.DELETE.value])
        def terminate():
            """Terminate server
                This method allows to remotely terminate MockServer.
                ---
                tags: [main]
                responses:
                  200:
                    description: Server terminates the connection
                """
            port = Env.MOCK_SERVER_FLASK_PORT
            kill_process_on_port(port)
            return ''
