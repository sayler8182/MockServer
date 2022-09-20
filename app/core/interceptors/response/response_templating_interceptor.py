from app.core.template_manager import TemplateManager
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.mock_response_interceptor import MockResponseInterceptor


class ResponseTemplatingInterceptor(object):
    def intercept(self, response, mock: Mock, mock_response: MockResponse, interceptor: MockResponseInterceptor):
        if response and response.body:
            body = response.body.decode()
            template_manager = TemplateManager()
            body = template_manager.apply_templating(body)
            response.body = body.encode()
        return response

    @staticmethod
    def is_configurable() -> any:
        return False

    @staticmethod
    def example() -> any:
        return None
