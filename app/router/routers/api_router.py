from app.router.routers.api.mocks_router import MocksRouter
from app.router.routers.api.settings_router import SettingsRouter


class ApiRouter(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app

    def init_router(self):
        self.__create_routers()
        self.__init_routers()

    def __create_routers(self):
        self.routers = [
            MocksRouter(self.flask_app),
            SettingsRouter(self.flask_app)
        ]

    def __init_routers(self):
        for router in self.routers:
            router.init_router()
