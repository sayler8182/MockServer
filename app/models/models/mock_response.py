from enum import Enum

from app.models.models.delay_mode import DelayMode
from app.utils.utils import new_id


class MockResponseType(Enum):
    mock_json = 'mock_json'
    proxy = 'proxy'

    @property
    def description(self) -> str:
        return {
            MockResponseType.mock_json: 'Mock json',
            MockResponseType.proxy: 'Proxy'
        }.get(self)

    @property
    def is_mock(self) -> bool:
        return {
            MockResponseType.mock_json: True,
            MockResponseType.proxy: False
        }.get(self)

    @property
    def is_proxy(self) -> bool:
        return {
            MockResponseType.mock_json: False,
            MockResponseType.proxy: True
        }.get(self)

    @staticmethod
    def supported_types():
        return [
            MockResponseType.mock_json,
            MockResponseType.proxy
        ]

    def get_dict(self):
        return self.value


class MockResponse(object):
    def __init__(self,
                 id: str = None,
                 mock_id: str = None,
                 is_enabled: bool = None,
                 type: MockResponseType = None,
                 name: str = None,
                 status: int = None,
                 delay_mode: DelayMode = None,
                 delay: int = None,
                 body: str = None,
                 order: int = None):
        self.id = id
        self.mock_id = mock_id
        self.is_enabled = is_enabled
        self.type = type
        self.name = name
        self.status = status
        self.delay_mode = delay_mode
        self.delay = delay
        self.body = body
        self.order = order
        self.__init_default_id()
        self.__init_default_is_enabled()
        self.__init_default_type()
        self.__init_default_status()
        self.__init_default_delay_mode()
        self.__init_default_delay()
        self.__init_default_order()

    @property
    def description(self) -> str:
        return {
            MockResponseType.mock_json: f'Mock - [{self.status}] {self.name or ""}',
            MockResponseType.proxy: f'Proxy - {self.name or ""}',
        }.get(self.type)

    def __init_default_id(self):
        if self.id is None:
            self.id = new_id()

    def __init_default_is_enabled(self):
        if self.is_enabled is None:
            self.is_enabled = True

    def __init_default_type(self):
        if self.type is None:
            self.type = MockResponseType.mock_json

    def __init_default_status(self):
        if self.status is None:
            self.status = 200

    def __init_default_delay_mode(self):
        if self.delay_mode is None:
            self.delay_mode = DelayMode.static

    def __init_default_delay(self):
        if self.delay is None:
            self.delay = 0

    def __init_default_order(self):
        if self.order is None:
            self.order = -1

    def get_dict(self):
        return {
            'id': self.id,
            'mock_id': self.mock_id,
            'is_enabled': self.is_enabled,
            'type': self.type.get_dict(),
            'name': self.name,
            'status': self.status,
            'delay_mode': self.delay_mode.get_dict(),
            'delay': self.delay,
            'body': self.body,
            'order': self.order
        }

    @staticmethod
    def mock_response_from_dict(object: dict):
        if object is None:
            return None

        id = object.get('id', None)
        mock_id = object.get('mock_id', None)
        is_enabled = object.get('is_enabled', None)
        type_string = object.get('type', None)
        type = MockResponseType[type_string]
        name = object.get('name', None)
        status = object.get('status', None)
        delay_mode_string = object.get('delay_mode', None)
        delay_mode = DelayMode[delay_mode_string]
        delay = object.get('delay', None)
        body = object.get('body', None)
        order = object.get('order', None)
        return MockResponse(id=id,
                            mock_id=mock_id,
                            is_enabled=is_enabled,
                            type=type,
                            name=name,
                            status=status,
                            delay_mode=delay_mode,
                            delay=delay,
                            body=body,
                            order=order)
