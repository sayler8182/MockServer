from app.adapters.request_header_adapter import RequestHeaderAdapter
from app.adapters.settings_proxy_adapter import SettingsProxyAdapter
from app.models.models.request_header import RequestHeaderType
from app.models.models.settings import Settings


class SettingsAdapter(object):
    @staticmethod
    def get_settings() -> Settings:
        proxy = SettingsProxyAdapter.get_selected_proxy()
        return Settings(
            proxy=SettingsProxyAdapter.get_proxy(proxy.id),
            proxy_request_headers=RequestHeaderAdapter.get_request_headers_for_proxy(proxy.id,
                                                                                     RequestHeaderType.settings_request),
            proxy_response_headers=RequestHeaderAdapter.get_request_headers_for_proxy(proxy.id,
                                                                                      RequestHeaderType.settings_response))
