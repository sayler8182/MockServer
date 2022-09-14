from app.adapters.proxy_adapter import ProxyAdapter
from app.models.models.settings import Settings


class SettingsAdapter(object):
    @staticmethod
    def get_settings() -> Settings:
        proxy = ProxyAdapter.get_proxy_selected()
        return Settings(proxy=proxy)
