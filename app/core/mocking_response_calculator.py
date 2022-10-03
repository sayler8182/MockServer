from app.adapters.mock_response_log_adapter import MockResponseLogAdapter
from app.models.models.mock import Mock, MockMethod
from app.models.models.mock_response import MockResponse
from app.utils.utils import first, last


class MockingResponseCalculator(object):
    def calculate(self, request, mock: Mock) -> MockResponse:
        if mock:
            default = self.__default_response(mock)
            if default is None:
                return None
            elif mock.response_id:
                return self.__calculate_static(request, mock) or default
            elif mock.method == MockMethod.random:
                return self.__calculate_random(request, mock) or default
            elif mock.method == MockMethod.rotate:
                return self.__calculate_rotate(request, mock) or default
            elif mock.method == MockMethod.sequential:
                return self.__calculate_sequential(request, mock) or default
            else:
                return default
        return None

    def __default_response(self, mock: Mock):
        return first(list(filter(lambda item: item.is_enabled, mock.responses)))

    def __calculate_static(self, request, mock: Mock) -> MockResponse:
        return first(list(filter(lambda item: item.is_enabled and item.id == mock.response_id, mock.responses)))

    def __calculate_random(self, request, mock: Mock) -> MockResponse:
        return first(mock.responses)

    def __calculate_rotate(self, request, mock: Mock) -> MockResponse:
        responses = self.__responses_for_mock(mock)
        responses_history = self.__responses_history(mock, responses)
        last_response = first(responses_history)
        if last_response:
            return self.__next_response_for_order(responses, last_response.order) or first(responses)
        return None

    def __calculate_sequential(self, request, mock: Mock) -> MockResponse:
        responses = self.__responses_for_mock(mock)
        responses_history = self.__responses_history(mock, responses)
        last_response = first(responses_history)
        if last_response:
            return self.__next_response_for_order(responses, last_response.order) or last(responses)
        return None

    def __next_response_for_order(self, responses: [MockResponse], order: int) -> MockResponse:
        next_order = None
        for response in responses:
            if response.order > order:
                next_order = response.order
                break
        if next_order:
            return self.__response_for_order(responses, next_order)
        return None

    def __response_for_order(self, responses: [MockResponse], order: int) -> MockResponse:
        return first(list(filter(lambda item: item.order == order, responses)))

    def __responses_for_mock(self, mock: Mock) -> [MockResponse]:
        return list(filter(lambda item: item.is_enabled, mock.responses))

    def __responses_history(self, mock: Mock, responses: [MockResponse]) -> [MockResponse]:
        responses_history = []
        logs = MockResponseLogAdapter.get_logs_for_mock(mock_id=mock.id)
        for log in logs:
            response = first(list(filter(lambda item: item.id == log.response_id, responses)))
            if response:
                responses_history.append(response)
        return responses_history
