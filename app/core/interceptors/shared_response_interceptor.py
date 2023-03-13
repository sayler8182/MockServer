from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.proxy_request import ProxyRequest
from app.models.models.proxy_response import ProxyResponse


class SharedResponseInterceptor(object):
    def __init__(self, interceptors):
        self.interceptors = interceptors

    def intercept(self, request: ProxyRequest, response: ProxyResponse, mock: Mock, mock_response: MockResponse):
        for interceptor in self.interceptors:
            interceptor.intercept(request, response, mock, mock_response)
        return response
