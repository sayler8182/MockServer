from app.adapters.mock_adapter import MockAdapter
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.proxy_request import ProxyRequest
from app.models.models.proxy_response import ProxyResponse


class ResponseSingleUseInterceptor(object):
    def intercept(self, request: ProxyRequest, response: ProxyResponse, mock: Mock, mock_response: MockResponse) -> ProxyResponse:
        if mock and mock_response and mock_response.is_single_use:
            MockAdapter.set_mock_response_disable(mock.id, mock_response.id)
            MockAdapter.set_mock_response_not_single_use(mock.id, mock_response.id)
        return response
