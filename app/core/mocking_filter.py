from app.adapters.mock_adapter import MockAdapter
from app.core.path_matcher import PathMatcher
from app.models.models.http_method import HTTPMethod
from app.models.models.mock import Mock
from app.models.models.mock_request_rule import MockRequestRule
from app.models.models.mock_request_rule_type import MockRequestRuleType
from app.utils.path_components import PathComponents
from app.utils.utils import first, safe_call_with_result


class MockingFilter(object):
    def find(self, request, method: HTTPMethod, path: str) -> Mock:
        mocks = MockAdapter.get_mocks()
        mocks = list(filter(self.__mock_filter(request, method, path), mocks))
        return first(mocks)

    def __mock_filter(self, request, method: HTTPMethod, path: str):
        return lambda mock: self.__match_is_enabled(mock, request) \
                            and self.__match_method(mock, request, method) \
                            and self.__match_path(mock, request, path) \
                            and self.__match_rules(mock, request)

    def __match_is_enabled(self, mock: Mock, request) -> bool:
        return mock.is_enabled

    def __match_method(self, mock: Mock, request, method: HTTPMethod) -> bool:
        return mock.request.method == method

    def __match_path(self, mock: Mock, request, path: str) -> bool:
        if not mock.request.path:
            return False
        pattern = PathComponents(mock.request.path)
        matcher = PathMatcher(pattern, path)
        result = matcher.match()
        return result.match

    def __match_rules(self, mock: Mock, request) -> bool:
        rules = mock.request.rules or []
        for rule in rules:
            match = self.__match_rule(rule, request)
            if not match:
                return False
        return True

    def __match_rule(self, rule: MockRequestRule, request) -> bool:
        action = {
            MockRequestRuleType.match_header: lambda: self.__match_rule_match_header(rule, request),
            MockRequestRuleType.match_parameter: lambda: self.__match_rule_match_parameter(rule, request),
        }.get(rule.type)
        return safe_call_with_result(action)

    def __match_rule_match_header(self, rule: MockRequestRule, request) -> bool:
        if request.headers:
            for key, value in request.headers:
                if rule.key == key and (rule.value == value or rule.value == '*'):
                    return True
        return False

    def __match_rule_match_parameter(self, rule: MockRequestRule, request) -> bool:
        if request.args:
            args = request.args.to_dict(flat=False)
            for key, value in args.items():
                values = value if isinstance(value, list) else [value]
                for value in values:
                    if rule.key == key and (rule.value == value or rule.value == '*'):
                        return True
        return False
