from app.adapters.request_header_adapter import RequestHeaderAdapter
from app.config.database_config import db
from app.models.db.proxy_db import ProxyDb
from app.models.db.request_header_db import RequestHeaderDb
from app.models.models.delay_mode import DelayMode
from app.models.models.proxy import Proxy
from app.models.models.request_header import RequestHeaderType


class ProxyAdapter(object):
    @staticmethod
    def get_proxies() -> [Proxy]:
        query = ProxyDb.query.all()
        return list(map(lambda item: ProxyAdapter.settings_proxy_from_entity(item), query))

    @staticmethod
    def get_proxy_selected() -> Proxy:
        query = ProxyDb.query.filter_by(is_selected=True).first()
        return ProxyAdapter.settings_proxy_from_entity(query)

    @staticmethod
    def get_proxy(proxy_id: str) -> Proxy:
        query = ProxyDb.query.filter_by(id=proxy_id).first()
        return ProxyAdapter.settings_proxy_from_entity(query)

    @staticmethod
    def add_proxy(proxy: Proxy, commit: bool = True):
        entity = ProxyAdapter.settings_proxy_from_object(proxy)
        db.session.merge(entity)
        ProxyAdapter.set_proxy_select(entity.id, entity.is_selected, False)
        if commit:
            db.session.commit()

    @staticmethod
    def set_proxy_select(proxy_id: str, is_selected: bool, commit: bool = True):
        proxies = ProxyAdapter.get_proxies()
        for proxy in proxies:
            proxy = ProxyAdapter.get_proxy(proxy_id=proxy.id)
            entity = ProxyAdapter.settings_proxy_from_object(proxy)
            entity.is_selected = False
            db.session.merge(entity)
        proxy = ProxyAdapter.get_proxy(
            proxy_id=proxy_id) if is_selected else proxies[0]
        entity = ProxyAdapter.settings_proxy_from_object(proxy)
        entity.is_selected = True
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_proxy_enable(proxy_id: str, commit: bool = True):
        proxy = ProxyAdapter.get_proxy(proxy_id=proxy_id)
        entity = ProxyAdapter.settings_proxy_from_object(proxy)
        entity.is_enabled = True
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_proxy_disable(proxy_id: str, commit: bool = True):
        proxy = ProxyAdapter.get_proxy(proxy_id=proxy_id)
        entity = ProxyAdapter.settings_proxy_from_object(proxy)
        entity.is_enabled = False
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_proxy_templating_enable(proxy_id: str, commit: bool = True):
        proxy = ProxyAdapter.get_proxy(proxy_id=proxy_id)
        entity = ProxyAdapter.settings_proxy_from_object(proxy)
        entity.is_templating_enabled = True
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_proxy_templating_disable(proxy_id: str, commit: bool = True):
        proxy = ProxyAdapter.get_proxy(proxy_id=proxy_id)
        entity = ProxyAdapter.settings_proxy_from_object(proxy)
        entity.is_templating_enabled = False
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_proxy_name_and_path(proxy_id: str, name: str, path: str, commit: bool = True):
        proxy = ProxyAdapter.get_proxy(proxy_id=proxy_id)
        entity = ProxyAdapter.settings_proxy_from_object(proxy)
        entity.name = name
        entity.path = path
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_proxy_delay_mode(proxy_id: str, delay_mode: DelayMode, commit: bool = True):
        proxy = ProxyAdapter.get_proxy(proxy_id=proxy_id)
        entity = ProxyAdapter.settings_proxy_from_object(proxy)
        entity.delay_mode = delay_mode.value
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_proxy_delay_static(proxy_id: str, delay: int, commit: bool = True):
        proxy = ProxyAdapter.get_proxy(proxy_id=proxy_id)
        entity = ProxyAdapter.settings_proxy_from_object(proxy)
        entity.delay = delay
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_proxy_delay_random(proxy_id: str, delay_from: int, delay_to: int, commit: bool = True):
        proxy = ProxyAdapter.get_proxy(proxy_id=proxy_id)
        entity = ProxyAdapter.settings_proxy_from_object(proxy)
        entity.delay_from = delay_from
        entity.delay_to = delay_to
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def remove_proxy(proxy_id: str, commit: bool = True):
        proxies = ProxyDb.query.all()
        RequestHeaderDb.query.filter_by(proxy_id=proxy_id).delete()
        if len(proxies) > 1:
            ProxyDb.query.filter_by(id=proxy_id).delete()
            if commit:
                db.session.commit()

    # mappers
    @staticmethod
    def settings_proxy_from_object(object: Proxy) -> ProxyDb:
        if object:
            return ProxyDb(id=object.id,
                           is_selected=object.is_selected,
                           is_enabled=object.is_enabled,
                           is_templating_enabled=object.is_templating_enabled,
                           name=object.name,
                           path=object.path,
                           delay_mode=object.delay_mode.value,
                           delay_from=object.delay_from,
                           delay_to=object.delay_to,
                           delay=object.delay)
        return None

    @staticmethod
    def settings_proxy_from_entity(entity: ProxyDb) -> Proxy:
        if entity:
            request_headers = RequestHeaderAdapter.get_request_headers_for_proxy(entity.id,
                                                                                 RequestHeaderType.proxy_request)
            response_headers = RequestHeaderAdapter.get_request_headers_for_proxy(entity.id,
                                                                                  RequestHeaderType.proxy_response)
            return Proxy(id=entity.id,
                         is_selected=entity.is_selected,
                         is_enabled=entity.is_enabled,
                         is_templating_enabled=entity.is_templating_enabled,
                         name=entity.name,
                         path=entity.path,
                         delay_mode=DelayMode[entity.delay_mode],
                         delay_from=entity.delay_from,
                         delay_to=entity.delay_to,
                         delay=entity.delay,
                         request_headers=request_headers,
                         response_headers=response_headers)
        return None
