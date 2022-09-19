import os


class EnvObject(object):
    @property
    def MOCK_SERVER_FLASK_HOST(self):
        return os.getenv('MOCK_SERVER_FLASK_HOST')

    @property
    def MOCK_SERVER_FLASK_PORT(self):
        return os.getenv('MOCK_SERVER_FLASK_PORT')

    @property
    def MOCK_SERVER_FLASK_DATABASE_INITIALIZED(self):
        return os.getenv('MOCK_SERVER_FLASK_DATABASE_INITIALIZED')


Env = EnvObject()
