from app.models.models.delay import Delay
from app.models.models.delay_mode import DelayMode
from app.models.models.http_method import HTTPMethod
from app.models.models.mock import MockMethod
from app.models.models.mock_request_rule_type import MockRequestRuleType
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
                 request_supported_rules: [MockRequestRuleType],
                 response_supported_types: [MockResponseType],
                 response_supported_delay_modes: [DelayMode],
                 response_supported_delays: [Delay],
                 response_supported_codes: [StatusCode],
                 response_supported_interceptors: [MockResponseInterceptorType]):
        self.settings = settings
        self.mocks_conflict = mocks_conflict
        self.mock_supported_methods = mock_supported_methods
        self.request_supported_methods = request_supported_methods
        self.request_supported_rules = request_supported_rules
        self.response_supported_types = response_supported_types
        self.response_supported_delay_modes = response_supported_delay_modes
        self.response_supported_delays = response_supported_delays
        self.response_supported_codes = response_supported_codes
        self.response_supported_interceptors = response_supported_interceptors

    def get_dict(self):
        return {
            'settings': self.settings.get_dict(),
            'mocks_conflict': self.mocks_conflict.get_dict(),
            'mock_supported_methods': get_dict(self.mock_supported_methods),
            'request_supported_methods': get_dict(self.request_supported_methods),
            'request_supported_rules': get_dict(self.request_supported_rules),
            'response_supported_types': get_dict(self.response_supported_types),
            'response_supported_delay_modes': get_dict(self.response_supported_delay_modes),
            'response_supported_delays': get_dict(self.response_supported_delays),
            'response_supported_codes': get_dict(self.response_supported_codes),
            'response_supported_interceptors': get_dict(self.response_supported_interceptors),
        }
