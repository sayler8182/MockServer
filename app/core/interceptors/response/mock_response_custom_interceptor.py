from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.mock_response_interceptor import MockResponseInterceptor


class MockResponseCustomInterceptor(object):
    def intercept(self, response, mock: Mock, mock_response: MockResponse, interceptor: MockResponseInterceptor):
        return response

    @staticmethod
    def example() -> any:
        return {
            "file_path": "required string - absolute path to interceptor"
        }
