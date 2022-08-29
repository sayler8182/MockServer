import os

root_directory = os.getcwd()
tmp_directory = f'{root_directory}/app/static/tmp/files'


def tmp_file(file_name: str) -> str:
    return f'{tmp_directory}/{file_name}'
