import uuid
from datetime import datetime

from app.models.models.environment_static_key import EnvironmentStaticKey
from app.utils import utils_date
from app.utils.utils import safe_call_with_result_and_params, to_int


def get_value_for_static(key: str, parameters: str, separator: str) -> str:
    parameters = get_parameters(parameters, separator)
    value = {
        EnvironmentStaticKey.date.description: __get_date,
        EnvironmentStaticKey.uuid.description: __get_uuid
    }.get(key.upper())
    return safe_call_with_result_and_params(value, parameters)


def get_parameters(parameters: str, separator: str) -> any:
    parameters = parameters.split(separator)
    parameters = dict(map(lambda item: get_parameter(item), parameters))
    return parameters


def get_parameter(item: str) -> tuple[str, str]:
    head, sep, tail = item.partition("=")
    return head, tail


# values
def __get_date(parameters: dict) -> str:
    date_format = parameters.get("format", None)
    shift = parameters.get("shift", None)
    shift_direction = parameters.get("shift_direction", 1)
    shift_direction = to_int(shift_direction)
    date = datetime.now()
    date = utils_date.add(date=date, shift=shift, shift_direction=shift_direction)
    if date_format:
        return date.strftime(date_format)
    return date.isoformat()


def __get_uuid(parameters: dict) -> str:
    return str(uuid.uuid4())
