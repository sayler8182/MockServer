from enum import Enum

from app.models.models.mock_request import MockRequest
from app.models.models.mock_response import MockResponse
from app.utils.utils import new_id, get_dict


class MockMethod(Enum):
    random = 'random'
    rotate = 'rotate'
    sequential = 'sequential'

    @property
    def description(self) -> str:
        return {
            MockMethod.random: 'Random',
            MockMethod.rotate: 'Rotate',
            MockMethod.sequential: 'Sequential'
        }.get(self)

    @staticmethod
    def supported_methods():
        return [
            MockMethod.rotate,
            MockMethod.sequential
        ]

    def get_dict(self):
        return self.value


class Mock(object):
    def __init__(self,
                 id: str = None,
                 scenario_id: str = None,
                 name: str = None,
                 is_enabled: bool = None,
                 method: MockMethod = None,
                 response_id: str = None,
                 request: MockRequest = None,
                 responses: [MockResponse] = None):
        self.id = id
        self.scenario_id = scenario_id
        self.name = name
        self.is_enabled = is_enabled
        self.method = method
        self.response_id = response_id
        self.request = request
        self.responses = responses
        self.__init_default_id()
        self.__init_default_is_enabled()
        self.__init_default_method()
        self.__init_default_request()
        self.__init_default_responses()

    @property
    def description(self) -> str:
        return self.name or self.request.path or ''

    def __init_default_id(self):
        if self.id is None:
            self.id = new_id()

    def __init_default_is_enabled(self):
        if self.is_enabled is None:
            self.is_enabled = True

    def __init_default_method(self):
        if self.method is None:
            self.method = MockMethod.rotate

    def __init_default_request(self):
        if self.request is None:
            self.request = MockRequest(mock_id=self.id)
        elif self.request.mock_id is None:
            self.request.mock_id = self.id

    def __init_default_responses(self):
        if self.responses is None:
            self.responses = []
        else:
            for response in self.responses:
                if response.mock_id is None:
                    response.mock_id = self.id

    def get_dict(self):
        return {
            'id': self.id,
            'scenario_id': self.scenario_id,
            'name': self.name,
            'is_enabled': self.is_enabled,
            'method': self.method.value,
            'response_id': self.response_id,
            'request': self.request.get_dict(),
            'responses': get_dict(self.responses)
        }

    @staticmethod
    def mock_from_dict(object: dict):
        if object is None:
            return None

        id = object.get('id', None)
        scenario_id = object.get('scenario_id', None)
        name = object.get('name', None)
        is_enabled = object.get('is_enabled', None)
        method_string = object.get('method', None)
        method = MockMethod[method_string]
        response_id = object.get('response_id', None)
        request_dict = object.get('request', None)
        request = MockRequest.mock_request_from_dict(request_dict)
        responses_list = object.get('responses', None)
        responses = list(map(lambda item: MockResponse.mock_response_from_dict(item), responses_list))
        return Mock(id=id,
                    scenario_id=scenario_id,
                    name=name,
                    is_enabled=is_enabled,
                    method=method,
                    response_id=response_id,
                    request=request,
                    responses=responses)
