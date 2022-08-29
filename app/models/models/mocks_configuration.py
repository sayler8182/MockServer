from app.models.models.http_method import HTTPMethod
from app.models.models.mock import MockMethod
from app.models.models.mock_response import MockResponseType
from app.models.models.settings import Settings
from app.models.models.status_code import StatusCode
from app.utils.utils import get_dict


class MocksConfiguration(object):
    def __init__(self,
                 settings: Settings,
                 mock_supported_methods: [MockMethod],
                 request_supported_methods: [HTTPMethod],
                 response_supported_types: [MockResponseType],
                 response_supported_codes: [StatusCode]):
        self.settings = settings
        self.mock_supported_methods = mock_supported_methods
        self.request_supported_methods = request_supported_methods
        self.response_supported_types = response_supported_types
        self.response_supported_codes = response_supported_codes

    def get_dict(self):
        return {
            'settings': self.settings.get_dict(),
            'mock_supported_methods': get_dict(self.mock_supported_methods),
            'request_supported_methods': get_dict(self.request_supported_methods),
            'response_supported_types': get_dict(self.response_supported_types),
            'response_supported_codes': get_dict(self.response_supported_codes),
        }
