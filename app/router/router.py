from app.router.routers.api_router import ApiRouter
from app.router.routers.app_router import AppRouter
from app.router.routers.proxy_router import ProxyRouter


class Router(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app
        self.routers = []

    def init_app(self):
        self.__create_routers()
        self.__init_routers()

    def __create_routers(self):
        self.routers = [
            AppRouter(self.flask_app),
            ApiRouter(self.flask_app),
            ProxyRouter(self.flask_app)
        ]

    def __init_routers(self):
        for router in self.routers:
            router.init_router()
