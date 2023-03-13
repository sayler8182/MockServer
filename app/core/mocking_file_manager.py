import os
from os.path import exists

import validators
from flask import send_file, abort

from app.adapters.proxy_adapter import ProxyAdapter
from app.core.interceptors.response_interceptor import ResponseInterceptor
from app.core.interceptors.shared_response.response_delay_interceptor import ResponseDelayInterceptor
from app.core.interceptors.shared_response.response_headers_interceptor import ResponseHeadersInterceptor
from app.core.interceptors.shared_response.response_remove_response_id_interceptor import \
    ResponseRemoveResponseIdInterceptor
from app.core.interceptors.shared_response.response_settings_headers_interceptor import \
    ResponseSettingsHeadersInterceptor
from app.core.interceptors.shared_response.response_single_use_interceptor import ResponseSingleUseInterceptor
from app.core.interceptors.shared_response.response_store_log_interceptor import ResponseStoreLogInterceptor
from app.core.interceptors.shared_response_interceptor import SharedResponseInterceptor
from app.models.models.http_method import HTTPMethod
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.proxy_request import ProxyRequest
from app.models.models.proxy_response import ProxyResponse, ProxyResponseType
from app.utils.env import Env


class MockingFileManager(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app
        self.shared_response_interceptor = SharedResponseInterceptor([
            ResponseSingleUseInterceptor(),
            ResponseDelayInterceptor(),
            ResponseSettingsHeadersInterceptor(),
            ResponseHeadersInterceptor(),
            ResponseRemoveResponseIdInterceptor(),
            ResponseStoreLogInterceptor()
        ])
        self.response_interceptor = ResponseInterceptor()

    def response(self, request, mock: Mock, mock_response: MockResponse, path: str):
        file_response = None
        return_path = None
        if mock_response.body_path:
            # absolute or relative
            return_path = mock_response.body_path
            if exists(return_path):
                file_response = send_file(return_path)
            else:
                root_directory = os.getcwd()
                resources = Env.MOCK_SERVER_RESOURCES
                return_path = f'{root_directory}{resources}{mock_response.body_path}'
                if exists(return_path):
                    file_response = send_file(return_path)

        if file_response and return_path:
            request = self.__prepare_request(request, path)
            response = self.__prepare_response(request, file_response, return_path)
            response = self.shared_response_interceptor.intercept(request, response, mock, mock_response)
            response = self.response_interceptor.intercept(request, response, mock, mock_response)
            return response.response
        return abort(404)

    def __prepare_request(self, request, path: str) -> ProxyRequest:
        proxy = ProxyAdapter.get_proxy_selected()
        proxy_path = proxy.path or ''
        path = path or ''
        url = proxy_path + path
        if not validators.url(url):
            return None
        return ProxyRequest(method=HTTPMethod[request.method],
                            url=url,
                            params=request.args,
                            data=request.get_data(),
                            headers=dict(request.headers),
                            json=request.get_json(silent=True))

    def __prepare_response(self, request, response, path: str) -> ProxyResponse:
        return ProxyResponse(request=request,
                             response=response,
                             type=ProxyResponseType.file,
                             status_code=response.status_code,
                             headers=dict(response.headers),
                             body=path)
