from app.models.models.proxy import Proxy


class Settings(object):
    def __init__(self,
                 proxy: Proxy):
        self.proxy = proxy

    def get_dict(self):
        return {
            'proxy': self.proxy.get_dict()
        }
