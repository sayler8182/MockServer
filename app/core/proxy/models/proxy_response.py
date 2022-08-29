from enum import Enum


class ProxyResponseType(Enum):
    json = 'json'


class ProxyResponse(object):
    def __init__(self,
                 response,
                 type: ProxyResponseType,
                 status_code: int,
                 headers: dict,
                 body: any):
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
