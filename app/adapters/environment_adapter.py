from app.config.database_config import db
from app.models.db.environment_item_db import EnvironmentItemDb
from app.models.models.environment import Environment
from app.models.models.environment_item import EnvironmentItem


class EnvironmentAdapter(object):
    @staticmethod
    def get_environment():
        return Environment(
            dynamic=EnvironmentAdapter.get_environment_items()
        )

    @staticmethod
    def get_environment_items():
        query = EnvironmentItemDb.query.all()
        return list(map(lambda item: EnvironmentAdapter.environment_item_from_entity(item), query))

    @staticmethod
    def get_environment_item(item_id: str):
        query = EnvironmentItemDb.query.filter_by(id=item_id).first()
        return EnvironmentAdapter.environment_item_from_entity(query)

    @staticmethod
    def add_or_set_environment(item: EnvironmentItem, commit: bool = True):
        EnvironmentItemDb.query.filter_by(name=item.name).delete()
        entity = EnvironmentAdapter.environment_item_from_object(item)
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def add_environment(item: EnvironmentItem, commit: bool = True):
        EnvironmentAdapter.add_or_set_environment(item, commit)

    @staticmethod
    def remove_all(commit: bool = True):
        EnvironmentItemDb.query.delete()
        if commit:
            db.session.commit()

    @staticmethod
    def remove_environment(item_id: str, commit: bool = True):
        EnvironmentItemDb.query.filter_by(id=item_id).delete()
        if commit:
            db.session.commit()

    @staticmethod
    def set_environment(item_id: str, name: str, value: str, commit: bool = True):
        item = EnvironmentItem(id=item_id,
                               name=name,
                               value=value)
        EnvironmentAdapter.add_or_set_environment(item, commit)

    # mappers
    @staticmethod
    def environment_item_from_object(object: EnvironmentItem) -> EnvironmentItemDb:
        if object:
            return EnvironmentItemDb(id=object.id,
                                     name=object.name,
                                     value=object.value)
        return None

    @staticmethod
    def environment_item_from_entity(entity: EnvironmentItemDb) -> EnvironmentItem:
        if entity:
            return EnvironmentItem(id=entity.id,
                                   name=entity.name,
                                   value=entity.value)
        return None
