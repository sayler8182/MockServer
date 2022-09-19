from app.adapters.environment_adapter import EnvironmentAdapter
from app.core.import_export.exporter_manager import ExporterManager
from app.core.import_export.importer_manager import ImporterManager
from app.models.models.environment import Environment
from app.models.models.environment_item import EnvironmentItem
from app.utils.form_validator import validate_not_empty


def environment() -> Environment:
    return EnvironmentAdapter.get_environment()


def environment_item(item_id: str) -> EnvironmentItem:
    return EnvironmentAdapter.get_environment_item(item_id)


def environment_new(name: str, value: str) -> EnvironmentItem:
    validate_not_empty(name, 'Name should not be empty')
    validate_not_empty(value, 'Value should not be empty')
    environment = EnvironmentItem(name=name,
                                  value=value)
    EnvironmentAdapter.add_environment(environment)
    return environment


def environment_update(item_id: str, name: str, value: str):
    validate_not_empty(name, 'Name should not be empty')
    validate_not_empty(value, 'Value should not be empty')
    EnvironmentAdapter.set_environment(item_id, name, value)


def environment_import_environment(file):
    validate_not_empty(file, 'File should be provided')
    return ImporterManager.import_file(file)


def environment_export_environment():
    return ExporterManager.export_environment()


def environment_remove_all():
    return EnvironmentAdapter.remove_all()


def environment_remove(item_id: str):
    validate_not_empty(item_id, 'Item should be provided')
    EnvironmentAdapter.remove_environment(item_id)
