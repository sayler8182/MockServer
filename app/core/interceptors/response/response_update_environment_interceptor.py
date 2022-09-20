import json

import jsonpath_ng

from app.adapters.environment_adapter import EnvironmentAdapter
from app.core.template_manager import TemplateManager
from app.models.models.environment_item import EnvironmentItem
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.mock_response_interceptor import MockResponseInterceptor
from app.utils.utils import to_list, to_binary, first


class ResponseUpdateEnvironmentInterceptor(object):
    def intercept(self, response, mock: Mock, mock_response: MockResponse, interceptor: MockResponseInterceptor):
        if response and response.body:
            body = to_binary(response.body)
            configurations = to_list(json.loads(interceptor.configuration))
            for configuration in configurations:
                key_path = configuration.get('key_path', None)
                name = configuration.get('name', None)
                skip_templating = configuration.get('skip_templating', False)
                object = json.loads(body)
                if object and key_path:
                    expression = jsonpath_ng.parse(key_path)
                    matches = expression.find(object)
                    value = first(list(map(lambda item: item.value, matches)))
                    if not skip_templating:
                        template_manager = TemplateManager()
                        value = template_manager.apply_templating(value)
                    item = EnvironmentItem(name=name, value=value)
                    EnvironmentAdapter.add_environment(item)
        return response

    @staticmethod
    def is_configurable() -> any:
        return True

    @staticmethod
    def example() -> any:
        return [
            {
                "key_path": "required string - key path to string value (jsonpath_ng format) eg -> response.items[2].key",
                "name": "required string - environment item name",
                "skip_templating": "optional bool - False if omitted - global templating has to be also disabled"
            }
        ]