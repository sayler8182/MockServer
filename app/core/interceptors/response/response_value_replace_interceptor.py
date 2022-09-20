import json

import jsonpath_ng

from app.core.template_manager import TemplateManager
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.mock_response_interceptor import MockResponseInterceptor
from app.utils.utils import to_list


class ResponseValueReplaceInterceptor(object):
    def intercept(self, response, mock: Mock, mock_response: MockResponse, interceptor: MockResponseInterceptor):
        if response and response.body:
            body = response.body
            configurations = to_list(json.loads(interceptor.configuration))
            for configuration in configurations:
                key_path = configuration.get('key_path', None)
                value = configuration.get('value', None)
                skip_templating = configuration.get('skip_templating', False)
                object = json.loads(body)
                if object and key_path:
                    expression = jsonpath_ng.parse(key_path)
                    if not skip_templating:
                        template_manager = TemplateManager()
                        value = template_manager.apply_templating(value)
                    data = expression.update(object, value)
                    new_body = json.dumps(data, separators=(',', ':'))
                    body = new_body.encode()
            response.body = body
        return response

    @staticmethod
    def is_configurable() -> any:
        return True

    @staticmethod
    def example() -> any:
        return [
            {
                "key_path": "required string - key path to value (jsonpath_ng format) eg -> response.items[2].key",
                "value": "required any - new value",
                "skip_templating": "optional bool - False if omitted",
                "if_value": {
                    "equal": "optional any - if exist replace only if old value is equal to this",
                    "not_equal": "optional any - if exist replace only if old value is not equal to this",
                    "greater": "optional number - if exist replace only if old value is greater to this",
                    "less": "optional number - if exist replace only if old value is less to this"
                }
            }
        ]
