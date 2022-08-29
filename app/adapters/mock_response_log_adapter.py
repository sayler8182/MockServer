from app.config.database_config import db
from app.models.db.mock_response_log_db import MockResponseLogDb
from app.models.models.mock_response_log import MockResponseLog


class MockResponseLogAdapter(object):
    @staticmethod
    def get_logs(mock_id: str) -> [MockResponseLog]:
        query = MockResponseLogDb.query.filter_by(mock_id=mock_id).order_by(MockResponseLogDb.date.desc()).all()
        return list(map(lambda item: MockResponseLogAdapter.log_from_entity(item), query))

    @staticmethod
    def add_log(log: MockResponseLog, commit: bool = True):
        entity = MockResponseLogAdapter.log_from_object(log)
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def remove_logs(mock_id: str, commit: bool = True) -> [MockResponseLog]:
        MockResponseLogDb.query.filter_by(mock_id=mock_id).delete()
        if commit:
            db.session.commit()

    # mappers
    @staticmethod
    def log_from_object(object: MockResponseLog) -> MockResponseLogDb:
        if object:
            return MockResponseLogDb(id=object.id,
                                     mock_id=object.mock_id,
                                     response_id=object.response_id,
                                     date=object.date)
        return None

    @staticmethod
    def log_from_entity(entity: MockResponseLogDb) -> MockResponseLog:
        if entity:
            return MockResponseLog(id=entity.id,
                                   mock_id=entity.mock_id,
                                   response_id=entity.response_id,
                                   date=entity.date)
        return None
