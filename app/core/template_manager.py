import json
import os
import re

from app.adapters.environment_adapter import EnvironmentAdapter
from app.core.template_environment_executor import get_value_for_static
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.mock_response_interceptor import MockResponseInterceptor
from app.models.models.proxy_request import ProxyRequest
from app.models.models.proxy_response import ProxyResponse


class TemplateManager(object):
    def __init__(self,
                 request: ProxyRequest = None,
                 response: ProxyResponse = None,
                 mock: Mock = None,
                 mock_response: MockResponse = None,
                 interceptor: MockResponseInterceptor = None):
        self.request = request
        self.response = response
        self.mock = mock
        self.mock_response = mock_response
        self.interceptor = interceptor

    def apply_templating(self, string: str) -> str:
        environment = self.__get_environment()
        return self.__apply(string, environment)

    def __get_environment(self) -> dict:
        environment = EnvironmentAdapter.get_environment()
        static = environment.static
        dynamic = environment.dynamic
        static = dict(map(lambda item: (item.name, None), static))
        dynamic = dict(map(lambda item: (item.name, item.value), dynamic))
        items = {}
        items.update(static)
        items.update(dynamic)
        return items

    def __apply(self, string: str, environment: dict) -> [str]:
        separator = "|"
        result = string
        keys = re.findall(r'{{(.*?)}}', f'{string}')
        for key in keys:
            value = self.__get_value(key, environment, separator)
            if isinstance(value, str):
                result = result.replace(f'{{{{{key}}}}}', value)
            elif isinstance(value, int):
                result = result.replace(f'"{{{{{key}}}}}"', f"{value}")
            elif isinstance(value, dict):
                value = json.dumps(value, separators=(',', ':'))
                result = result.replace(f'"{{{{{key}}}}}"', value)
            else:
                result = result.replace(f'"{{{{{key}}}}}"', "null")
        return result

    def __get_value(self, key: str, environment: dict, separator: str) -> str:
        head, sep, tail = key.partition(separator)

        static = get_value_for_static(self, head, tail, separator)
        if static is not None:
            return static

        dynamic = environment.get(head, None)
        if dynamic is not None:
            return dynamic

        system = os.getenv(head)
        if system is not None:
            return system

        return None
