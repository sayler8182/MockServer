from app.models.models.mock_response_interceptor_type import MockResponseInterceptorType
from app.utils.utils import new_id


class MockResponseInterceptor(object):
    def __init__(self,
                 mock_id: str,
                 response_id: str,
                 type: MockResponseInterceptorType,
                 id: str = None,
                 is_enabled: bool = None,
                 name: str = None,
                 configuration: str = None):
        self.id = id
        self.mock_id = mock_id
        self.response_id = response_id
        self.type = type
        self.is_enabled = is_enabled
        self.name = name
        self.configuration = configuration
        self.__init_default_id()
        self.__init_default_is_enabled()

    @property
    def description(self) -> str:
        name = self.name or 'Default'
        return f'[{self.type.description}] {name} interceptor'

    def __init_default_id(self):
        if self.id is None:
            self.id = new_id()

    def __init_default_is_enabled(self):
        if self.is_enabled is None:
            self.is_enabled = True

    def get_dict(self):
        return {
            'id': self.id,
            'mock_id': self.mock_id,
            'response_id': self.response_id,
            'type': self.type.get_dict(),
            'name': self.name,
            'configuration': self.configuration
        }

    @staticmethod
    def mock_response_interceptor_from_dict(object: dict):
        if object is None:
            return None

        id = object.get('id', None)
        mock_id = object.get('mock_id', None)
        response_id = object.get('response_id', None)
        type_string = object.get('type', None)
        type = MockResponseInterceptorType[type_string]
        name = object.get('name', None)
        configuration = object.get('configuration', None)
        return MockResponseInterceptor(id=id,
                                       mock_id=mock_id,
                                       response_id=response_id,
                                       type=type,
                                       name=name,
                                       configuration=configuration)
