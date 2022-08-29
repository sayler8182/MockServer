import json

from werkzeug.datastructures import FileStorage

from app.adapters.mock_adapter import MockAdapter
from app.adapters.settings_proxy_adapter import SettingsProxyAdapter
from app.core.import_export.import_export_type import ImportExportType
from app.models.models.mock import Mock
from app.models.models.settings_proxy import SettingsProxy
from app.utils.utils import store_file_in_tmp, read_file


class ImporterManager(object):
    @staticmethod
    def import_file(file: FileStorage):
        data = ImporterManager.__data(file)
        type = ImporterManager.__type(data)
        {
            ImportExportType.mocks: ImporterManager.import_mocks,
            ImportExportType.mock: ImporterManager.import_mock,
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
    def import_proxies(data: dict):
        objects = ImporterManager.__list(data)
        for object in objects:
            proxy = SettingsProxy.proxy_from_dict(object)
            SettingsProxyAdapter.add_proxy(proxy)

    @staticmethod
    def import_proxy(data: dict):
        object = ImporterManager.__object(data)
        proxy = SettingsProxy.proxy_from_dict(object)
        SettingsProxyAdapter.add_proxy(proxy)

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
