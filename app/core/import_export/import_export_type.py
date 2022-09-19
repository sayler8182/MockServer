from enum import Enum


class ImportExportType(Enum):
    mocks = 'mocks'
    mock = 'mock'
    environment = 'environment'
    proxies = 'proxies'
    proxy = 'proxy'
