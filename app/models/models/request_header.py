from enum import Enum

from app.utils.utils import new_id


class RequestHeaderType(Enum):
    proxy_request = 'proxy_request'
    proxy_response = 'proxy_response'
    mock_request = 'mock_request'
    mock_response = 'mock_response'

    def get_dict(self):
        return self.value


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

    @staticmethod
    def request_header_from_dict(object: dict):
        if object is None:
            return None

        id = object.get('id', None)
        type_string = object.get('type', None)
        type = RequestHeaderType[type_string]
        proxy_id = object.get('proxy_id', None)
        mock_id = object.get('mock_id', None)
        request_id = object.get('request_id', None)
        response_id = object.get('response_id', None)
        name = object.get('name', None)
        value = object.get('value', None)
        return RequestHeader(id=id,
                             type=type,
                             proxy_id=proxy_id,
                             mock_id=mock_id,
                             request_id=request_id,
                             response_id=response_id,
                             name=name,
                             value=value)
