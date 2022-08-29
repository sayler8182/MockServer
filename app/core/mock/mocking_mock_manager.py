from app.core.mock.interceptors.mock_response_interceptor import MockResponseInterceptor
from app.core.mock.interceptors.response.mock_response_headers_interceptor import MockResponseHeadersInterceptor
from app.core.mock.interceptors.response.mock_response_remove_response_id_interceptor import \
    MockResponseRemoveResponseIdInterceptor
from app.core.mock.interceptors.response.mock_response_settings_headers_interceptor import \
    MockResponseSettingsHeadersInterceptor
from app.core.mock.interceptors.response.mock_response_store_log_interceptor import MockResponseStoreLogInterceptor
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.utils.utils_api import response_dumps_string


class MockingMockManager(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app
        self.response_interceptor = MockResponseInterceptor([
            MockResponseSettingsHeadersInterceptor(),
            MockResponseHeadersInterceptor(),
            MockResponseRemoveResponseIdInterceptor(),
            MockResponseStoreLogInterceptor()
        ])

    def response(self, request, mock: Mock, mock_response: MockResponse, path: str):
        body = mock_response.body
        print("kaboom")
        response = response_dumps_string(self.flask_app, status=mock_response.status, object=body)
        return self.response_interceptor.intercept(response, mock, mock_response)
