from enum import Enum


class ProxyResponseType(Enum):
    proxy = 'proxy'
    file = 'file'
    json = 'json'

    def get_dict(self):
        return self.value


class ProxyResponse(object):
    def __init__(self,
                 request,
                 response,
                 type: ProxyResponseType,
                 status_code: int,
                 headers: dict,
                 body: any):
        self.request = request
        self.response = response
        self.type = type
        self.status_code = status_code
        self.headers = headers
        self.body = body

    def get_dict(self):
        return {
            'type': self.type.value,
            'status_code': self.status_code,
            'headers': self.headers,
            'body': self.body,
        }
