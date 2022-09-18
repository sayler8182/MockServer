import json
from os.path import exists

from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.mock_response_interceptor import MockResponseInterceptor


class ResponseCustomInterceptor(object):
    def intercept(self, response, mock: Mock, mock_response: MockResponse, interceptor: MockResponseInterceptor):
        configuration = json.loads(interceptor.configuration)
        file_path = configuration.get('file_path', None)
        if file_path and exists(file_path):
            with open(file_path, "r") as file:
                code = file.read()
                params = {
                    'response': response,
                    'mock': mock,
                    'mock_response': mock_response,
                    'interceptor': interceptor
                }
                exec(code, params)
        return response

    @staticmethod
    def example() -> any:
        return {
            "file_path": "required string - absolute path to interceptor"
        }
