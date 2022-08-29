from app.adapters.mock_adapter import MockAdapter
from app.config.database_config import db


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

    def __validity_check(self, mock_id: str):
        responses = MockAdapter.get_mock_responses_for_mock(mock_id=mock_id)
        for index, response in enumerate(responses):
            if response.order != index:
                self.__raise_inconsistency_found()

    def __raise_inconsistency_found(self):
        print('Inconsistency found during order calculation')
        raise ValueError('Inconsistency found during order calculation')
