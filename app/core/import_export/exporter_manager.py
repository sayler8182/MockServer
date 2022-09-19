from app.adapters.environment_adapter import EnvironmentAdapter
from app.adapters.mock_adapter import MockAdapter
from app.adapters.proxy_adapter import ProxyAdapter
from app.core.import_export.import_export_type import ImportExportType
from app.utils.utils import get_dict
from app.utils.utils_api import response_dumps_dict_from_tmp_file

version = '1.0.0'


class ExporterManager(object):
    @staticmethod
    def export_mocks():
        mocks = MockAdapter.get_mocks()
        object = ExporterManager.__object(type=ImportExportType.mocks,
                                          data=get_dict(mocks))
        file_name = ImportExportType.mocks.value
        return response_dumps_dict_from_tmp_file(object, file_name)

    @staticmethod
    def export_mock(mock_id: str):
        mock = MockAdapter.get_mock(mock_id)
        object = ExporterManager.__object(type=ImportExportType.mock,
                                          data=mock.get_dict())
        file_name = ImportExportType.mock.name or 'mock'
        return response_dumps_dict_from_tmp_file(object, file_name)

    @staticmethod
    def export_environment():
        environment = EnvironmentAdapter.get_environment()
        object = ExporterManager.__object(type=ImportExportType.environment,
                                          data=environment.get_dict())
        file_name = ImportExportType.environment.value
        return response_dumps_dict_from_tmp_file(object, file_name)

    @staticmethod
    def export_proxies():
        proxies = ProxyAdapter.get_proxies()
        object = ExporterManager.__object(type=ImportExportType.proxies,
                                          data=get_dict(proxies))
        file_name = ImportExportType.proxies.value
        return response_dumps_dict_from_tmp_file(object, file_name)

    @staticmethod
    def export_proxy(proxy_id: str):
        proxy = ProxyAdapter.get_proxy(proxy_id)
        object = ExporterManager.__object(type=ImportExportType.proxy,
                                          data=proxy.get_dict())
        file_name = ImportExportType.proxy.name or 'proxy'
        return response_dumps_dict_from_tmp_file(object, file_name)

    # utils

    @staticmethod
    def __object(type: ImportExportType, data: any) -> dict:
        return {
            'version': version,
            'type': type.value,
            'data': data
        }
