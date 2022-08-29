from app.config.database_config import db
from app.models.db.database_db import DatabaseDb
from app.models.models.database import Database


class DatabaseAdapter(object):
    @staticmethod
    def get_database() -> Database:
        query = DatabaseDb.query.first()
        return DatabaseAdapter.database_from_entity(query) or Database()

    @staticmethod
    def set_database(is_initiated: bool, commit: bool = True):
        database = DatabaseAdapter.get_database()
        entity = DatabaseAdapter.database_from_object(database)
        entity.is_initiated = is_initiated
        db.session.merge(entity)
        if commit:
            db.session.commit()

    # mappers
    @staticmethod
    def database_from_object(object: Database) -> DatabaseDb:
        if object:
            return DatabaseDb(id='unique',
                              is_initiated=object.is_initiated)
        return None

    @staticmethod
    def database_from_entity(entity: DatabaseDb) -> Database:
        if entity:
            return Database(id='unique',
                            is_initiated=entity.is_initiated)
        return None
