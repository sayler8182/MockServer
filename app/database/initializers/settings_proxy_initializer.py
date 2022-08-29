from app.adapters.settings_proxy_adapter import SettingsProxyAdapter
from app.models.models.settings_proxy import SettingsProxy


class SettingsProxyInitializer(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app

    def init_initializer(self):
        proxy = SettingsProxy(is_selected=True,
                              is_enabled=True,
                              name='Default')
        SettingsProxyAdapter.add_proxy(proxy)
