import json
from datetime import datetime

from app.models.models.delay_mode import DelayMode
from app.models.models.http_method import HTTPMethod
from app.models.models.mock_response_type import MockResponseType
from app.models.models.proxy_response import ProxyResponseType
from app.utils.utils import new_id, get_dict, clean_nones


class MockResponseLog(object):
    def __init__(self,
                 id: str = None,
                 mock_id: str = None,
                 response_id: str = None,
                 date: datetime = None,
                 data: any = None):
        self.id = id
        self.mock_id = mock_id
        self.response_id = response_id
        self.date = date
        self.data = data if isinstance(data, MockResponseLogData) else MockResponseLogData.decode(data)
        self.__init_default_id()
        self.__init_default_date()

    @property
    def view_name(self):
        path = self.data.path or ''
        return {
            ProxyResponseType.proxy: f'<b>[PROXY]</b> {path}',
            ProxyResponseType.json: f'<b>[JSON]</b> {path}',
            ProxyResponseType.file: f'<b>[FILE]</b> {path}',
        }.get(self.data.type)

    @property
    def view_description(self):
        path = self.data.path or ''
        return {
            ProxyResponseType.proxy: f'<i>{self.data.response_name}</i>',
            ProxyResponseType.json: f'<i>{self.data.response_name}</i>',
            ProxyResponseType.file: f'<i>{self.data.body_path}</i>',
        }.get(self.data.type)

    @property
    def description(self):
        object = self.data.get_dict()
        object['body'] = '/* ... */'
        object = clean_nones(object)
        return f'{json.dumps(object, indent=4)}'

    def __init_default_id(self):
        if self.id is None:
            self.id = new_id()

    def __init_default_date(self):
        if self.date is None:
            self.date = datetime.now()

    def get_dict(self):
        return {
            'id': self.id,
            'mock_id': self.mock_id,
            'response_id': self.response_id,
            'date': self.date.isoformat(),
            'data': MockResponseLogData.encode(self.data)
        }


class MockResponseLogData(object):
    def __init__(self,
                 type: ProxyResponseType = None,
                 mock_name: str = None,
                 method: HTTPMethod = None,
                 proxy: str = None,
                 path: str = None,
                 is_single_use: bool = None,
                 response_type: MockResponseType = None,
                 response_name: str = None,
                 status_code: int = None,
                 delay_mode: DelayMode = None,
                 delay_from: int = None,
                 delay_to: int = None,
                 delay: int = None,
                 body: str = None,
                 body_path: str = None):
        self.type = type
        self.mock_name = mock_name
        self.method = method
        self.proxy = proxy
        self.path = path
        self.is_single_use = is_single_use
        self.response_type = response_type
        self.response_name = response_name
        self.status_code = status_code
        self.delay_mode = delay_mode
        self.delay_from = delay_from
        self.delay_to = delay_to
        self.delay = delay
        self.body = body
        self.body_path = body_path

    def get_dict(self):
        return {
            'type': get_dict(self.type),
            'mock_name': self.mock_name,
            'method': get_dict(self.method),
            'proxy': self.proxy,
            'path': self.path,
            'is_single_use': self.is_single_use,
            'response_type': get_dict(self.response_type),
            'response_name': self.response_name,
            'status_code': self.status_code,
            'delay_mode': get_dict(self.delay_mode),
            'delay_from': self.delay_from,
            'delay_to': self.delay_to,
            'delay': self.delay,
            'body': self.body,
            'body_path': self.body_path,
        }

    @staticmethod
    def decode(data: str) -> any:
        object = json.loads(data)
        type_string = object.get('type', None)
        type = ProxyResponseType[type_string] if type_string else None
        mock_name = object.get('mock_name', None)
        method_string = object.get('method', None)
        method = HTTPMethod[method_string] if method_string else None
        proxy = object.get('proxy', None)
        path = object.get('path', None)
        is_single_use = object.get('is_single_use', None)
        response_type_string = object.get('response_type', None)
        response_type = MockResponseType[response_type_string] if response_type_string else None
        response_name = object.get('response_name', None)
        status_code = object.get('status_code', None)
        delay_mode_string = object.get('delay_mode', None)
        delay_mode = DelayMode[delay_mode_string] if delay_mode_string else None
        delay_from = object.get('delay_from', None)
        delay_to = object.get('delay_to', None)
        delay = object.get('delay', None)
        body = object.get('body', None)
        body_path = object.get('body_path', None)
        return MockResponseLogData(type=type,
                                   mock_name=mock_name,
                                   method=method,
                                   proxy=proxy,
                                   path=path,
                                   is_single_use=is_single_use,
                                   response_type=response_type,
                                   response_name=response_name,
                                   status_code=status_code,
                                   delay_mode=delay_mode,
                                   delay_from=delay_from,
                                   delay_to=delay_to,
                                   delay=delay,
                                   body=body,
                                   body_path=body_path)

    @staticmethod
    def encode(data) -> str:
        object = data.get_dict()
        return json.dumps(object)
