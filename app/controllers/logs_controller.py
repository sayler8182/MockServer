from app.adapters.mock_adapter import MockAdapter
from app.adapters.mock_response_log_adapter import MockResponseLogAdapter
from app.models.models.mock import Mock
from app.models.models.mock_response_log import MockResponseLog


# mock
def mock(mock_id: str) -> Mock:
    return MockAdapter.get_mock(mock_id)


# logs
def logs() -> [MockResponseLog]:
    return MockResponseLogAdapter.get_logs()


def logs_for_mock(mock_id: str) -> [MockResponseLog]:
    return MockResponseLogAdapter.get_logs_for_mock(mock_id)


def log(log_id: str) -> MockResponseLog:
    return MockResponseLogAdapter.get_log(log_id)


def logs_remove_all(mock_id: str):
    if mock_id:
        MockResponseLogAdapter.remove_logs_for_mock(mock_id)
    else:
        MockResponseLogAdapter.remove_logs()


def log_remove(mock_id: str, log_id: str):
    MockResponseLogAdapter.remove_log(log_id)
