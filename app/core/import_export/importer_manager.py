import json
import os

from werkzeug.datastructures import FileStorage

from app.adapters.environment_adapter import EnvironmentAdapter
from app.adapters.mock_adapter import MockAdapter
from app.adapters.proxy_adapter import ProxyAdapter
from app.core.import_export.import_export_type import ImportExportType
from app.models.models.environment import Environment
from app.models.models.mock import Mock
from app.models.models.proxy import Proxy
from app.utils.utils import store_file_in_tmp, read_file, store_file_in_upload, unzip_file_in_tmp


class ImporterManager(object):
    # upload
    @staticmethod
    def upload_file(file: FileStorage) -> str:
        return store_file_in_upload(file)

    # import file
    @staticmethod
    def import_file(file: FileStorage):
        file_path = store_file_in_tmp(file)
        ImporterManager.import_file_from_path(file_path)

    @staticmethod
    def import_file_from_path(file_path: str):
        print(file_path)
        if file_path.endswith(".zip"):
            ImporterManager.import_zip_from_path(file_path)
        elif file_path.endswith(".json"):
            ImporterManager.import_json_from_path(file_path)

    # import json
    @staticmethod
    def import_json_from_path(file_path: str):
        data = ImporterManager.__data_from_path(file_path)
        ImporterManager.__import_file_from_data(data)

    # import zip
    @staticmethod
    def import_zip_from_path(file_path: str):
        directory = unzip_file_in_tmp(file_path)
        for file_name in os.listdir(directory):
            file_path = f'{directory}/{file_name}'
            if os.path.isfile(file_path) and file_path.endswith(".json"):
                ImporterManager.import_file_from_path(file_path)

    @staticmethod
    def import_mocks(data: dict):
        objects = ImporterManager.__list(data)
        for object in objects:
            mock = Mock.mock_from_dict(object)
            MockAdapter.add_mock(mock)

    @staticmethod
    def import_mock(data: dict):
        object = ImporterManager.__object(data)
        mock = Mock.mock_from_dict(object)
        MockAdapter.add_mock(mock)

    @staticmethod
    def import_environment(data: dict):
        object = ImporterManager.__object(data)
        environment = Environment.environment_from_dict(object)
        print(environment)
        for item in environment.dynamic:
            EnvironmentAdapter.add_environment(item)

    @staticmethod
    def import_proxies(data: dict):
        objects = ImporterManager.__list(data)
        for object in objects:
            proxy = Proxy.proxy_from_dict(object)
            ProxyAdapter.add_proxy(proxy)

    @staticmethod
    def import_proxy(data: dict):
        object = ImporterManager.__object(data)
        proxy = Proxy.proxy_from_dict(object)
        ProxyAdapter.add_proxy(proxy)

    # utils
    @staticmethod
    def __import_file_from_data(data: dict):
        type = ImporterManager.__type(data)
        {
            ImportExportType.mocks: ImporterManager.import_mocks,
            ImportExportType.mock: ImporterManager.import_mock,
            ImportExportType.environment: ImporterManager.import_environment,
            ImportExportType.proxies: ImporterManager.import_proxies,
            ImportExportType.proxy: ImporterManager.import_proxy
        }[type](data)

    @staticmethod
    def __data_from_path(file_path: str) -> dict:
        content = read_file(file_path)
        object = json.loads(content)
        return object

    @staticmethod
    def __type(content: dict) -> ImportExportType:
        type = content.get('type', None)
        return ImportExportType[type]

    @staticmethod
    def __list(content: dict) -> list:
        return content.get('data', [])

    @staticmethod
    def __object(content: dict) -> dict:
        return content.get('data', {})
