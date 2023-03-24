import json
import os
from os.path import exists

import validators
from flask import abort

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
from app.core.interceptors.shared_response.response_templating_interceptor import ResponseTemplatingInterceptor
from app.core.interceptors.shared_response_interceptor import SharedResponseInterceptor
from app.models.models.http_method import HTTPMethod
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.proxy_request import ProxyRequest
from app.models.models.proxy_response import ProxyResponse, ProxyResponseType
from app.utils.env import Env
from app.utils.utils_api import response_dumps, response_dumps_string


class MockingScriptManager(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app
        self.shared_response_interceptor = SharedResponseInterceptor([
            ResponseSingleUseInterceptor(),
            ResponseDelayInterceptor(),
            ResponseSettingsHeadersInterceptor(),
            ResponseHeadersInterceptor(),
            ResponseTemplatingInterceptor(),
            ResponseRemoveResponseIdInterceptor(),
            ResponseStoreLogInterceptor()
        ])
        self.response_interceptor = ResponseInterceptor()

    def response(self, request, mock: Mock, mock_response: MockResponse, path: str):
        script_path = None
        return_path = None
        if mock_response.body_script:
            # absolute or relative
            return_path = mock_response.body_script
            if exists(return_path):
                script_path = return_path
            else:
                root_directory = os.getcwd()
                resources = Env.MOCK_SERVER_RESOURCES
                return_path = f'{root_directory}{resources}{mock_response.body_script}'
                if exists(return_path):
                    script_path = return_path

        if script_path and return_path:
            request = self.__prepare_request(request, path)
            script_response = self.__execute(request, mock, mock_response, return_path)
            response = self.__prepare_response(request, mock_response, script_response)
            response = self.shared_response_interceptor.intercept(request, response, mock, mock_response)
            response = self.response_interceptor.intercept(request, response, mock, mock_response)
            return response_dumps(self.flask_app, response)
        return abort(404)

    def __execute(self, request: ProxyRequest, mock: Mock, mock_response: MockResponse, file_path: str) -> any:
        with open(file_path, "r") as file:
            code = file.read()
            params = {
                'request': request,
                'mock': mock,
                'mock_response': mock_response,
                'result': {}
            }
            exec(code, params)
            return self.__map_script_result(params['result']['body'])

    def __map_script_result(self, result: any) -> any:
        if isinstance(result, str):
            return result
        if isinstance(result, dict):
            return json.dumps(result)
        if isinstance(result, list):
            return json.dumps(result)
        return ''

    def __prepare_request(self, request, path: str) -> ProxyRequest:
        proxy = ProxyAdapter.get_proxy_selected()
        proxy_path = proxy.path or ''
        path = path or ''
        url = proxy_path + path
        if not validators.url(url):
            return None
        return ProxyRequest(method=HTTPMethod[request.method],
                            url=url,
                            params=request.args.to_dict(flat=False),
                            data=request.get_data().decode(),
                            headers=dict(request.headers),
                            json=request.get_json(silent=True))

    def __prepare_response(self, request: ProxyRequest, mock_response: MockResponse, body: str) -> ProxyResponse:
        status_code = mock_response.status
        response = response_dumps_string(self.flask_app, status=status_code, object=body)
        headers = dict(map(lambda item: (item.name, item.value), mock_response.response_headers))
        return ProxyResponse(request=request,
                             response=response,
                             type=ProxyResponseType.json,
                             status_code=response.status_code,
                             headers=headers,
                             body=body)
