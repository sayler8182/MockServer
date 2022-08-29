import json

from flask import send_from_directory

from app.core.proxy.models.proxy_response import ProxyResponse
from app.static.tmp import tmp_file, tmp_directory
from app.utils.utils import chunked_response, new_id

default_mimetype = 'application/json'


# response_dumps

def response_dumps(flask_app, response: ProxyResponse):
    data = chunked_response(response.response)
    return flask_app.response_class(
        response=data,
        status=response.status_code,
        mimetype=default_mimetype,
        headers=response.headers)


def response_dumps_string(flask_app, status=200, object='', headers={}):
    dictionary = json.loads(object) if object else None
    return response_dumps_dict(
        flask_app=flask_app,
        status=status,
        object=dictionary,
        headers=headers)


def response_dumps_object(flask_app, status=200, object={}, headers={}):
    dictionary = object.get_dict()
    return response_dumps_dict(
        flask_app=flask_app,
        status=status,
        object=dictionary,
        headers=headers)


def response_dumps_dict(flask_app, status=200, object={}, headers={}):
    data = json.dumps(object) if object else None
    return flask_app.response_class(
        response=data,
        status=status,
        mimetype=default_mimetype,
        headers=headers)


def response_dumps_dict_from_tmp_file(object: {}, download_name: str, file_extension: str = 'json'):
    download_name = f'{download_name}.{file_extension}'
    file_name = new_id()
    file_path = tmp_file(file_name)
    with open(file_path, 'x+') as file:
        data = json.dumps(object, indent=4)
        file.write(data)
        file.seek(0)
    return send_from_directory(directory=tmp_directory,
                               path=file_name,
                               as_attachment=True,
                               download_name=download_name,
                               max_age=0)
