from enum import Enum


class EnvironmentStaticKey(Enum):
    date = 'date'
    env = 'env'
    request_body = 'request.body'
    request_header = 'request.header'
    request_headers = 'request.headers'
    request_method = 'request.method'
    request_param = 'request.param'
    request_params = 'request.params'
    request_url = 'request.url'
    uuid = 'uuid'

    @staticmethod
    def available_keys():
        return [
            EnvironmentStaticKey.date,
            EnvironmentStaticKey.env,
            EnvironmentStaticKey.request_body,
            EnvironmentStaticKey.request_header,
            EnvironmentStaticKey.request_headers,
            EnvironmentStaticKey.request_method,
            EnvironmentStaticKey.request_param,
            EnvironmentStaticKey.request_params,
            EnvironmentStaticKey.request_url,
            EnvironmentStaticKey.uuid
        ]

    @property
    def description(self) -> str:
        return f'{self.value}'.upper()

    @property
    def comment(self) -> str:
        return {
            EnvironmentStaticKey.date: "Current date in ISO format",
            EnvironmentStaticKey.env: "Environment variable",
            EnvironmentStaticKey.request_body: "Body from request",
            EnvironmentStaticKey.request_header: "Header from request",
            EnvironmentStaticKey.request_headers: "Headers from request",
            EnvironmentStaticKey.request_method: "Method from request",
            EnvironmentStaticKey.request_param: "Parameter from request form and url matching params",
            EnvironmentStaticKey.request_params: "Parameters from request form and url matching params",
            EnvironmentStaticKey.request_url: "URL from request",
            EnvironmentStaticKey.uuid: "Random uuid4",
        }.get(self)

    @property
    def parameters(self) -> dict:
        return {
            EnvironmentStaticKey.date: {
                "format": "Date format (in python style)",
                "shift": "shift between current date, separated with space: 1d 13h 2m 11s",
                "shift_direction": "shift direction 1 or -1 (add or subtract date)"
            },
            EnvironmentStaticKey.env: {
                "name": "Variable name",
            },
            EnvironmentStaticKey.request_body: {},
            EnvironmentStaticKey.request_header: {
                "name": "Header name",
                "type": "Cast to type (in python style)"
            },
            EnvironmentStaticKey.request_headers: {},
            EnvironmentStaticKey.request_method: {},
            EnvironmentStaticKey.request_param: {
                "name": "Parameter name",
                "type": "Cast to type (in python style)"
            },
            EnvironmentStaticKey.request_params: {},
            EnvironmentStaticKey.request_url: {},
            EnvironmentStaticKey.uuid: {}
        }.get(self)
