from app.models.models.proxy_request import ProxyRequest
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse


class RequestRemoveForwardedInterceptor(object):
    def intercept(self, request: ProxyRequest, mock: Mock, mock_response: MockResponse) -> ProxyRequest:
        request.headers.pop('X-Forwarded-For', None)
        return request
