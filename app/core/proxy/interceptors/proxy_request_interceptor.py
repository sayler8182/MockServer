from app.core.proxy.models.proxy_request import ProxyRequest
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse


class ProxyRequestInterceptor(object):
    def __init__(self, interceptors):
        self.interceptors = interceptors

    def intercept(self, request: ProxyRequest, mock: Mock, mock_response: MockResponse):
        for interceptor in self.interceptors:
            interceptor.intercept(request, mock, mock_response)
        return request
