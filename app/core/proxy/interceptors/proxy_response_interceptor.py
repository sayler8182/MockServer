from app.core.proxy.models.proxy_response import ProxyResponse
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse


class ProxyResponseInterceptor(object):
    def __init__(self, interceptors):
        self.interceptors = interceptors

    def intercept(self, response: ProxyResponse, mock: Mock, mock_response: MockResponse):
        for interceptor in self.interceptors:
            interceptor.intercept(response, mock, mock_response)
        return response
