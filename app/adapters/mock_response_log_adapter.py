from app.config.database_config import db
from app.models.db.mock_response_log_db import MockResponseLogDb
from app.models.models.mock_response_log import MockResponseLog, MockResponseLogData, MockResponseLogDataRequest


class MockResponseLogAdapter(object):
    @staticmethod
    def get_logs() -> [MockResponseLog]:
        query = MockResponseLogDb.query.order_by(MockResponseLogDb.date.desc()).all()
        return list(map(lambda item: MockResponseLogAdapter.log_from_entity(item), query))

    @staticmethod
    def get_logs_for_mock(mock_id: str) -> [MockResponseLog]:
        query = MockResponseLogDb.query.filter_by(mock_id=mock_id).order_by(MockResponseLogDb.date.desc()).all()
        return list(map(lambda item: MockResponseLogAdapter.log_from_entity(item), query))

    @staticmethod
    def get_log(log_id: str) -> [MockResponseLog]:
        query = MockResponseLogDb.query.filter_by(id=log_id).first()
        return MockResponseLogAdapter.log_from_entity(query)

    @staticmethod
    def add_log(log: MockResponseLog, commit: bool = True):
        entity = MockResponseLogAdapter.log_from_object(log)
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def remove_logs(commit: bool = True):
        MockResponseLogDb.query.delete()
        if commit:
            db.session.commit()

    @staticmethod
    def remove_logs_for_mock(mock_id: str, commit: bool = True):
        MockResponseLogDb.query.filter_by(mock_id=mock_id).delete()
        if commit:
            db.session.commit()

    @staticmethod
    def remove_log(log_id: str, commit: bool = True):
        MockResponseLogDb.query.filter_by(id=log_id).delete()
        if commit:
            db.session.commit()

    # mappers
    @staticmethod
    def log_from_object(object: MockResponseLog) -> MockResponseLogDb:
        if object:
            data_request = MockResponseLogDataRequest.encode(object.data_request)
            data = MockResponseLogData.encode(object.data)
            return MockResponseLogDb(id=object.id,
                                     mock_id=object.mock_id,
                                     response_id=object.response_id,
                                     date=object.date,
                                     data_request=data_request,
                                     data=data)
        return None

    @staticmethod
    def log_from_entity(entity: MockResponseLogDb) -> MockResponseLog:
        if entity:
            return MockResponseLog(id=entity.id,
                                   mock_id=entity.mock_id,
                                   response_id=entity.response_id,
                                   date=entity.date,
                                   data_request=entity.data_request,
                                   data=entity.data)
        return None
