from app.models.models.http_method import HTTPMethod
from app.models.models.mock import MockMethod
from app.models.models.mock_response_interceptor_type import MockResponseInterceptorType
from app.models.models.mock_response_type import MockResponseType
from app.models.models.settings import Settings
from app.models.models.status_code import StatusCode
from app.utils.utils import get_dict


class MocksConfiguration(object):
    def __init__(self,
                 settings: Settings,
                 mocks_conflict: [str],
                 mock_supported_methods: [MockMethod],
                 request_supported_methods: [HTTPMethod],
                 response_supported_types: [MockResponseType],
                 response_supported_codes: [StatusCode],
                 response_supported_interceptors: [MockResponseInterceptorType]):
        self.settings = settings
        self.mocks_conflict = mocks_conflict
        self.mock_supported_methods = mock_supported_methods
        self.request_supported_methods = request_supported_methods
        self.response_supported_types = response_supported_types
        self.response_supported_codes = response_supported_codes
        self.response_supported_interceptors = response_supported_interceptors

    def get_dict(self):
        return {
            'settings': self.settings.get_dict(),
            'mocks_conflict': self.mocks_conflict.get_dict(),
            'mock_supported_methods': get_dict(self.mock_supported_methods),
            'request_supported_methods': get_dict(self.request_supported_methods),
            'response_supported_types': get_dict(self.response_supported_types),
            'response_supported_codes': get_dict(self.response_supported_codes),
            'response_supported_interceptors': get_dict(self.response_supported_interceptors),
        }
