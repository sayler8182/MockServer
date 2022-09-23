from app.adapters.proxy_adapter import ProxyAdapter
from app.core.mocking_file_manager import MockingFileManager
from app.core.mocking_filter import MockingFilter
from app.core.mocking_mock_manager import MockingMockManager
from app.core.mocking_proxy_manager import MockingProxyManager
from app.core.mocking_response_calculator import MockingResponseCalculator
from app.models.models.http_method import HTTPMethod
from app.models.models.mock_response_type import MockResponseType
from app.utils.utils_api import response_error


class MockingManager(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app
        self.mocking_filter = MockingFilter()
        self.response_calculator = MockingResponseCalculator()

    def response(self, request, path: str):
        mock = self.mocking_filter.find(method=HTTPMethod[request.method], path=path)
        mock_response = self.response_calculator.calculate(request, mock)
        if mock and mock_response and mock_response.type == MockResponseType.mock_json:
            manager = MockingMockManager(self.flask_app)
            return manager.response(request, mock, mock_response, path)
        if mock and mock_response and mock_response.type == MockResponseType.mock_file:
            manager = MockingFileManager(self.flask_app)
            return manager.response(request, mock, mock_response, path)
        if not mock or not mock_response or mock_response.type == MockResponseType.proxy:
            proxy = ProxyAdapter.get_proxy_selected()
            if proxy.is_enabled:
                manager = MockingProxyManager(self.flask_app)
                return manager.response(request, mock, mock_response, path)
            return response_error(self.flask_app, 404, 'Proxy is disabled')
        return response_error(self.flask_app, 500, 'Unexpected mocking error')
