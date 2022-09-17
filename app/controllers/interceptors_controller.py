from app.adapters.mock_adapter import MockAdapter
from app.core.interceptors.response_interceptor import ResponseInterceptor
from app.models.models.mock_response_interceptor import MockResponseInterceptor
from app.models.models.mock_response_interceptor_type import MockResponseInterceptorType
from app.utils.form_validator import validate_not_empty


# interceptor
def interceptor(mock_id: str, response_id: str, interceptor_id: str) -> MockResponseInterceptor:
    return MockAdapter.get_mock_response_interceptor(mock_id, response_id, interceptor_id)


def interceptor_configuration_example(type: MockResponseInterceptorType) -> str:
    return ResponseInterceptor.example(type)


def interceptor_update(mock_id: str, response_id: str, interceptor_id: str, name: str):
    validate_not_empty(mock_id, 'Mock should be provided')
    validate_not_empty(response_id, 'Mock response should be provided')
    validate_not_empty(interceptor_id, 'Mock response interceptor should be provided')
    MockAdapter.set_mock_response_interceptor(mock_id, response_id, interceptor_id, name)


def interceptor_enable(mock_id: str, response_id: str, interceptor_id: str):
    validate_not_empty(mock_id, 'Mock should be provided')
    validate_not_empty(response_id, 'Mock response should be provided')
    validate_not_empty(interceptor_id, 'Mock response interceptor should be provided')
    MockAdapter.set_mock_response_interceptor_enable(mock_id, response_id, interceptor_id)


def interceptor_disable(mock_id: str, response_id: str, interceptor_id: str):
    validate_not_empty(mock_id, 'Mock should be provided')
    validate_not_empty(response_id, 'Mock response should be provided')
    validate_not_empty(interceptor_id, 'Mock response interceptor should be provided')
    MockAdapter.set_mock_response_interceptor_disable(mock_id, response_id, interceptor_id)


def interceptor_update_configuration(mock_id: str, response_id: str, interceptor_id: str, configuration: str):
    validate_not_empty(mock_id, 'Mock should be provided')
    validate_not_empty(response_id, 'Mock response should be provided')
    validate_not_empty(interceptor_id, 'Mock response interceptor should be provided')
    MockAdapter.set_mock_response_interceptor_configuration(mock_id, response_id, interceptor_id, configuration)
