from app.adapters.mock_adapter import MockAdapter
from app.core.proxy.models.proxy_response import ProxyResponse
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse


class ProxyResponseRemoveResponseIdInterceptor(object):
    def intercept(self, response: ProxyResponse, mock: Mock, mock_response: MockResponse) -> ProxyResponse:
        if mock:
            MockAdapter.set_mock_response_unset(mock_id=mock.id)
        return response
