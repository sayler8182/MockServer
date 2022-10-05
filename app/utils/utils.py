import subprocess
import uuid
from os.path import exists
from typing import Iterable
from zipfile import ZipFile

from flask import flash
from werkzeug.datastructures import FileStorage

from app.static.tmp import tmp_file, tmp_directory
from app.static.upload import upload_file


def toast(message: str, category: str = 'message'):
    is_flash_enabled = category == 'error'
    if is_flash_enabled:
        flash(message=message, category=category)


def call(action=None, success=None, error=None) -> bool:
    try:
        safe_call(action)
        safe_call(success)
        return True
    except ValueError as exception:
        toast(str(exception), category='error')
        safe_call(error)
        return False


def call_with_result(action=None, success=None, error=None):
    try:
        result = safe_call_with_result(action)
        safe_call(success)
        return result
    except ValueError as exception:
        toast(str(exception), category='error')
        safe_call(error)
        return None


def safe_call(action):
    if action:
        action()


def safe_call_with_result(action):
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
    if isinstance(value, int):
        return value
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


def get_dict(object):
    if isinstance(object, list):
        return list(map(lambda item: item.get_dict(), object))
    elif object is not None:
        return object.get_dict()
    return None


def chunked_response(response, size: int = 1024) -> Iterable[bytes]:
    for chunk in response.iter_content(size):
        yield chunk


def chunked(value: any, size: int = 1024) -> Iterable[any]:
    if not None:
        yield value
    return None


def store_file_in_tmp(file: FileStorage) -> str:
    file_id = new_id()
    file_extension = last(file.filename.split('.'))
    file_name = f'{file_id}.{file_extension}'
    file_path = tmp_file(file_name)
    file.save(file_path)
    return file_path


def store_file_in_upload(file: FileStorage) -> str:
    file_id = new_id()
    file_extension = last(file.filename.split('.'))
    file_name = f'{file_id}.{file_extension}'
    file_path = upload_file(file_name)
    file.save(file_path)
    return file_path


def unzip_file_in_tmp(file_path: str) -> str:
    directory_name = new_id()
    directory_path = tmp_directory(directory_name)
    with ZipFile(file_path, 'r') as file_zip:
        file_zip.extractall(path=directory_path)
    return directory_path


def open_directory(file_path: str) -> bool:
    if exists(file_path):
        directory = file_path[:file_path.rfind('/')]
        command = f'open "{directory}"'
        print(command)
        subprocess.call(command, shell=True)
        return True
    return False


def read_file(file_path: str) -> str:
    file = open(file_path)
    file.seek(0)
    content = file.read()
    file.close()
    return content


def to_list(object: any) -> [any]:
    if object is None:
        return []
    if isinstance(object, list):
        return object
    return [object]


def to_binary(object: any) -> [bytes]:
    if isinstance(object, str):
        return object.encode()
    return object


def clean_nones(value):
    if isinstance(value, list):
        return [clean_nones(x) for x in value if x is not None]
    elif isinstance(value, dict):
        return {
            key: clean_nones(val)
            for key, val in value.items()
            if val is not None
        }
    else:
        return value
