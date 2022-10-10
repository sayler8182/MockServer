from flasgger import Swagger

from app.utils.env import Env

swagger: Swagger = None


class SwaggerConfig(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app

        self.author = "Konrad Piękoś"
        self.host = Env.MOCK_SERVER_FLASK_HOST
        self.port = Env.MOCK_SERVER_FLASK_PORT

    def init_app(self):
        global swagger
        template = self.__get_template()
        swagger = Swagger(self.flask_app, template=template)

    def __get_template(self):
        return {
            "swagger": "2.0",
            "info": {
                "title": "MockServer",
                "description": "API for MockServer",
                "contact": {
                    "responsibleOrganization": f"{self.author}",
                    "responsibleDeveloper": f"{self.author}",
                    "email": "konradpiekos93@gmail.com",
                    "url": "https://www.github.com/sayler8182",
                },
                "version": "0.0.0"
            },
            "host": f"{self.host}:{self.port}",
            "basePath": "/api",
            "schemes": [
                "http",
                "https"
            ]
        }
