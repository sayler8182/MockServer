from app.adapters.request_header_adapter import RequestHeaderAdapter
from app.adapters.proxy_adapter import ProxyAdapter
from app.models.models.proxy_request import ProxyRequest
from app.models.models.proxy_response import ProxyResponse
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.request_header import RequestHeaderType


class ResponseSettingsHeadersInterceptor(object):
    def intercept(self, request: ProxyRequest, response: ProxyResponse, mock: Mock,
                  mock_response: MockResponse) -> ProxyResponse:
        proxy = ProxyAdapter.get_proxy_selected()
        headers = RequestHeaderAdapter.get_request_headers_for_proxy(
            proxy.id, RequestHeaderType.proxy_response)
        for header in headers:
            response.headers[header.name] = header.value
        return response
