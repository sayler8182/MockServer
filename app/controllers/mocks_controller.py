from flask import request

from app.adapters.mock_adapter import MockAdapter
from app.adapters.request_header_adapter import RequestHeaderAdapter
from app.adapters.settings_adapter import SettingsAdapter
from app.core.import_export.exporter_manager import ExporterManager
from app.core.import_export.importer_manager import ImporterManager
from app.core.mocking_response_calculator import MockingResponseCalculator
from app.core.mocking_response_order_calculator import MockingResponseOrderCalculator
from app.models.models.http_method import HTTPMethod
from app.models.models.mock import Mock, MockMethod
from app.models.models.mock_response import MockResponse, MockResponseType
from app.models.models.mocks_configuration import MocksConfiguration
from app.models.models.request_header import RequestHeader, RequestHeaderType
from app.models.models.status_code import StatusCode
from app.utils.form_validator import validate_not_empty
from app.utils.utils import to_int

order_calculator = MockingResponseOrderCalculator()


# configuration
def configuration() -> MocksConfiguration:
    return MocksConfiguration(
        settings=SettingsAdapter.get_settings(),
        mock_supported_methods=MockMethod.supported_methods(),
        request_supported_methods=HTTPMethod.supported_methods(),
        response_supported_types=MockResponseType.supported_types(),
        response_supported_codes=StatusCode.supported_codes(),
    )


# mock
def mocks() -> [Mock]:
    return MockAdapter.get_mocks()


def mock(mock_id: str) -> Mock:
    return MockAdapter.get_mock(mock_id)


def mock_response_next(mock_id: str) -> str:
    mock = MockAdapter.get_mock(mock_id)
    calculator = MockingResponseCalculator()
    return calculator.calculate(request, mock)


def mock_new() -> Mock:
    new_mock = Mock()
    MockAdapter.add_mock(new_mock)
    return new_mock


def mock_import_mocks(file):
    validate_not_empty(file, 'File should be provided')
    return ImporterManager.import_file(file)


def mock_export_mocks():
    return ExporterManager.export_mocks()


def mock_remove_all():
    return MockAdapter.remove_all()


def mock_remove(mock_id: str):
    validate_not_empty(mock_id, 'Mock should be provided')
    MockAdapter.remove_mock(mock_id)


def mock_export_mock(mock_id: str):
    validate_not_empty(mock_id, 'Mock should be provided')
    return ExporterManager.export_mock(mock_id)


def mock_enable(mock_id: str):
    validate_not_empty(mock_id, 'Mock should be provided')
    MockAdapter.set_mock_enable(mock_id)


def mock_disable(mock_id: str):
    validate_not_empty(mock_id, 'Mock should be provided')
    MockAdapter.set_mock_disable(mock_id)


def mock_update(mock_id: str, name: str):
    validate_not_empty(mock_id, 'Mock should be provided')
    MockAdapter.set_mock(mock_id, name)


# mock request
def mock_request_update(mock_id: str, method: str, path: str):
    http_method = HTTPMethod[method]
    validate_not_empty(mock_id, 'Mock should be provided')
    validate_not_empty(http_method, 'Correct HTTPMethod should be provided')
    validate_not_empty(path, 'Path should be empty')
    MockAdapter.set_mock_request(mock_id, http_method, path)


# mock response
def mock_method_update(mock_id: str, method: str):
    mock_method = MockMethod[method]
    validate_not_empty(mock_id, 'Mock should be provided')
    MockAdapter.set_mock_method(mock_id, mock_method)


def mock_response(mock_id: str, response_id: str) -> MockResponse:
    validate_not_empty(mock_id, 'Mock should be provided')
    validate_not_empty(mock_id, 'Mock response should be provided')
    return MockAdapter.get_mock_response(mock_id, response_id)


def mock_response_new(mock_id: str) -> MockResponse:
    validate_not_empty(mock_id, 'Mock should be provided')
    order = order_calculator.order_for_new_response(mock_id)
    new_mock_response = MockResponse(mock_id=mock_id, order=order)
    MockAdapter.add_mock_response(new_mock_response)
    return new_mock_response


def mock_response_remove(mock_id: str, response_id: str):
    validate_not_empty(mock_id, 'Mock should be provided')
    validate_not_empty(response_id, 'Mock response should be provided')
    MockAdapter.remove_mock_response(mock_id, response_id)
    order_calculator.adjust_order_for_mock(mock_id)


def mock_response_enable(mock_id: str, response_id: str):
    validate_not_empty(mock_id, 'Mock should be provided')
    validate_not_empty(response_id, 'Mock response should be provided')
    MockAdapter.set_mock_response_enable(mock_id, response_id)


def mock_response_disable(mock_id: str, response_id: str):
    validate_not_empty(mock_id, 'Mock should be provided')
    validate_not_empty(response_id, 'Mock response should be provided')
    MockAdapter.set_mock_response_disable(mock_id, response_id)


def mock_response_set(mock_id: str, response_id: str):
    validate_not_empty(mock_id, 'Mock should be provided')
    validate_not_empty(response_id, 'Mock response should be provided')
    MockAdapter.set_mock_response_set(mock_id, response_id)


def mock_response_unset(mock_id: str, response_id: str):
    validate_not_empty(mock_id, 'Mock should be provided')
    validate_not_empty(response_id, 'Mock response should be provided')
    MockAdapter.set_mock_response_unset(mock_id)


def mock_response_update(mock_id: str, response_id: str, name: str):
    validate_not_empty(mock_id, 'Mock should be provided')
    validate_not_empty(response_id, 'Mock response should be provided')
    MockAdapter.set_mock_response(mock_id, response_id, name)


# mock response type
def mock_response_update_type(mock_id: str, response_id: str, type: str):
    type = MockResponseType[type]
    validate_not_empty(mock_id, 'Mock should be provided')
    validate_not_empty(response_id, 'Mock response should be provided')
    validate_not_empty(type, 'Type should be provided')
    MockAdapter.set_mock_response_type(mock_id, response_id, type)


# mock response status
def mock_response_update_status(mock_id: str, response_id: str, status: str):
    status = to_int(status)
    validate_not_empty(mock_id, 'Mock should be provided')
    validate_not_empty(response_id, 'Mock response should be provided')
    validate_not_empty(status, 'Status should be provided')
    MockAdapter.set_mock_response_status(mock_id, response_id, status)


# mock response headers


def mock_response_headers_remove(mock_id: str, response_id: str, header_id: str):
    validate_not_empty(mock_id, 'Mock should be provided')
    validate_not_empty(response_id, 'Mock response should be provided')
    validate_not_empty(header_id, 'Mock response header should be provided')
    RequestHeaderAdapter.remove_request_header(header_id)


def mock_response_headers_new(mock_id: str, response_id: str, name: str, value: str):
    validate_not_empty(mock_id, 'Mock should be provided')
    validate_not_empty(response_id, 'Mock response should be provided')
    validate_not_empty(name, 'Name should not be empty')
    validate_not_empty(value, 'Value should not be empty')
    header = RequestHeader(type=RequestHeaderType.mock_response,
                           mock_id=mock_id,
                           response_id=response_id,
                           name=name,
                           value=value)
    RequestHeaderAdapter.add_request_header(header)
    return header


# mock response body
def mock_response_update_body(mock_id: str, response_id: str, body: str):
    validate_not_empty(mock_id, 'Mock should be provided')
    validate_not_empty(response_id, 'Mock response should be provided')
    MockAdapter.set_mock_response_body(mock_id, response_id, body)