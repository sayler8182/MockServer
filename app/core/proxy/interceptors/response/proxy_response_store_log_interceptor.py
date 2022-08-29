from app.adapters.mock_response_log_adapter import MockResponseLogAdapter
from app.core.proxy.models.proxy_response import ProxyResponse
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.mock_response_log import MockResponseLog


class ProxyResponseStoreLogInterceptor(object):
    def intercept(self, response: ProxyResponse, mock: Mock, mock_response: MockResponse) -> ProxyResponse:
        if mock and mock_response:
            log = MockResponseLog(mock_id=mock.id,
                                  response_id=mock_response.id)
            MockResponseLogAdapter.add_log(log)
        return response
