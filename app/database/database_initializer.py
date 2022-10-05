from app.adapters.database_adapter import DatabaseAdapter
from app.database.initializers.import_initializer import ImportInitializer
from app.database.initializers.settings_proxy_initializer import SettingsProxyInitializer


class DatabaseInitializer:
    def __init__(self, flask_app):
        self.flask_app = flask_app
        self.initializers = []

    def init_app(self):
        database = DatabaseAdapter.get_database()
        if not database.is_initiated:
            self.__create_initializers()
            self.__init_initializers()
            self.__finish_initializers()

    def __create_initializers(self):
        self.initializers = [
            ImportInitializer(self.flask_app),
            SettingsProxyInitializer(self.flask_app),
        ]

    def __init_initializers(self):
        for initializer in self.initializers:
            initializer.init_initializer()

    def __finish_initializers(self):
        DatabaseAdapter.set_database(True)
