from app.models.models.mock_request_rule_type import MockRequestRuleType
from app.utils.utils import new_id


class MockRequestRule(object):
    def __init__(self,
                 mock_id: str,
                 type: MockRequestRuleType,
                 id: str = None,
                 is_enabled: bool = None,
                 key: str = None,
                 value: str = None):
        self.id = id
        self.mock_id = mock_id
        self.type = type
        self.is_enabled = is_enabled
        self.key = key
        self.value = value
        self.__init_default_id()
        self.__init_default_is_enabled()

    @property
    def hash(self):
        return f"{self.type.value}-{self.key}-{self.value}"

    @property
    def description(self) -> str:
        return f'[{self.type.description}] rule'

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
            'type': self.type.get_dict(),
            'key': self.key,
            'value': self.value
        }

    @staticmethod
    def mock_request_rule_from_dict(object: dict):
        if object is None:
            return None

        id = object.get('id', None)
        mock_id = object.get('mock_id', None)
        type_string = object.get('type', None)
        type = MockRequestRuleType[type_string]
        is_enabled = object.get('is_enabled', None)
        key = object.get('key', None)
        value = object.get('value', None)
        return MockRequestRule(id=id,
                               mock_id=mock_id,
                               type=type,
                               is_enabled=is_enabled,
                               key=key,
                               value=value)
