import os


class EnvObject(object):
    @property
    def MOCK_SERVER_FLASK_HOST(self):
        return os.getenv('MOCK_SERVER_FLASK_HOST') or '127.0.0.1'

    @property
    def MOCK_SERVER_FLASK_PORT(self):
        return os.getenv('MOCK_SERVER_FLASK_PORT') or 5012

    @property
    def MOCK_SERVER_FLASK_DATABASE_INITIALIZED(self):
        return os.getenv('MOCK_SERVER_FLASK_DATABASE_INITIALIZED')

    @property
    def MOCK_SERVER_RESOURCES(self):
        return os.getenv('MOCK_SERVER_RESOURCES') or '/app/static/'

    @property
    def MOCK_SERVER_AUTO_IMPORT(self):
        return os.getenv('MOCK_SERVER_AUTO_IMPORT')


Env = EnvObject()
