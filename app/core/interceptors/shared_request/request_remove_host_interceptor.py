from app.models.models.proxy_request import ProxyRequest
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse


class RequestRemoveHostInterceptor(object):
    def intercept(self, request: ProxyRequest, mock: Mock, mock_response: MockResponse) -> ProxyRequest:
        request.headers.pop('Host', None)
        return request
