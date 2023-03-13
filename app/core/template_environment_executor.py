import uuid

from datetime import datetime

from app.core.path_matcher import PathMatcher
from app.models.models.environment_static_key import EnvironmentStaticKey
from app.utils import utils_date
from app.utils.path_components import PathComponents
from app.utils.utils import to_int, to_type, parse_url


def get_value_for_static(manager, key: str, parameters: str, separator: str) -> str:
    parameters = get_parameters(manager, parameters, separator)
    value = {
        EnvironmentStaticKey.date.description: __get_date,
        EnvironmentStaticKey.request_body.description: __get_request_body,
        EnvironmentStaticKey.request_header.description: __get_request_header,
        EnvironmentStaticKey.request_headers.description: __get_request_headers,
        EnvironmentStaticKey.request_method.description: __get_request_method,
        EnvironmentStaticKey.request_param.description: __get_request_param,
        EnvironmentStaticKey.request_params.description: __get_request_params,
        EnvironmentStaticKey.request_url.description: __get_request_url,
        EnvironmentStaticKey.uuid.description: __get_uuid
    }.get(key.upper())
    if value:
        return value(manager, parameters)
    return None


def get_parameters(manager, parameters: str, separator: str) -> any:
    parameters = parameters.split(separator)
    parameters = dict(map(lambda item: get_parameter(item), parameters))
    return parameters


def get_parameter(item: str) -> tuple[str, str]:
    head, sep, tail = item.partition("=")
    return head, tail


# values
def __get_date(manager, parameters: dict) -> str:
    date_format = parameters.get("format", None)
    shift = parameters.get("shift", None)
    shift_direction = parameters.get("shift_direction", 1)
    shift_direction = to_int(shift_direction)
    date = datetime.now()
    date = utils_date.add(date=date, shift=shift, shift_direction=shift_direction)
    if date_format:
        return date.strftime(date_format)
    return date.isoformat()


def __get_request_body(manager, parameters: dict) -> str:
    if manager and manager.request and manager.request.json:
        return manager.request.json
    return None


def __get_request_header(manager, parameters: dict) -> str:
    name = parameters.get("name", None)
    type = parameters.get("type", None)
    if manager and manager.request:
        if manager.request.headers:
            header = manager.request.headers.get(name, None)
            if header is not None:
                header = to_type(header, type)
                return header
    return None


def __get_request_headers(manager, parameters: dict) -> dict:
    if manager and manager.request and manager.request.headers:
        return manager.request.headers
    return None


def __get_request_method(manager, parameters: dict) -> str:
    if manager and manager.request and manager.request.method:
        return manager.request.method.get_dict()
    return None


def __get_request_param(manager, parameters: dict) -> str:
    name = parameters.get("name", None)
    type = parameters.get("type", None)
    if manager and manager.request:
        if manager.request.params:
            param = manager.request.params.get(name, None)
            if param is not None:
                param = to_type(param, type)
                return param

        params = ____get_params(manager) or {}
        param = params.get(name, None)
        if param is not None:
            param = to_type(param, type)
            return param
    return None


def __get_request_params(manager, parameters: dict) -> dict:
    result = {}
    if manager and manager.request and manager.request.params:
        params = manager.request.params
        result.update(params)

    params = ____get_params(manager) or {}
    result.update(params)

    if result:
        return result
    return None


def __get_request_url(manager, parameters: dict) -> str:
    url = None
    if manager and manager.request and manager.request.params:
        url = manager.request.url
    return url


def __get_uuid(manager, parameters: dict) -> str:
    return str(uuid.uuid4())

### UTILS
def ____get_params(manager) -> dict:
    if manager.request.url and manager.mock and manager.mock.request and manager.mock.request.path:
        url = parse_url(manager.request.url)
        pattern = PathComponents(manager.mock.request.path)
        matcher = PathMatcher(pattern, url.path)
        result = matcher.match()
        if result.match and result.parameters:
            return result.parameters
    return None