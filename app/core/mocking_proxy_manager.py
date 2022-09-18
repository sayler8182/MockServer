import requests
import validators

from app.adapters.proxy_adapter import ProxyAdapter
from app.core.interceptors.response_interceptor import ResponseInterceptor
from app.core.interceptors.shared_request.request_remove_forwarded_interceptor import RequestRemoveForwardedInterceptor
from app.core.interceptors.shared_request.request_remove_host_interceptor import RequestRemoveHostInterceptor
from app.core.interceptors.shared_request_interceptor import SharedRequestInterceptor
from app.core.interceptors.shared_response.response_headers_interceptor import ResponseHeadersInterceptor
from app.core.interceptors.shared_response.response_remove_headers_duplicates_interceptor import \
    ResponseRemoveHeadersDuplicatesInterceptor
from app.core.interceptors.shared_response.response_remove_response_id_interceptor import \
    ResponseRemoveResponseIdInterceptor
from app.core.interceptors.shared_response.response_settings_headers_interceptor import \
    ResponseSettingsHeadersInterceptor
from app.core.interceptors.shared_response.response_store_log_interceptor import ResponseStoreLogInterceptor
from app.core.interceptors.shared_response_interceptor import SharedResponseInterceptor
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.proxy_request import ProxyRequest
from app.models.models.proxy_response import ProxyResponse, ProxyResponseType
from app.utils.utils_api import response_dumps, response_error


class MockingProxyManager(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app
        self.shared_request_interceptor = SharedRequestInterceptor([
            RequestRemoveHostInterceptor(),
            RequestRemoveForwardedInterceptor()
        ])
        self.shared_response_interceptor = SharedResponseInterceptor([
            ResponseRemoveHeadersDuplicatesInterceptor(),
            ResponseSettingsHeadersInterceptor(),
            ResponseHeadersInterceptor(),
            ResponseRemoveResponseIdInterceptor(),
            ResponseStoreLogInterceptor()
        ])
        self.response_interceptor = ResponseInterceptor()

    def response(self, request, mock: Mock, mock_response: MockResponse, path: str):
        request = self.__prepare_request(request, path)
        if not request:
            return response_error(self.flask_app, 500, 'Incorrect proxy request')
        request = self.shared_request_interceptor.intercept(request, mock, mock_response)
        response = self.__prepare_response(request)
        if not response:
            return response_error(self.flask_app, 500, 'Incorrect proxy response')
        response = self.shared_response_interceptor.intercept(response, mock, mock_response)
        if mock and mock_response:
            response = self.response_interceptor.intercept(response, mock, mock_response)
        return response_dumps(self.flask_app, response)

    def __prepare_request(self, request, path: str) -> ProxyRequest:
        proxy = ProxyAdapter.get_proxy_selected()
        proxy_path = proxy.path or ''
        path = path or ''
        url = proxy_path + path
        if not validators.url(url):
            return None
        return ProxyRequest(method=request.method,
                            url=url,
                            data=request.get_data(),
                            headers=dict(request.headers),
                            json=request.get_json(silent=True))

    def __prepare_response(self, request: ProxyRequest) -> ProxyResponse:
        response = requests.request(method=request.method,
                                    url=request.url,
                                    data=request.data,
                                    headers=request.headers,
                                    json=request.json)
        return ProxyResponse(response=response,
                             type=ProxyResponseType.json,
                             status_code=response.status_code,
                             headers=dict(response.headers),
                             body=response.content)
