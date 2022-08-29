from app.config.database_config import db
from app.models.db.request_header_db import RequestHeaderDb
from app.models.db.settings_proxy_db import SettingsProxyDb
from app.models.models.delay_mode import DelayMode
from app.models.models.settings_proxy import SettingsProxy


class SettingsProxyAdapter(object):
    @staticmethod
    def get_proxies() -> [SettingsProxy]:
        query = SettingsProxyDb.query.all()
        return list(map(lambda item: SettingsProxyAdapter.settings_proxy_from_entity(item), query))

    @staticmethod
    def get_selected_proxy() -> SettingsProxy:
        query = SettingsProxyDb.query.filter_by(is_selected=True).first()
        return SettingsProxyAdapter.settings_proxy_from_entity(query)

    @staticmethod
    def get_proxy(proxy_id: str) -> SettingsProxy:
        query = SettingsProxyDb.query.filter_by(id=proxy_id).first()
        return SettingsProxyAdapter.settings_proxy_from_entity(query)

    @staticmethod
    def add_proxy(proxy: SettingsProxy, commit: bool = True):
        entity = SettingsProxyAdapter.settings_proxy_from_object(proxy)
        db.session.merge(entity)
        SettingsProxyAdapter.set_proxy_select(entity.id, entity.is_selected, False)
        if commit:
            db.session.commit()

    @staticmethod
    def set_proxy_select(proxy_id: str, is_selected: bool, commit: bool = True):
        proxies = SettingsProxyAdapter.get_proxies()
        for proxy in proxies:
            proxy = SettingsProxyAdapter.get_proxy(proxy_id=proxy.id)
            entity = SettingsProxyAdapter.settings_proxy_from_object(proxy)
            entity.is_selected = False
            db.session.merge(entity)
        proxy = SettingsProxyAdapter.get_proxy(proxy_id=proxy_id) if is_selected else proxies[0]
        entity = SettingsProxyAdapter.settings_proxy_from_object(proxy)
        entity.is_selected = True
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_proxy_enable(proxy_id: str, is_enabled: bool, commit: bool = True):
        proxy = SettingsProxyAdapter.get_proxy(proxy_id=proxy_id)
        entity = SettingsProxyAdapter.settings_proxy_from_object(proxy)
        entity.is_enabled = is_enabled
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_proxy_name_and_path(proxy_id: str, name: str, path: str, commit: bool = True):
        proxy = SettingsProxyAdapter.get_proxy(proxy_id=proxy_id)
        entity = SettingsProxyAdapter.settings_proxy_from_object(proxy)
        entity.name = name
        entity.path = path
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def remove_proxy(proxy_id: str, commit: bool = True):
        proxies = SettingsProxyDb.query.all()
        RequestHeaderDb.query.filter_by(proxy_id=proxy_id).delete()
        if len(proxies) > 1:
            SettingsProxyDb.query.filter_by(id=proxy_id).delete()
            if commit:
                db.session.commit()

    # mappers
    @staticmethod
    def settings_proxy_from_object(object: SettingsProxy) -> SettingsProxyDb:
        if object:
            return SettingsProxyDb(id=object.id,
                                   is_selected=object.is_selected,
                                   is_enabled=object.is_enabled,
                                   name=object.name,
                                   path=object.path,
                                   delay_mode=object.delay_mode.value,
                                   delay_from=object.delay_from,
                                   delay_to=object.delay_to,
                                   delay=object.delay)
        return None

    @staticmethod
    def settings_proxy_from_entity(entity: SettingsProxyDb) -> SettingsProxy:
        if entity:
            return SettingsProxy(id=entity.id,
                                 is_selected=entity.is_selected,
                                 is_enabled=entity.is_enabled,
                                 name=entity.name,
                                 path=entity.path,
                                 delay_mode=DelayMode[entity.delay_mode],
                                 delay_from=entity.delay_from,
                                 delay_to=entity.delay_to,
                                 delay=entity.delay)
        return None
