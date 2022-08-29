class ProxyRequest(object):
    def __init__(self,
                 method: str,
                 url: str,
                 data: str,
                 headers: dict,
                 json: str):
        self.method = method
        self.url = url
        self.data = data
        self.headers = headers
        self.json = json

    def get_dict(self):
        return {
            'method': self.method,
            'url': self.url,
            'data': self.data,
            'headers': self.headers,
            'json': self.json
        }
