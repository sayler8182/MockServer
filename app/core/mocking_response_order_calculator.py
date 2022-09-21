from app.adapters.mock_adapter import MockAdapter
from app.config.database_config import db
from app.models.models.mock_response import MockResponse
from app.utils.utils import first


class MockingResponseOrderCalculator(object):
    def order_for_new_response(self, mock_id: str) -> int:
        responses = MockAdapter.get_mock_responses_for_mock(mock_id=mock_id)
        order = len(responses)
        self.__validity_check(mock_id)
        return order

    def adjust_order_for_mock(self, mock_id: str):
        responses = MockAdapter.get_mock_responses_for_mock(mock_id=mock_id)
        for index, response in enumerate(responses):
            MockAdapter.set_mock_response_order(mock_id, response.id, index)
        db.session.commit()
        self.__validity_check(mock_id)

    def adjust_order_for_mock_keep_response(self, mock_id: str, response_id: str):
        lock_response = MockAdapter.get_mock_response(mock_id=mock_id, id=response_id)
        responses = MockAdapter.get_mock_responses_for_mock(mock_id=mock_id)
        filtered_responses = list(filter(lambda item: item.id != response_id, responses))
        for index, response in enumerate(responses):
            match = self.__find_for_index(index, filtered_responses, lock_response)
            filtered_responses = list(filter(lambda item: item.id != match.id, filtered_responses))
            MockAdapter.set_mock_response_order(mock_id, match.id, index)
        db.session.commit()
        self.__validity_check(mock_id)

    def __find_for_index(self, index: int, responses: [MockResponse], lock_response: MockResponse) -> MockResponse:
        if index == lock_response.order:
            return lock_response
        return first(responses)

    def __validity_check(self, mock_id: str):
        responses = MockAdapter.get_mock_responses_for_mock(mock_id=mock_id)
        for index, response in enumerate(responses):
            if response.order != index:
                self.__raise_inconsistency_found()

    def __raise_inconsistency_found(self):
        print('Inconsistency found during order calculation')
        raise ValueError('Inconsistency found during order calculation')
