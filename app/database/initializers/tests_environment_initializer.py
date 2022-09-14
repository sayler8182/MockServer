from app.adapters.mock_adapter import MockAdapter
from app.adapters.proxy_adapter import ProxyAdapter
from app.models.models.http_method import HTTPMethod
from app.models.models.mock import Mock
from app.models.models.mock_request import MockRequest
from app.models.models.mock_response import MockResponse
from app.models.models.proxy import Proxy


class TestEnvironmentInitializer(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app

    def init_initializer(self):
        # proxy
        proxy = Proxy(is_selected=True,
                      is_enabled=True,
                      name='Test environment',
                      path='https://example.com/api')
        ProxyAdapter.add_proxy(proxy)
        # mock
        mock = Mock(
            name='Mock1',
            request=MockRequest(method=HTTPMethod.POST, path='/path1'),
            responses=[
                MockResponse(name='Response1', order=0),
                MockResponse(name='Response2', order=1),
            ])
        MockAdapter.add_mock(mock)
