from app.adapters.proxy_adapter import ProxyAdapter
from app.core.template_manager import TemplateManager
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.proxy_request import ProxyRequest
from app.utils.utils import to_binary


class ResponseTemplatingInterceptor(object):
    def intercept(self, request: ProxyRequest, response, mock: Mock, mock_response: MockResponse):
        if response and response.body:
            proxy = ProxyAdapter.get_proxy_selected()
            if proxy.is_enabled and proxy.is_templating_enabled:
                body = to_binary(response.body)
                body = body.decode()
                template_manager = TemplateManager(request=request, response=response, mock=mock,
                                                   mock_response=mock_response)
                body = template_manager.apply_templating(body)
                response.body = body.encode()
        return response
