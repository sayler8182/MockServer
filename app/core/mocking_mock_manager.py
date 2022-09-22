from app.core.interceptors.response_interceptor import ResponseInterceptor
from app.core.interceptors.shared_response.response_delay_interceptor import ResponseDelayInterceptor
from app.core.interceptors.shared_response.response_headers_interceptor import ResponseHeadersInterceptor
from app.core.interceptors.shared_response.response_remove_response_id_interceptor import \
    ResponseRemoveResponseIdInterceptor
from app.core.interceptors.shared_response.response_settings_headers_interceptor import \
    ResponseSettingsHeadersInterceptor
from app.core.interceptors.shared_response.response_single_use_interceptor import ResponseSingleUseInterceptor
from app.core.interceptors.shared_response.response_store_log_interceptor import ResponseStoreLogInterceptor
from app.core.interceptors.shared_response.response_templating_interceptor import ResponseTemplatingInterceptor
from app.core.interceptors.shared_response_interceptor import SharedResponseInterceptor
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.proxy_response import ProxyResponseType, ProxyResponse
from app.utils.utils_api import response_dumps_string, response_dumps


class MockingMockManager(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app
        self.shared_response_interceptor = SharedResponseInterceptor([
            ResponseSingleUseInterceptor(),
            ResponseDelayInterceptor(),
            ResponseSettingsHeadersInterceptor(),
            ResponseHeadersInterceptor(),
            ResponseTemplatingInterceptor(),
            ResponseRemoveResponseIdInterceptor(),
            ResponseStoreLogInterceptor()
        ])
        self.response_interceptor = ResponseInterceptor()

    def response(self, request, mock: Mock, mock_response: MockResponse, path: str):
        response = self.__prepare_response(mock_response)
        response = self.shared_response_interceptor.intercept(response, mock, mock_response)
        response = self.response_interceptor.intercept(response, mock, mock_response)
        return response_dumps(self.flask_app, response)

    def __prepare_response(self, mock_response: MockResponse) -> ProxyResponse:
        status_code = mock_response.status
        body = mock_response.body
        response = response_dumps_string(self.flask_app, status=status_code, object=body)
        headers = dict(map(lambda item: (item.name, item.value), mock_response.response_headers))
        return ProxyResponse(response=response,
                             type=ProxyResponseType.json,
                             status_code=status_code,
                             headers=headers,
                             body=mock_response.body)
