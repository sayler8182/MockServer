from app.models.models.delay_mode import DelayMode
from app.models.models.mock_response_interceptor import MockResponseInterceptor
from app.models.models.mock_response_type import MockResponseType
from app.models.models.request_header import RequestHeader
from app.utils.utils import new_id, get_dict


class MockResponse(object):
    def __init__(self,
                 id: str = None,
                 mock_id: str = None,
                 is_enabled: bool = None,
                 is_single_use: bool = None,
                 type: MockResponseType = None,
                 name: str = None,
                 status: int = None,
                 delay_mode: DelayMode = None,
                 delay: int = None,
                 body: str = None,
                 order: int = None,
                 response_headers: [RequestHeader] = None,
                 response_interceptors: [MockResponseInterceptor] = None):
        self.id = id
        self.mock_id = mock_id
        self.is_enabled = is_enabled
        self.is_single_use = is_single_use
        self.type = type
        self.name = name
        self.status = status
        self.delay_mode = delay_mode
        self.delay = delay
        self.body = body
        self.order = order
        self.response_headers = response_headers
        self.response_interceptors = response_interceptors
        self.__init_default_id()
        self.__init_default_is_enabled()
        self.__init_default_is_single_use()
        self.__init_default_type()
        self.__init_default_status()
        self.__init_default_delay_mode()
        self.__init_default_delay()
        self.__init_default_order()
        self.__init_default_response_interceptors()

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

    def __init_default_is_single_use(self):
        if self.is_single_use is None:
            self.is_single_use = False

    def __init_default_type(self):
        if self.type is None:
            self.type = MockResponseType.mock_json

    def __init_default_status(self):
        if self.status is None:
            self.status = 200

    def __init_default_delay_mode(self):
        if self.delay_mode is None:
            self.delay_mode = DelayMode.none

    def __init_default_delay(self):
        if self.delay is None:
            self.delay = 0

    def __init_default_order(self):
        if self.order is None:
            self.order = -1

    def __init_default_response_interceptors(self):
        if self.response_interceptors is None:
            self.response_interceptors = []

    def get_dict(self):
        return {
            'id': self.id,
            'mock_id': self.mock_id,
            'is_enabled': self.is_enabled,
            'is_single_use': self.is_single_use,
            'type': self.type.get_dict(),
            'name': self.name,
            'status': self.status,
            'delay_mode': self.delay_mode.get_dict(),
            'delay': self.delay,
            'body': self.body,
            'order': self.order,
            'response_headers': get_dict(self.response_headers),
            'response_interceptors': get_dict(self.response_interceptors)
        }

    @staticmethod
    def mock_response_from_dict(object: dict):
        if object is None:
            return None

        id = object.get('id', None)
        mock_id = object.get('mock_id', None)
        is_enabled = object.get('is_enabled', None)
        is_single_use = object.get('is_single_use', None)
        type_string = object.get('type', None)
        type = MockResponseType[type_string]
        name = object.get('name', None)
        status = object.get('status', None)
        delay_mode_string = object.get('delay_mode', None)
        delay_mode = DelayMode[delay_mode_string]
        delay = object.get('delay', None)
        body = object.get('body', None)
        order = object.get('order', None)
        response_headers_list = object.get('response_headers', None) or []
        response_headers = list(map(lambda item: RequestHeader.request_header_from_dict(item), response_headers_list))
        response_interceptors_list = object.get('response_interceptors', None) or []
        response_interceptors = list(map(lambda item: MockResponseInterceptor.mock_response_interceptor_from_dict(item),
                                         response_interceptors_list))
        return MockResponse(id=id,
                            mock_id=mock_id,
                            is_enabled=is_enabled,
                            is_single_use=is_single_use,
                            type=type,
                            name=name,
                            status=status,
                            delay_mode=delay_mode,
                            delay=delay,
                            body=body,
                            order=order,
                            response_headers=response_headers,
                            response_interceptors=response_interceptors)
