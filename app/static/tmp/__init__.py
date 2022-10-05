import os

root_directory = os.getcwd()
tmp_root_directory = f'{root_directory}/app/static/tmp/files'


def tmp_file(file_name: str) -> str:
    return f'{tmp_root_directory}/{file_name}'


def tmp_directory(directory_name: str) -> str:
    return f'{tmp_root_directory}/{directory_name}'
