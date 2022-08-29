from app.adapters.mock_adapter import MockAdapter
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse


class MockResponseRemoveResponseIdInterceptor(object):
    def intercept(self, response, mock: Mock, mock_response: MockResponse):
        if mock:
            MockAdapter.set_mock_response_unset(mock_id=mock.id)
        return response
