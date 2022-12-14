from app.models.models.delay_mode import DelayMode
from app.models.models.request_header import RequestHeader
from app.utils.utils import new_id, get_dict


class Proxy(object):
    def __init__(self,
                 id: str = None,
                 is_selected: bool = None,
                 is_enabled: bool = None,
                 is_templating_enabled: bool = None,
                 name: str = None,
                 path: str = None,
                 delay_mode: DelayMode = None,
                 delay_from: int = None,
                 delay_to: int = None,
                 delay: int = None,
                 request_headers: [RequestHeader] = None,
                 response_headers: [RequestHeader] = None):
        self.id = id
        self.is_selected = is_selected
        self.is_enabled = is_enabled
        self.is_templating_enabled = is_templating_enabled
        self.name = name
        self.path = path
        self.delay_mode = delay_mode
        self.delay_from = delay_from
        self.delay_to = delay_to
        self.delay = delay
        self.request_headers = request_headers
        self.response_headers = response_headers
        self.__init_default_id()
        self.__init_default_is_selected()
        self.__init_default_is_enabled()
        self.__init_default_is_templating_enabled()
        self.__init_default_delay_mode()
        self.__init_default_delay_from()
        self.__init_default_delay_to()
        self.__init_default_delay()

    def __init_default_id(self):
        if self.id is None:
            self.id = new_id()

    def __init_default_is_selected(self):
        if self.is_selected is None:
            self.is_selected = False

    def __init_default_is_enabled(self):
        if self.is_enabled is None:
            self.is_enabled = False

    def __init_default_is_templating_enabled(self):
        if self.is_templating_enabled is None:
            self.is_templating_enabled = True

    def __init_default_delay_mode(self):
        if self.delay_mode is None:
            self.delay_mode = DelayMode.none

    def __init_default_delay_from(self):
        if self.delay_from is None:
            self.delay_from = 0

    def __init_default_delay_to(self):
        if self.delay_to is None:
            self.delay_to = 0

    def __init_default_delay(self):
        if self.delay is None:
            self.delay = 0

    def get_dict(self):
        return {
            'id': self.id,
            'is_selected': self.is_selected,
            'is_enabled': self.is_enabled,
            'is_templating_enabled': self.is_templating_enabled,
            'name': self.name,
            'path': self.path,
            'delay_mode': self.delay_mode.get_dict(),
            'delay_from': self.delay_from,
            'delay_to': self.delay_to,
            'delay': self.delay,
            'request_headers': get_dict(self.request_headers),
            'response_headers': get_dict(self.response_headers)
        }

    @staticmethod
    def proxy_from_dict(object: dict):
        if object is None:
            return None

        id = object.get('id', None)
        is_selected = object.get('is_selected', None)
        is_enabled = object.get('is_enabled', None)
        is_templating_enabled = object.get('is_templating_enabled', None)
        name = object.get('name', None)
        path = object.get('path', None)
        delay_mode_string = object.get('delay_mode', None)
        delay_mode = DelayMode[delay_mode_string]
        delay_from = object.get('delay_from', None)
        delay_to = object.get('delay_to', None)
        delay = object.get('delay', None)
        request_headers_list = object.get('request_headers', None) or []
        request_headers = list(map(lambda item: RequestHeader.request_header_from_dict(item), request_headers_list))
        response_headers_list = object.get('response_headers', None) or []
        response_headers = list(
            map(lambda item: RequestHeader.request_header_from_dict(item), response_headers_list))
        return Proxy(id=id,
                     is_selected=is_selected,
                     is_enabled=is_enabled,
                     is_templating_enabled=is_templating_enabled,
                     name=name,
                     path=path,
                     delay_mode=delay_mode,
                     delay_from=delay_from,
                     delay_to=delay_to,
                     delay=delay,
                     request_headers=request_headers,
                     response_headers=response_headers)
