import datetime
import re

from app.utils.utils import safe_call_with_result_and_params, to_int


def add(date: datetime, shift: str, shift_direction: int) -> datetime:
    components = get_components(shift=shift)
    for component in components.items():
        date = add_component(date=date, component=component, shift_direction=shift_direction)
    return date


def add_component(date: datetime, component: tuple, shift_direction: int):
    key, value = component
    action = {
        "s": lambda x: datetime.timedelta(seconds=x),
        "m": lambda x: datetime.timedelta(minutes=x),
        "h": lambda x: datetime.timedelta(hours=x),
        "d": lambda x: datetime.timedelta(days=x),
    }.get(key)
    value = value * (-1 if shift_direction < 0 else 1)
    date = date + safe_call_with_result_and_params(action, value)
    return date


def get_components(shift: str) -> dict:
    result = {}
    regex = r"([0-9]+)([a-z]+)"
    components = shift.split(" ")
    for component in components:
        match = re.match(regex, component)
        if match:
            groups = match.groups()
            if len(groups) == 2:
                key = groups[1]
                value = to_int(groups[0])
                if key and value:
                    result[key] = value
    return result
