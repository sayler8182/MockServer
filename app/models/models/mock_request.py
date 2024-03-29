from app.models.models.http_method import HTTPMethod
from app.models.models.mock_request_rule import MockRequestRule
from app.models.models.request_header import RequestHeader
from app.utils.utils import new_id, get_dict


class MockRequest(object):
    def __init__(self,
                 id: str = None,
                 mock_id: str = None,
                 method: HTTPMethod = None,
                 proxy: str = None,
                 path: str = None,
                 rules: [MockRequestRule] = []):
        self.id = id
        self.mock_id = mock_id
        self.method = method
        self.proxy = proxy
        self.path = path
        self.rules = rules
        self.__init_default_id()
        self.__init_default_method()

    @property
    def hash(self):
        rules_hash = "_".join(map(lambda rule: rule.hash, self.rules))
        return f"{self.method.name}-{self.proxy}-{self.path}-[{rules_hash}]"

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
            'rules': get_dict(self.rules)
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
        rules_list = object.get('rules', None) or []
        rules = list(map(lambda item: MockRequestRule.mock_request_rule_from_dict(item), rules_list))
        return MockRequest(id=id,
                           mock_id=mock_id,
                           method=method,
                           proxy=proxy,
                           path=path,
                           rules=rules)
