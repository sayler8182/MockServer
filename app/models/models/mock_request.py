from app.models.models.http_method import HTTPMethod
from app.models.models.request_header import RequestHeader
from app.utils.utils import new_id, get_dict


class MockRequest(object):
    def __init__(self,
                 id: str = None,
                 mock_id: str = None,
                 method: HTTPMethod = None,
                 proxy: str = None,
                 path: str = None,
                 request_headers: [RequestHeader] = None):
        self.id = id
        self.mock_id = mock_id
        self.method = method
        self.proxy = proxy
        self.path = path
        self.request_headers = request_headers
        self.__init_default_id()
        self.__init_default_method()

    def __init_default_id(self):
        if self.id is None:
            self.id = new_id()

    def __init_default_method(self):
        if self.method is None:
            self.method = HTTPMethod.GET

    def get_dict(self):
        return {
            'id': self.id,
            'mock_id': self.mock_id,
            'method': self.method.get_dict(),
            'proxy': self.proxy,
            'path': self.path,
            'request_headers': get_dict(self.request_headers),
        }

    @staticmethod
    def mock_request_from_dict(object: dict):
        if object is None:
            return None

        id = object.get('id', None)
        mock_id = object.get('mock_id', None)
        method_string = object.get('method', None)
        method = HTTPMethod[method_string]
        proxy = object.get('proxy', None)
        path = object.get('path', None)
        request_headers_list = object.get('request_headers', None)
        request_headers = list(map(lambda item: RequestHeader.request_header_from_dict(item), request_headers_list))
        return MockRequest(id=id,
                           mock_id=mock_id,
                           method=method,
                           proxy=proxy,
                           path=path,
                           request_headers=request_headers)
