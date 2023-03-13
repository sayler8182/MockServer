import json

import jsonpath_ng

from app.core.template_manager import TemplateManager
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.mock_response_interceptor import MockResponseInterceptor
from app.models.models.proxy_request import ProxyRequest
from app.models.models.proxy_response import ProxyResponse
from app.utils.utils import to_list, to_binary


class ResponseValueReplaceInterceptor(object):
    def intercept(self, request: ProxyRequest, response: ProxyResponse, mock: Mock, mock_response: MockResponse,
                  interceptor: MockResponseInterceptor):
        if response and response.body and interceptor.configuration:
            body = to_binary(response.body)
            configurations = to_list(json.loads(interceptor.configuration))
            for configuration in configurations:
                key_path = configuration.get('key_path', None)
                value = configuration.get('value', None)
                skip_templating = configuration.get('skip_templating', False)
                object = json.loads(body)
                if object and key_path:
                    expression = jsonpath_ng.parse(key_path)
                    if not skip_templating:
                        template_manager = TemplateManager(request=request, response=response, mock=mock,
                                                           mock_response=mock_response, interceptor=interceptor)
                        value = template_manager.apply_templating(value)
                    if value:
                        data = expression.update_or_create(object, value)
                    else:
                        data = expression.filter(lambda item: True, object)
                    new_body = json.dumps(data, separators=(',', ':'))
                    body = new_body.encode()
            response.body = body
            response.headers['Content-Length'] = len(response.body)
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
                "skip_templating": "optional bool - False if omitted - global templating has to be also disabled"
            }
        ]
