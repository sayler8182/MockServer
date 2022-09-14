from app.adapters.request_header_adapter import RequestHeaderAdapter
from app.adapters.proxy_adapter import ProxyAdapter
from app.core.proxy.models.proxy_response import ProxyResponse
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.request_header import RequestHeaderType


class ProxyResponseSettingsHeadersInterceptor(object):
    def intercept(self, response: ProxyResponse, mock: Mock, mock_response: MockResponse) -> ProxyResponse:
        proxy = ProxyAdapter.get_proxy_selected()
        headers = RequestHeaderAdapter.get_request_headers_for_proxy(
            proxy.id, RequestHeaderType.proxy_response)
        for header in headers:
            response.headers[header.name] = header.value
        return response
