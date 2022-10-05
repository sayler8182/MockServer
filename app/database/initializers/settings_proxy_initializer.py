from app.adapters.proxy_adapter import ProxyAdapter
from app.models.models.proxy import Proxy


class SettingsProxyInitializer(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app

    def init_initializer(self):
        proxies = ProxyAdapter.get_proxies()
        if not proxies:
            proxy = Proxy(is_selected=True,
                          is_enabled=True,
                          name='Default')
            ProxyAdapter.add_proxy(proxy)
