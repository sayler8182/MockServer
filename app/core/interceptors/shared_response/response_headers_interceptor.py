from app.adapters.request_header_adapter import RequestHeaderAdapter
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.proxy_response import ProxyResponse
from app.models.models.request_header import RequestHeaderType


class ResponseHeadersInterceptor(object):
    def intercept(self, response: ProxyResponse, mock: Mock, mock_response: MockResponse) -> ProxyResponse:
        if mock and mock_response:
            headers = RequestHeaderAdapter.get_request_headers_for_mock_response(mock.id, mock_response.id,
                                                                                 RequestHeaderType.mock_response)
            for header in headers:
                response.headers[header.name] = header.value
        return response
