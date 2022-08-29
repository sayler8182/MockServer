from enum import Enum

from app.utils.utils import new_id


class RequestHeaderType(Enum):
    settings_request = 'settings_request'
    settings_response = 'settings_response'
    mock_request = 'mock_request'
    mock_response = 'mock_response'


class RequestHeader(object):
    def __init__(self,
                 type: RequestHeaderType,
                 id: str = None,
                 proxy_id: str = None,
                 mock_id: str = None,
                 request_id: str = None,
                 response_id: str = None,
                 name: str = None,
                 value: str = None):
        self.id = id
        self.type = type
        self.proxy_id = proxy_id
        self.mock_id = mock_id
        self.request_id = request_id
        self.response_id = response_id
        self.name = name
        self.value = value
        self.__init_default_id()

    def __init_default_id(self):
        if self.id is None:
            self.id = new_id()

    def get_dict(self):
        return {
            'id': self.id,
            'type': self.type.get_dict(),
            'proxy_id': self.proxy_id,
            'mock_id': self.mock_id,
            'request_id': self.request_id,
            'response_id': self.response_id,
            'name': self.name,
            'value': self.value,
        }
