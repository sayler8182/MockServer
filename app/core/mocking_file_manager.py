import os
from os.path import exists

from flask import send_file, abort

from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.utils.env import Env


class MockingFileManager(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app

    def response(self, request, mock: Mock, mock_response: MockResponse, path: str):
        if mock_response.body_path:
            # absolute
            return_path = mock_response.body_path
            if exists(return_path):
                return send_file(return_path)

            # relative
            root_directory = os.getcwd()
            resources = Env.MOCK_SERVER_RESOURCES
            return_path = f'{root_directory}{resources}{mock_response.body_path}'
            if exists(return_path):
                return send_file(return_path)
        return abort(404)
