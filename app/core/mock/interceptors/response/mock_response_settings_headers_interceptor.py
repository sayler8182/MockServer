from app.adapters.request_header_adapter import RequestHeaderAdapter
from app.adapters.settings_proxy_adapter import SettingsProxyAdapter
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.request_header import RequestHeaderType


class MockResponseSettingsHeadersInterceptor(object):
    def intercept(self, response, mock: Mock, mock_response: MockResponse):
        proxy = SettingsProxyAdapter.get_selected_proxy()
        headers = RequestHeaderAdapter.get_request_headers_for_proxy(proxy.id, RequestHeaderType.settings_response)
        for header in headers:
            response.headers[header.name] = header.value
        return response
