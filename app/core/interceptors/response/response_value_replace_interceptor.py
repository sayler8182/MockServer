import json

import jsonpath_ng

from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.mock_response_interceptor import MockResponseInterceptor


class ResponseValueReplaceInterceptor(object):
    def intercept(self, response, mock: Mock, mock_response: MockResponse, interceptor: MockResponseInterceptor):
        if response and response.body:
            configuration = json.loads(interceptor.configuration)
            key_path = configuration.get('key_path', None)
            value = configuration.get('value', None)
            object = json.loads(response.body)
            if object and key_path:
                expression = jsonpath_ng.parse(key_path)
                data = expression.update(object, value)
                new_body = json.dumps(data, separators=(',', ':')).encode()
                response.body = new_body
        return response

    @staticmethod
    def example() -> any:
        return {
            "key_path": "required string - key path to value (jsonpath_ng format) eg -> response.items[2].key",
            "value": "required any - new value",
            "if_value": {
                "equal": "optional any - if exist replace only if old value is equal to this",
                "not_equal": "optional any - if exist replace only if old value is not equal to this",
                "greater": "optional number - if exist replace only if old value is greater to this",
                "less": "optional number - if exist replace only if old value is less to this"
            }
        }
