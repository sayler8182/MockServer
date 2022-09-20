import json

from app.core.interceptors.response.response_custom_interceptor import ResponseCustomInterceptor
from app.core.interceptors.response.response_templating_interceptor import ResponseTemplatingInterceptor
from app.core.interceptors.response.response_update_environment_interceptor import ResponseUpdateEnvironmentInterceptor
from app.core.interceptors.response.response_value_replace_interceptor import ResponseValueReplaceInterceptor
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.mock_response_interceptor import MockResponseInterceptor
from app.models.models.mock_response_interceptor_type import MockResponseInterceptorType


class ResponseInterceptor(object):
    def intercept(self, response, mock: Mock, mock_response: MockResponse):
        for interceptor in mock_response.response_interceptors:
            if interceptor.is_enabled and interceptor.type.is_available(mock_response.type):
                implementation = self.__implementation(interceptor)
                implementation.intercept(response, mock, mock_response, interceptor)
        return response

    def __implementation(self, interceptor: MockResponseInterceptor):
        return {
            MockResponseInterceptorType.custom: ResponseCustomInterceptor(),
            MockResponseInterceptorType.templating: ResponseTemplatingInterceptor(),
            MockResponseInterceptorType.update_environment: ResponseUpdateEnvironmentInterceptor(),
            MockResponseInterceptorType.value_replace: ResponseValueReplaceInterceptor()
        }.get(interceptor.type)

    @staticmethod
    def is_configurable(type: MockResponseInterceptorType) -> bool:
        result = {
            MockResponseInterceptorType.custom: ResponseCustomInterceptor.is_configurable(),
            MockResponseInterceptorType.templating: ResponseTemplatingInterceptor.is_configurable(),
            MockResponseInterceptorType.update_environment: ResponseUpdateEnvironmentInterceptor.is_configurable(),
            MockResponseInterceptorType.value_replace: ResponseValueReplaceInterceptor.is_configurable()
        }.get(type)
        return result

    @staticmethod
    def example(type: MockResponseInterceptorType) -> str:
        object = {
            MockResponseInterceptorType.custom: ResponseCustomInterceptor.example(),
            MockResponseInterceptorType.templating: ResponseTemplatingInterceptor.example(),
            MockResponseInterceptorType.update_environment: ResponseUpdateEnvironmentInterceptor.example(),
            MockResponseInterceptorType.value_replace: ResponseValueReplaceInterceptor.example()
        }.get(type)
        return json.dumps(object)
