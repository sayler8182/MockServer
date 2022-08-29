from app.core.proxy.models.proxy_response import ProxyResponse
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse


class ProxyResponseRemoveHeadersDuplicatesInterceptor(object):
    def intercept(self, response: ProxyResponse, mock: Mock, mock_response: MockResponse) -> ProxyResponse:
        response.headers.pop('Server', None)
        response.headers.pop('Date', None)
        response.headers.pop('Transfer-Encoding', None)
        response.headers.pop('Connection', None)
        return response
