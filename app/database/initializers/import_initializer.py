from app.core.import_export.importer_manager import ImporterManager
from app.utils.env import Env


class ImportInitializer(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app
        self.file_path = Env.MOCK_SERVER_AUTO_IMPORT

    def init_initializer(self):
        ImporterManager.import_file_from_path(self.file_path)
