from enum import Enum


class HTTPMethod(Enum):
    GET = 'GET'
    POST = 'POST'
    DELETE = 'DELETE'
    PUT = 'PUT'
    PATCH = 'PATCH'

    @staticmethod
    def supported_methods():
        return [
            HTTPMethod.GET,
            HTTPMethod.POST,
            HTTPMethod.DELETE,
            HTTPMethod.PUT,
            HTTPMethod.PATCH
        ]

    def get_dict(self):
        return self.value
