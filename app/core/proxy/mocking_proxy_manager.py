import requests
import validators

from app.adapters.proxy_adapter import ProxyAdapter
from app.core.proxy.interceptors.proxy_request_interceptor import ProxyRequestInterceptor
from app.core.proxy.interceptors.proxy_response_interceptor import ProxyResponseInterceptor
from app.core.proxy.interceptors.request.proxy_request_remove_forwarded_interceptor import \
    ProxyRequestRemoveForwardedInterceptor
from app.core.proxy.interceptors.request.proxy_request_remove_host_interceptor import ProxyRequestRemoveHostInterceptor
from app.core.proxy.interceptors.response.proxy_response_headers_interceptors import ProxyResponseHeadersInterceptor
from app.core.proxy.interceptors.response.proxy_response_remove_headers_duplicates_interceptor import \
    ProxyResponseRemoveHeadersDuplicatesInterceptor
from app.core.proxy.interceptors.response.proxy_response_remove_response_id_interceptor import \
    ProxyResponseRemoveResponseIdInterceptor
from app.core.proxy.interceptors.response.proxy_response_settings_headers_interceptor import \
    ProxyResponseSettingsHeadersInterceptor
from app.core.proxy.interceptors.response.proxy_response_store_log_interceptor import ProxyResponseStoreLogInterceptor
from app.core.proxy.models.proxy_request import ProxyRequest
from app.core.proxy.models.proxy_response import ProxyResponse, ProxyResponseType
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.utils.utils_api import response_dumps, response_error


class MockingProxyManager(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app
        self.request_interceptor = ProxyRequestInterceptor([
            ProxyRequestRemoveHostInterceptor(),
            ProxyRequestRemoveForwardedInterceptor()
        ])
        self.response_interceptor = ProxyResponseInterceptor([
            ProxyResponseRemoveHeadersDuplicatesInterceptor(),
            ProxyResponseSettingsHeadersInterceptor(),
            ProxyResponseHeadersInterceptor(),
            ProxyResponseRemoveResponseIdInterceptor(),
            ProxyResponseStoreLogInterceptor()
        ])

    def response(self, request, mock: Mock, mock_response: MockResponse, path: str):
        request = self.__prepare_request(request, path)
        if not request:
            return response_error(self.flask_app, 500, 'Incorrect proxy request')
        request = self.request_interceptor.intercept(request, mock, mock_response)
        response = self.__prepare_response(request)
        if not response:
            return response_error(self.flask_app, 500, 'Incorrect proxy response')
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
