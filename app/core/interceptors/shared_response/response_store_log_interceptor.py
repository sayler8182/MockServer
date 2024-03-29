from base64 import b64encode

from app.adapters.mock_response_log_adapter import MockResponseLogAdapter
from app.adapters.proxy_adapter import ProxyAdapter
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.mock_response_log import MockResponseLog, MockResponseLogData, MockResponseLogDataRequest
from app.models.models.mock_response_type import MockResponseType
from app.models.models.proxy import Proxy
from app.models.models.proxy_request import ProxyRequest
from app.models.models.proxy_response import ProxyResponse, ProxyResponseType


class ResponseStoreLogInterceptor(object):
    def intercept(self, request: ProxyRequest, response: ProxyResponse, mock: Mock,
                  mock_response: MockResponse) -> ProxyResponse:
        mock_id = mock.id if mock else None
        response_id = mock_response.id if mock_response else None
        data_request = self.__log_data_request(request)
        data = self.__log_data(response, mock, mock_response)
        log = MockResponseLog(mock_id=mock_id,
                              response_id=response_id,
                              data_request=data_request,
                              data=data)
        MockResponseLogAdapter.add_log(log)
        return response

    def __log_data_request(self, request: ProxyRequest) -> MockResponseLogDataRequest:
        return MockResponseLogDataRequest(method=request.method,
                                          url=request.url,
                                          params=request.params,
                                          data=request.data,
                                          headers=request.headers,
                                          json=request.json)

    def __log_data(self, response: ProxyResponse, mock: Mock, mock_response: MockResponse) -> MockResponseLogData:
        proxy = ProxyAdapter.get_proxy_selected()
        if response and mock and mock_response:
            value = {
                MockResponseType.mock_json: lambda: self.__log_data_for_mock_json(proxy, response, mock, mock_response),
                MockResponseType.mock_file: lambda: self.__log_data_for_mock_file(proxy, response, mock, mock_response),
                MockResponseType.mock_script: lambda: self.__log_data_for_mock_script(proxy, response, mock, mock_response),
                MockResponseType.proxy: lambda: self.__log_data_for_proxy(proxy, response, mock, mock_response)
            }.get(mock_response.type)
            return value()
        return self.__log_data_for_proxy(proxy, response, mock, mock_response)

    def __log_data_for_mock_json(self, proxy: Proxy, response: ProxyResponse, mock: Mock,
                                 mock_response: MockResponse) -> MockResponseLogData:
        body = b64encode(response.body).decode() if response.body else None
        return MockResponseLogData(type=ProxyResponseType.json,
                                   mock_name=mock.description,
                                   method=mock.request.method,
                                   proxy=proxy.path,
                                   path=mock.request.path,
                                   is_single_use=mock_response.is_single_use,
                                   response_type=mock_response.type,
                                   response_name=mock_response.description,
                                   status_code=mock_response.status,
                                   delay_mode=mock_response.delay_mode,
                                   delay_from=mock_response.delay_from,
                                   delay_to=mock_response.delay_to,
                                   delay=mock_response.delay,
                                   body=body,
                                   body_path=None,
                                   body_script=None)

    def __log_data_for_mock_file(self, proxy: Proxy, response: ProxyResponse, mock: Mock,
                                 mock_response: MockResponse) -> MockResponseLogData:
        body = response.body
        return MockResponseLogData(type=ProxyResponseType.file,
                                   mock_name=mock.description,
                                   method=mock.request.method,
                                   proxy=proxy.path,
                                   path=mock.request.path,
                                   is_single_use=mock_response.is_single_use,
                                   response_type=mock_response.type,
                                   response_name=mock_response.description,
                                   status_code=mock_response.status,
                                   delay_mode=mock_response.delay_mode,
                                   delay_from=mock_response.delay_from,
                                   delay_to=mock_response.delay_to,
                                   delay=mock_response.delay,
                                   body=None,
                                   body_path=body,
                                   body_script=None)

    def __log_data_for_mock_script(self, proxy: Proxy, response: ProxyResponse, mock: Mock,
                                   mock_response: MockResponse) -> MockResponseLogData:
        body = response.body
        return MockResponseLogData(type=ProxyResponseType.file,
                                   mock_name=mock.description,
                                   method=mock.request.method,
                                   proxy=proxy.path,
                                   path=mock.request.path,
                                   is_single_use=mock_response.is_single_use,
                                   response_type=mock_response.type,
                                   response_name=mock_response.description,
                                   status_code=mock_response.status,
                                   delay_mode=mock_response.delay_mode,
                                   delay_from=mock_response.delay_from,
                                   delay_to=mock_response.delay_to,
                                   delay=mock_response.delay,
                                   body=body,
                                   body_path=None,
                                   body_script=None)

    def __log_data_for_proxy(self, proxy: Proxy, response: ProxyResponse, mock: Mock,
                             mock_response: MockResponse) -> MockResponseLogData:
        if mock and mock_response:
            body = b64encode(response.body).decode()
            return MockResponseLogData(type=ProxyResponseType.proxy,
                                       mock_name=mock.description,
                                       method=mock.request.method,
                                       proxy=proxy.path,
                                       path=mock.request.path,
                                       is_single_use=mock_response.is_single_use,
                                       response_type=mock_response.type,
                                       response_name=mock_response.description,
                                       status_code=mock_response.status,
                                       delay_mode=mock_response.delay_mode,
                                       delay_from=mock_response.delay_from,
                                       delay_to=mock_response.delay_to,
                                       delay=mock_response.delay,
                                       body=body,
                                       body_path=None,
                                       body_script=None)
        return MockResponseLogData(type=ProxyResponseType.proxy,
                                   method=response.request.method,
                                   path=response.request.url)
