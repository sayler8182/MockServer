import os

root_directory = os.getcwd()
upload_directory = f'{root_directory}/app/static/upload/files'


def upload_file(file_name: str) -> str:
    return f'{upload_directory}/{file_name}'
