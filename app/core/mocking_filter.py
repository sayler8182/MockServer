from app.adapters.mock_adapter import MockAdapter
from app.core.path_matcher import PathMatcher
from app.models.models.http_method import HTTPMethod
from app.models.models.mock import Mock
from app.utils.path_components import PathComponents
from app.utils.utils import first


class MockingFilter(object):
    def find(self, method: HTTPMethod, path: str) -> Mock:
        mocks = MockAdapter.get_mocks()
        mocks = list(filter(self.__mock_filter(method, path), mocks))
        return first(mocks)

    def __mock_filter(self, method: HTTPMethod, path: str):
        return lambda mock: self.__match_is_enabled(mock) \
                            and self.__match_method(mock, method) \
                            and self.__match_path(mock, path)

    def __match_is_enabled(self, mock: Mock):
        return mock.is_enabled

    def __match_method(self, mock: Mock, method: HTTPMethod):
        return mock.request.method == method

    def __match_path(self, mock: Mock, path: str):
        pattern = PathComponents(mock.request.path)
        matcher = PathMatcher(pattern, path)
        result = matcher.match()
        return result.match
