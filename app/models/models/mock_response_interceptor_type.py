from enum import Enum

from app.models.models.mock_response_type import MockResponseType


class MockResponseInterceptorType(Enum):
    custom = 'custom'
    value_replace = 'value_replace'

    @property
    def description(self) -> str:
        return {
            MockResponseInterceptorType.custom: 'Custom',
            MockResponseInterceptorType.value_replace: 'Replace value'
        }.get(self)

    @staticmethod
    def supported_types():
        return [
            MockResponseInterceptorType.custom,
            MockResponseInterceptorType.value_replace
        ]

    @staticmethod
    def supported_types_for_response(response: any):
        if not response or not response.type:
            return []
        type = response.type
        types = MockResponseInterceptorType.supported_types()
        return list(filter(lambda item: item.is_available(type), types))

    def get_dict(self):
        return self.value

    def is_available(self, type: MockResponseType):
        common_items = [
            MockResponseInterceptorType.custom,
            MockResponseInterceptorType.value_replace
        ]
        items = {
            MockResponseType.mock_json: common_items + [],
            MockResponseType.proxy: common_items + []
        }.get(type)
        return self in items
