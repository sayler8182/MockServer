import uuid
from typing import Iterable

from flask import flash
from werkzeug.datastructures import FileStorage

from app.static.tmp import tmp_file


def toast(message: str, category: str = 'message'):
    is_flash_enabled = category == 'error'
    if is_flash_enabled:
        flash(message=message, category=category)


def call(action=None, success=None, error=None) -> bool:
    try:
        save_call(action)
        save_call(success)
        return True
    except ValueError as exception:
        toast(str(exception), category='error')
        save_call(error)
        return False


def call_with_result(action=None, success=None, error=None):
    try:
        result = save_call_with_result(action)
        save_call(success)
        return result
    except ValueError as exception:
        toast(str(exception), category='error')
        save_call(error)
        return None


def save_call(action):
    if action:
        action()


def save_call_with_result(action):
    if action:
        return action()
    return None


def to_bool(value: any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        values = ['true', '1', 't', 'y', 'yes']
        return value.lower() in values
    return False


def to_int(value: any) -> int:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, str):
        return int(value)
    return None


def conditional_value(condition: bool, if_value: any, else_value: any = '') -> any:
    if condition:
        return if_value
    return else_value


def new_id():
    return str(uuid.uuid4().hex)


def first(array):
    if array:
        return array[0]
    return None


def last(array):
    if array:
        length = len(array)
        return array[length - 1]
    return None


def get_dict(array):
    return list(map(lambda item: item.get_dict(), array))


def chunked_response(response, size: int = 1024) -> Iterable[bytes]:
    for chunk in response.iter_content(size):
        yield chunk


def chunked_string(string: str, size: int = 1024) -> Iterable[str]:
    if not None:
        yield string
    return None


def store_file_in_tmp(file: FileStorage) -> str:
    file_name = new_id()
    file_path = tmp_file(file_name)
    file.save(file_path)
    return file_path


def read_file(file_path: str) -> str:
    file = open(file_path)
    file.seek(0)
    content = file.read()
    file.close()
    return content
