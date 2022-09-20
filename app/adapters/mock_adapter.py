from app.adapters.request_header_adapter import RequestHeaderAdapter
from app.config.database_config import db
from app.models.db.mock_db import MockDb
from app.models.db.mock_request_db import MockRequestDb
from app.models.db.mock_response_db import MockResponseDb
from app.models.db.mock_response_interceptor_db import MockResponseInterceptorDb
from app.models.db.request_header_db import RequestHeaderDb
from app.models.models.delay_mode import DelayMode
from app.models.models.http_method import HTTPMethod
from app.models.models.mock import Mock, MockMethod
from app.models.models.mock_request import MockRequest
from app.models.models.mock_response import MockResponse
from app.models.models.mock_response_interceptor import MockResponseInterceptor
from app.models.models.mock_response_interceptor_type import MockResponseInterceptorType
from app.models.models.mock_response_type import MockResponseType
from app.models.models.request_header import RequestHeaderType


class MockAdapter(object):
    @staticmethod
    def get_mocks() -> [Mock]:
        query = MockDb.query.all()
        return list(map(lambda item: MockAdapter.mock_from_entity(item), query))

    @staticmethod
    def get_mock(id: str) -> Mock:
        query = MockDb.query.filter_by(id=id).first()
        return MockAdapter.mock_from_entity(query)

    @staticmethod
    def get_mock_request(id: str) -> MockRequest:
        query = MockRequestDb.query.filter_by(id=id).first()
        return MockAdapter.mock_request_from_entity(query)

    @staticmethod
    def get_mock_request_for_mock(mock_id: str) -> MockRequest:
        query = MockRequestDb.query.filter_by(mock_id=mock_id).first()
        return MockAdapter.mock_request_from_entity(query)

    @staticmethod
    def get_mock_response(mock_id: str, id: str) -> MockResponse:
        query = MockResponseDb.query.filter_by(mock_id=mock_id, id=id).first()
        return MockAdapter.mock_response_from_entity(query)

    @staticmethod
    def get_mock_responses(response_ids: [str]) -> [MockResponse]:
        query = MockResponseDb.query.filter(MockResponseDb.id.in_(response_ids)).order_by(
            MockResponseDb.order.asc()).all()
        return list(map(lambda item: MockAdapter.mock_response_from_entity(item), query))

    @staticmethod
    def get_mock_responses_for_mock(mock_id: str) -> [MockResponse]:
        query = MockResponseDb.query.filter_by(mock_id=mock_id).order_by(MockResponseDb.order.asc()).all()
        return list(map(lambda item: MockAdapter.mock_response_from_entity(item), query))

    @staticmethod
    def get_mock_response_interceptor(mock_id: str, response_id: str, id: str) -> MockResponseInterceptor:
        query = MockResponseInterceptorDb.query.filter_by(mock_id=mock_id, response_id=response_id, id=id).first()
        return MockAdapter.mock_response_interceptor_from_entity(query)

    @staticmethod
    def get_response_interceptors_for_mock_response(mock_id: str, response_id: str) -> [MockResponseInterceptor]:
        query = MockResponseInterceptorDb.query.filter_by(mock_id=mock_id, response_id=response_id).all()
        return list(map(lambda item: MockAdapter.mock_response_interceptor_from_entity(item), query))

    @staticmethod
    def add_mock(mock: Mock, commit: bool = True):
        entity = MockAdapter.mock_from_object(mock)
        db.session.merge(entity)
        MockAdapter.add_mock_request(mock.request, commit=False)
        MockAdapter.add_mock_responses(mock.responses, commit=False)
        if commit:
            db.session.commit()

    @staticmethod
    def add_mock_request(mock_request: MockRequest, commit: bool = True):
        entity = MockAdapter.mock_request_from_object(mock_request)
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def add_mock_response(mock_response: MockResponse, commit: bool = True):
        entity = MockAdapter.mock_response_from_object(mock_response)
        MockAdapter.add_mock_response_interceptors(mock_response.response_interceptors, commit=False)
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def add_mock_responses(mock_responses: [MockResponse], commit: bool = True):
        for mock_response in mock_responses:
            MockAdapter.add_mock_response(mock_response, False)
        if commit:
            db.session.commit()

    @staticmethod
    def add_mock_response_interceptor(mock_response_interceptor: MockResponseInterceptor, commit: bool = True):
        entity = MockAdapter.mock_response_interceptor_from_object(mock_response_interceptor)
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def add_mock_response_interceptors(mock_response_interceptors: [MockResponseInterceptor], commit: bool = True):
        for mock_response_interceptor in mock_response_interceptors:
            MockAdapter.add_mock_response_interceptor(mock_response_interceptor, False)
        if commit:
            db.session.commit()

    @staticmethod
    def remove_all(commit: bool = True):
        MockDb.query.delete()
        MockRequestDb.query.filter_by().delete()
        MockResponseDb.query.filter_by().delete()
        RequestHeaderDb.query.filter_by(type=RequestHeaderType.mock_request.value).delete()
        RequestHeaderDb.query.filter_by(type=RequestHeaderType.mock_response.value).delete()
        MockResponseInterceptorDb.query.filter_by().delete()
        if commit:
            db.session.commit()

    @staticmethod
    def remove_mock(mock_id: str, commit: bool = True):
        MockDb.query.filter_by(id=mock_id).delete()
        MockRequestDb.query.filter_by(mock_id=mock_id).delete()
        MockResponseDb.query.filter_by(mock_id=mock_id).delete()
        RequestHeaderDb.query.filter_by(mock_id=mock_id).delete()
        MockResponseInterceptorDb.query.filter_by(mock_id=mock_id).delete()
        if commit:
            db.session.commit()

    @staticmethod
    def remove_mock_response(mock_id: str, response_id: str, commit: bool = True):
        MockResponseDb.query.filter_by(mock_id=mock_id, id=response_id).delete()
        RequestHeaderDb.query.filter_by(mock_id=mock_id, response_id=response_id).delete()
        MockResponseInterceptorDb.query.filter_by(mock_id=mock_id, response_id=response_id).delete()
        if commit:
            db.session.commit()

    @staticmethod
    def remove_mock_response_interceptor(interceptor_id: str, commit: bool = True):
        MockResponseInterceptorDb.query.filter_by(id=interceptor_id).delete()
        if commit:
            db.session.commit()

    @staticmethod
    def set_mock_enable(mock_id: str, commit: bool = True):
        mock = MockAdapter.get_mock(mock_id)
        entity = MockAdapter.mock_from_object(mock)
        entity.is_enabled = True
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_mock_disable(mock_id: str, commit: bool = True):
        mock = MockAdapter.get_mock(mock_id)
        entity = MockAdapter.mock_from_object(mock)
        entity.is_enabled = False
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_mock(mock_id: str, name: str, commit: bool = True):
        mock = MockAdapter.get_mock(mock_id)
        entity = MockAdapter.mock_from_object(mock)
        entity.name = name
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_mock_method(mock_id: str, method: MockMethod, commit: bool = True):
        mock = MockAdapter.get_mock(mock_id)
        entity = MockAdapter.mock_from_object(mock)
        entity.method = method.value
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_mock_request(mock_id: str, method: HTTPMethod, path: str, commit: bool = True):
        mock = MockAdapter.get_mock(mock_id)
        request = MockAdapter.get_mock_request(mock.request.id)
        entity = MockAdapter.mock_request_from_object(request)
        entity.method = method.value
        entity.path = path
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_mock_response_enable(mock_id: str, response_id: str, commit: bool = True):
        response = MockAdapter.get_mock_response(mock_id, response_id)
        entity = MockAdapter.mock_response_from_object(response)
        entity.is_enabled = True
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_mock_response_disable(mock_id: str, response_id: str, commit: bool = True):
        response = MockAdapter.get_mock_response(mock_id, response_id)
        entity = MockAdapter.mock_response_from_object(response)
        entity.is_enabled = False
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_mock_response_set(mock_id: str, response_id: str, commit: bool = True):
        mock = MockAdapter.get_mock(mock_id)
        entity = MockAdapter.mock_from_object(mock)
        entity.response_id = response_id
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_mock_response_unset(mock_id: str, commit: bool = True):
        mock = MockAdapter.get_mock(mock_id)
        entity = MockAdapter.mock_from_object(mock)
        entity.response_id = None
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_mock_response(mock_id: str, response_id: str, name: str, commit: bool = True):
        response = MockAdapter.get_mock_response(mock_id, response_id)
        entity = MockAdapter.mock_response_from_object(response)
        entity.name = name
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_mock_response_order(mock_id: str, response_id: str, order: int, commit: bool = True):
        response = MockAdapter.get_mock_response(mock_id, response_id)
        entity = MockAdapter.mock_response_from_object(response)
        entity.order = order
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_mock_response_type(mock_id: str, response_id: str, type: MockResponseType, commit: bool = True):
        response = MockAdapter.get_mock_response(mock_id, response_id)
        entity = MockAdapter.mock_response_from_object(response)
        entity.type = type.value
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_mock_response_status(mock_id: str, response_id: str, status: int, commit: bool = True):
        response = MockAdapter.get_mock_response(mock_id, response_id)
        entity = MockAdapter.mock_response_from_object(response)
        entity.status = status
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_mock_response_body(mock_id: str, response_id: str, body: str, commit: bool = True):
        response = MockAdapter.get_mock_response(mock_id, response_id)
        entity = MockAdapter.mock_response_from_object(response)
        entity.body = body
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_mock_response_interceptor(mock_id: str, response_id: str, interceptor_id: str, name: str,
                                      commit: bool = True):
        interceptor = MockAdapter.get_mock_response_interceptor(mock_id, response_id, interceptor_id)
        entity = MockAdapter.mock_response_interceptor_from_object(interceptor)
        entity.name = name
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_mock_response_interceptor_configuration(mock_id: str, response_id: str, interceptor_id: str,
                                                    configuration: str, commit: bool = True):
        interceptor = MockAdapter.get_mock_response_interceptor(mock_id, response_id, interceptor_id)
        entity = MockAdapter.mock_response_interceptor_from_object(interceptor)
        entity.configuration = configuration
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_mock_response_interceptor_enable(mock_id: str, response_id: str, interceptor_id: str, commit: bool = True):
        interceptor = MockAdapter.get_mock_response_interceptor(mock_id, response_id, interceptor_id)
        entity = MockAdapter.mock_response_interceptor_from_object(interceptor)
        entity.is_enabled = True
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def set_mock_response_interceptor_disable(mock_id: str, response_id: str, interceptor_id: str, commit: bool = True):
        interceptor = MockAdapter.get_mock_response_interceptor(mock_id, response_id, interceptor_id)
        entity = MockAdapter.mock_response_interceptor_from_object(interceptor)
        entity.is_enabled = False
        db.session.merge(entity)
        if commit:
            db.session.commit()

    # mappers
    @staticmethod
    def mock_from_object(object: Mock) -> MockDb:
        if object:
            return MockDb(id=object.id,
                          scenario_id=object.scenario_id,
                          name=object.name,
                          is_enabled=object.is_enabled,
                          method=object.method.value,
                          response_id=object.response_id)
        return None

    @staticmethod
    def mock_from_entity(entity: MockDb) -> Mock:
        if entity:
            request = MockAdapter.get_mock_request_for_mock(entity.id)
            responses = MockAdapter.get_mock_responses_for_mock(entity.id)
            return Mock(id=entity.id,
                        scenario_id=entity.scenario_id,
                        is_enabled=entity.is_enabled,
                        name=entity.name,
                        method=MockMethod[entity.method],
                        response_id=entity.response_id,
                        request=request,
                        responses=responses)
        return None

    @staticmethod
    def mock_request_from_object(object: MockRequest) -> MockRequestDb:
        if object:
            return MockRequestDb(mock_id=object.mock_id,
                                 id=object.id,
                                 method=object.method.value,
                                 proxy=object.proxy,
                                 path=object.path)
        return None

    @staticmethod
    def mock_request_from_entity(entity: MockRequestDb) -> MockRequest:
        if entity:
            request_headers = RequestHeaderAdapter.get_request_headers_for_mock_request(entity.mock_id, entity.id,
                                                                                        RequestHeaderType.mock_request)
            return MockRequest(mock_id=entity.mock_id,
                               id=entity.id,
                               method=HTTPMethod[entity.method],
                               proxy=entity.proxy,
                               path=entity.path,
                               request_headers=request_headers)
        return None

    @staticmethod
    def mock_response_from_object(object: MockResponse) -> MockResponseDb:
        if object:
            return MockResponseDb(mock_id=object.mock_id,
                                  id=object.id,
                                  is_enabled=object.is_enabled,
                                  type=object.type.value,
                                  name=object.name,
                                  status=object.status,
                                  delay_mode=object.delay_mode.value,
                                  delay=object.delay,
                                  body=object.body,
                                  order=object.order)
        return None

    @staticmethod
    def mock_response_from_entity(entity: MockResponseDb) -> MockResponse:
        if entity:
            response_headers = RequestHeaderAdapter.get_request_headers_for_mock_response(entity.mock_id, entity.id,
                                                                                          RequestHeaderType.mock_response)
            response_interceptors = MockAdapter.get_response_interceptors_for_mock_response(entity.mock_id, entity.id)
            return MockResponse(mock_id=entity.mock_id,
                                id=entity.id,
                                is_enabled=entity.is_enabled,
                                type=MockResponseType[entity.type],
                                name=entity.name,
                                status=entity.status,
                                delay_mode=DelayMode[entity.delay_mode],
                                delay=entity.delay,
                                body=entity.body,
                                order=entity.order,
                                response_headers=response_headers,
                                response_interceptors=response_interceptors)
        return None

    @staticmethod
    def mock_response_interceptor_from_object(object: MockResponseInterceptor) -> MockResponseInterceptorDb:
        if object:
            return MockResponseInterceptorDb(mock_id=object.mock_id,
                                             response_id=object.response_id,
                                             type=object.type.value,
                                             id=object.id,
                                             is_enabled=object.is_enabled,
                                             name=object.name,
                                             configuration=object.configuration)
        return None

    @staticmethod
    def mock_response_interceptor_from_entity(entity: MockResponseInterceptorDb) -> MockResponseInterceptor:
        if entity:
            return MockResponseInterceptor(mock_id=entity.mock_id,
                                           response_id=entity.response_id,
                                           type=MockResponseInterceptorType[entity.type],
                                           id=entity.id,
                                           is_enabled=entity.is_enabled,
                                           name=entity.name,
                                           configuration=entity.configuration)
        return None
