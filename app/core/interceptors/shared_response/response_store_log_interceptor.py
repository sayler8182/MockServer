from base64 import b64encode

from app.adapters.mock_response_log_adapter import MockResponseLogAdapter
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.mock_response_log import MockResponseLog, MockResponseLogData
from app.models.models.mock_response_type import MockResponseType
from app.models.models.proxy_request import ProxyRequest
from app.models.models.proxy_response import ProxyResponse, ProxyResponseType


class ResponseStoreLogInterceptor(object):
    def intercept(self, request: ProxyRequest, response: ProxyResponse, mock: Mock,
                  mock_response: MockResponse) -> ProxyResponse:
        mock_id = mock.id if mock else None
        response_id = mock_response.id if mock_response else None
        data = self.__log_data(response, mock, mock_response)
        log = MockResponseLog(mock_id=mock_id,
                              response_id=response_id,
                              data=data)
        MockResponseLogAdapter.add_log(log)
        return response

    def __log_data(self, response: ProxyResponse, mock: Mock, mock_response: MockResponse) -> MockResponseLogData:
        if response and mock and mock_response:
            value = {
                MockResponseType.mock_json: lambda: self.__log_data_for_mock_json(response, mock, mock_response),
                MockResponseType.mock_file: lambda: self.__log_data_for_mock_file(response, mock, mock_response),
                MockResponseType.proxy: lambda: self.__log_data_for_proxy(response, mock, mock_response)
            }.get(mock_response.type)
            return value()
        return self.__log_data_for_proxy(response, mock, mock_response)

    def __log_data_for_mock_json(self, response: ProxyResponse, mock: Mock,
                                 mock_response: MockResponse) -> MockResponseLogData:
        body = b64encode(response.body).decode() if response.body else None
        return MockResponseLogData(type=ProxyResponseType.json,
                                   mock_name=mock.description,
                                   method=mock.request.method,
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
                                   body_path=None)

    def __log_data_for_mock_file(self, response: ProxyResponse, mock: Mock,
                                 mock_response: MockResponse) -> MockResponseLogData:
        body = response.body
        return MockResponseLogData(type=ProxyResponseType.file,
                                   mock_name=mock.description,
                                   method=mock.request.method,
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
                                   body_path=body)

    def __log_data_for_proxy(self, response: ProxyResponse, mock: Mock,
                             mock_response: MockResponse) -> MockResponseLogData:
        if mock and mock_response:
            body = b64encode(response.body).decode()
            return MockResponseLogData(type=ProxyResponseType.proxy,
                                       mock_name=mock.description,
                                       method=mock.request.method,
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
                                       body_path=None)
        return MockResponseLogData(type=ProxyResponseType.proxy,
                                   method=response.request.method,
                                   path=response.request.url)
