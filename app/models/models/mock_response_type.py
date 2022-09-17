from enum import Enum


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
