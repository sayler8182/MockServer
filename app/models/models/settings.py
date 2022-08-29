from app.models.models.request_header import RequestHeader
from app.models.models.settings_proxy import SettingsProxy
from app.utils.utils import get_dict


class Settings(object):
    def __init__(self,
                 proxy: SettingsProxy,
                 proxy_request_headers: [RequestHeader],
                 proxy_response_headers: [RequestHeader]):
        self.proxy = proxy
        self.proxy_request_headers = proxy_request_headers
        self.proxy_response_headers = proxy_response_headers

    def get_dict(self):
        return {
            'proxy': self.proxy.get_dict(),
            'proxy_request_headers': get_dict(self.proxy_request_headers),
            'proxy_response_headers': get_dict(self.proxy_response_headers)
        }
