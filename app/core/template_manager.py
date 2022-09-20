import re

from app.adapters.environment_adapter import EnvironmentAdapter
from app.core.template_environment_executor import get_value_for_static


class TemplateManager(object):
    def apply_templating(self, string: str) -> str:
        environment = self.__get_environment()
        return self.__apply(string, environment)

    def __get_environment(self) -> dict:
        environment = EnvironmentAdapter.get_environment()
        static = environment.static
        dynamic = environment.dynamic
        static = dict(map(lambda item: (item.name, item.value), static))
        dynamic = dict(map(lambda item: (item.name, item.value), dynamic))
        items = {}
        items.update(static)
        items.update(dynamic)
        return items

    def __apply(self, string: str, environment: dict) -> [str]:
        result = string
        keys = re.findall(r'{{(.*?)}}', string)
        for key in keys:
            value = self.__get_value(key, environment)
            if value:
                result = result.replace(f'{{{{{key}}}}}', value)
        return result

    def __get_value(self, key: str, environment: dict) -> str:
        return get_value_for_static(key) or environment.get(key, None)
