from app.adapters.proxy_adapter import ProxyAdapter
from app.core.template_manager import TemplateManager
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.mock_response_interceptor import MockResponseInterceptor
from app.models.models.proxy_request import ProxyRequest
from app.models.models.proxy_response import ProxyResponse
from app.utils.utils import to_binary


class ResponseTemplatingInterceptor(object):
    def intercept(self, request: ProxyRequest, response: ProxyResponse, mock: Mock, mock_response: MockResponse,
                  interceptor: MockResponseInterceptor):
        if response and response.body:
            proxy = ProxyAdapter.get_proxy_selected()
            if proxy.is_enabled and not proxy.is_templating_enabled:
                body = to_binary(response.body)
                body = body.decode()
                template_manager = TemplateManager(request=request, response=response, mock=mock,
                                                   mock_response=mock_response, interceptor=interceptor)
                body = template_manager.apply_templating(body)
                response.body = body.encode()
                response.headers['Content-Length'] = len(response.body)
        return response

    @staticmethod
    def is_configurable() -> any:
        return False

    @staticmethod
    def example() -> any:
        return None
