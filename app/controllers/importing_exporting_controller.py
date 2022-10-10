from app.core.import_export.exporter_manager import ExporterManager
from app.core.import_export.importer_manager import ImporterManager
from app.utils.form_validator import validate_not_empty


def import_file(file):
    validate_not_empty(file, 'File should be provided')
    return ImporterManager.import_file(file)


def export_file_mocks():
    return ExporterManager.export_mocks()


def export_file_mock(mock_id: str):
    validate_not_empty(mock_id, 'Mock should be provided')
    return ExporterManager.export_mock(mock_id)


def export_file_environment():
    return ExporterManager.export_environment()


def export_file_proxies():
    return ExporterManager.export_proxies()


def export_file_proxy(proxy_id: str):
    validate_not_empty(proxy_id, 'Proxy should be provided')
    return ExporterManager.export_proxy(proxy_id)
