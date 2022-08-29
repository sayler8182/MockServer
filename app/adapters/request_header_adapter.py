from app.config.database_config import db
from app.models.db.request_header_db import RequestHeaderDb
from app.models.models.request_header import RequestHeader, RequestHeaderType


class RequestHeaderAdapter(object):
    @staticmethod
    def get_request_headers_for_proxy(proxy_id: str, type: RequestHeaderType) -> [RequestHeader]:
        query = RequestHeaderDb.query.filter_by(proxy_id=proxy_id, type=type.value).all()
        return list(map(lambda item: RequestHeaderAdapter.request_header_from_entity(item), query))

    @staticmethod
    def get_request_headers_for_mock_request(mock_id: str, request_id: str, type: RequestHeaderType) -> [RequestHeader]:
        query = RequestHeaderDb.query.filter_by(mock_id=mock_id, request_id=request_id, type=type.value).all()
        return list(map(lambda item: RequestHeaderAdapter.request_header_from_entity(item), query))

    @staticmethod
    def get_request_headers_for_mock_response(mock_id: str, response_id: str, type: RequestHeaderType) -> [RequestHeader]:
        query = RequestHeaderDb.query.filter_by(mock_id=mock_id, response_id=response_id, type=type.value).all()
        return list(map(lambda item: RequestHeaderAdapter.request_header_from_entity(item), query))

    @staticmethod
    def get_request_header(id: str) -> RequestHeader:
        query = RequestHeaderDb.query.filter_by(id=id).first()
        return RequestHeaderAdapter.request_header_from_entity(query)

    @staticmethod
    def add_request_header(request: RequestHeader, commit: bool = True):
        entity = RequestHeaderAdapter.request_header_from_object(request)
        db.session.merge(entity)
        if commit:
            db.session.commit()

    @staticmethod
    def remove_request_header(id: str, commit: bool = True):
        RequestHeaderDb.query.filter_by(id=id).delete()
        if commit:
            db.session.commit()

    # mappers
    @staticmethod
    def request_header_from_object(object: RequestHeader) -> RequestHeaderDb:
        if object:
            return RequestHeaderDb(id=object.id,
                                   type=object.type.value,
                                   proxy_id=object.proxy_id,
                                   mock_id=object.mock_id,
                                   request_id=object.request_id,
                                   response_id=object.response_id,
                                   name=object.name,
                                   value=object.value)
        return None

    @staticmethod
    def request_header_from_entity(entity: RequestHeaderDb) -> RequestHeader:
        if entity:
            return RequestHeader(id=entity.id,
                                 type=RequestHeaderType[entity.type],
                                 proxy_id=entity.proxy_id,
                                 mock_id=entity.mock_id,
                                 request_id=entity.request_id,
                                 response_id=entity.response_id,
                                 name=entity.name,
                                 value=entity.value)
        return None
