import json

from app.core.interceptors.response.mock_response_custom_interceptor import MockResponseCustomInterceptor
from app.core.interceptors.response.mock_response_value_replace_interceptor import MockResponseValueReplaceInterceptor
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.mock_response_interceptor import MockResponseInterceptor
from app.models.models.mock_response_interceptor_type import MockResponseInterceptorType


class ResponseInterceptor(object):
    def intercept(self, response, mock: Mock, mock_response: MockResponse):
        for interceptor in mock_response.response_interceptors:
            implementation = self.__implementation(interceptor)
            implementation.intercept(response, mock, mock_response, interceptor)
        return response

    def __implementation(self, interceptor: MockResponseInterceptor):
        return {
            MockResponseInterceptorType.custom: MockResponseCustomInterceptor(),
            MockResponseInterceptorType.value_replace: MockResponseValueReplaceInterceptor()
        }.get(interceptor.type)

    @staticmethod
    def example(type: MockResponseInterceptorType) -> str:
        object = {
            MockResponseInterceptorType.custom: MockResponseCustomInterceptor.example(),
            MockResponseInterceptorType.value_replace: MockResponseValueReplaceInterceptor.example()
        }.get(type)
        return json.dumps(object)
