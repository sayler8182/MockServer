import json

from werkzeug.datastructures import FileStorage

from app.adapters.environment_adapter import EnvironmentAdapter
from app.adapters.mock_adapter import MockAdapter
from app.adapters.proxy_adapter import ProxyAdapter
from app.core.import_export.import_export_type import ImportExportType
from app.models.models.environment import Environment
from app.models.models.mock import Mock
from app.models.models.proxy import Proxy
from app.utils.utils import store_file_in_tmp, read_file


class ImporterManager(object):
    @staticmethod
    def import_file(file: FileStorage):
        data = ImporterManager.__data(file)
        type = ImporterManager.__type(data)
        {
            ImportExportType.mocks: ImporterManager.import_mocks,
            ImportExportType.mock: ImporterManager.import_mock,
            ImportExportType.environment: ImporterManager.import_environment,
            ImportExportType.proxies: ImporterManager.import_proxies,
            ImportExportType.proxy: ImporterManager.import_proxy
        }[type](data)

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
        for item in environment.items:
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
    def __data(file: FileStorage) -> dict:
        file_path = store_file_in_tmp(file)
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
