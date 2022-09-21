from app.adapters.proxy_adapter import ProxyAdapter
from app.adapters.request_header_adapter import RequestHeaderAdapter
from app.adapters.settings_adapter import SettingsAdapter
from app.core.import_export.exporter_manager import ExporterManager
from app.core.import_export.importer_manager import ImporterManager
from app.models.models.delay import Delay
from app.models.models.delay_mode import DelayMode
from app.models.models.proxy import Proxy
from app.models.models.request_header import RequestHeader, RequestHeaderType
from app.models.models.settings import Settings
from app.models.models.settings_configuration import SettingsConfiguration
from app.utils.form_validator import validate_not_empty
from app.utils.utils import to_bool, to_int


# configuration
def configuration() -> SettingsConfiguration:
    return SettingsConfiguration(
        supported_delay_modes=DelayMode.supported_modes(),
        supported_delays=Delay.supported_delays()
    )


# settings
def settings() -> Settings:
    return SettingsAdapter.get_settings()


# proxy
def proxies() -> [Proxy]:
    return ProxyAdapter.get_proxies()


def proxy(proxy_id: str) -> Proxy:
    validate_not_empty(proxy_id, 'Incorrect proxy provided')
    return ProxyAdapter.get_proxy(proxy_id)


def proxy_new() -> Proxy:
    new_proxy = Proxy()
    ProxyAdapter.add_proxy(new_proxy)
    return new_proxy


def proxy_import_proxies(file):
    validate_not_empty(file, 'File should be provided')
    return ImporterManager.import_file(file)


def proxy_export_proxies():
    return ExporterManager.export_proxies()


def proxy_remove(proxy_id: str) -> str:
    ProxyAdapter.remove_proxy(proxy_id)
    return proxy_id


def proxy_export_proxy(proxy_id: str):
    validate_not_empty(proxy_id, 'Proxy should be provided')
    return ExporterManager.export_proxy(proxy_id)


def proxy_select(proxy_id: str, is_selected: bool):
    validate_not_empty(proxy_id, 'Incorrect proxy provided')
    is_selected = to_bool(is_selected)
    ProxyAdapter.set_proxy_select(proxy_id, is_selected)


def proxy_enable(proxy_id: str):
    validate_not_empty(proxy_id, 'Incorrect proxy provided')
    ProxyAdapter.set_proxy_enable(proxy_id)


def proxy_disable(proxy_id: str):
    validate_not_empty(proxy_id, 'Incorrect proxy provided')
    ProxyAdapter.set_proxy_disable(proxy_id)


def proxy_templating_enable(proxy_id: str):
    validate_not_empty(proxy_id, 'Incorrect proxy provided')
    ProxyAdapter.set_proxy_templating_enable(proxy_id)


def proxy_templating_disable(proxy_id: str):
    validate_not_empty(proxy_id, 'Incorrect proxy provided')
    ProxyAdapter.set_proxy_templating_disable(proxy_id)


def proxy_update(proxy_id: str, name: str, path: str):
    validate_not_empty(proxy_id, 'Incorrect proxy provided')
    ProxyAdapter.set_proxy_name_and_path(proxy_id, name, path)


def proxy_update_delay_mode(proxy_id: str, delay_mode: str):
    delay_mode = DelayMode[delay_mode]
    validate_not_empty(proxy_id, 'Incorrect proxy provided')
    ProxyAdapter.set_proxy_delay_mode(proxy_id, delay_mode)


def proxy_update_delay_static(proxy_id: str, delay: str):
    delay = to_int(delay)
    validate_not_empty(proxy_id, 'Incorrect proxy provided')
    ProxyAdapter.set_proxy_delay_static(proxy_id, delay)


def proxy_update_delay_random(proxy_id: str, delay_from: str, delay_to: str):
    delay_from = to_int(delay_from)
    delay_to = to_int(delay_to)
    validate_not_empty(proxy_id, 'Incorrect proxy provided')
    ProxyAdapter.set_proxy_delay_random(proxy_id, delay_from, delay_to)


# request headers
def proxy_request_headers_remove(proxy_id: str, header_id: str):
    validate_not_empty(id, 'Incorrect proxy provided')
    validate_not_empty(id, 'Incorrect header provided')
    RequestHeaderAdapter.remove_request_header(header_id)
    return header_id


def proxy_request_headers_new(proxy_id: str, name: str, value: str):
    validate_not_empty(id, 'Incorrect proxy provided')
    validate_not_empty(name, 'Name should not be empty')
    validate_not_empty(value, 'Value should not be empty')
    header = RequestHeader(type=RequestHeaderType.proxy_request,
                           proxy_id=proxy_id,
                           name=name,
                           value=value)
    RequestHeaderAdapter.add_request_header(header)
    return header


# response headers
def proxy_response_headers_remove(proxy_id: str, header_id: str):
    validate_not_empty(id, 'Incorrect proxy provided')
    validate_not_empty(id, 'Incorrect header provided')
    RequestHeaderAdapter.remove_request_header(header_id)
    return header_id


def proxy_response_headers_new(proxy_id: str, name: str, value: str):
    validate_not_empty(id, 'Incorrect proxy provided')
    validate_not_empty(name, 'Name should not be empty')
    validate_not_empty(value, 'Value should not be empty')
    header = RequestHeader(type=RequestHeaderType.proxy_response,
                           proxy_id=proxy_id,
                           name=name,
                           value=value)
    RequestHeaderAdapter.add_request_header(header)
    return header
