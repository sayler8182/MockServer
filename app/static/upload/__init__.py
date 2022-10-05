import os

root_directory = os.getcwd()
upload_root_directory = f'{root_directory}/app/static/upload/files'


def upload_file(file_name: str) -> str:
    return f'{upload_root_directory}/{file_name}'


def upload_directory(directory_name: str) -> str:
    return f'{upload_root_directory}/{directory_name}'
