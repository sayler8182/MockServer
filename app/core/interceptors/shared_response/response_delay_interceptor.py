import time
from random import randint

from app.adapters.proxy_adapter import ProxyAdapter
from app.models.models.delay_mode import DelayMode
from app.models.models.mock import Mock
from app.models.models.mock_response import MockResponse
from app.models.models.proxy_response import ProxyResponse
from app.utils.utils import safe_call_with_result


class ResponseDelayInterceptor(object):
    def intercept(self, response: ProxyResponse, mock: Mock, mock_response: MockResponse) -> ProxyResponse:
        proxy = ProxyAdapter.get_proxy_selected()
        delay = self.__delay(mock_response) or self.__delay(proxy) or 0
        time.sleep(delay / 1000)
        return response

    def __delay(self, provider) -> int:
        if provider is None:
            return None

        value = {
            DelayMode.none: lambda: self.__delay_time_none(provider),
            DelayMode.static: lambda: self.__delay_time_static(provider),
            DelayMode.random: lambda: self.__delay_time_random(provider),
            DelayMode.predefined: lambda: self.__delay_time_predefined(provider)
        }.get(provider.delay_mode)
        return safe_call_with_result(value)

    def __delay_time_none(self, provider) -> int:
        return None

    def __delay_time_static(self, provider) -> int:
        return provider.delay

    def __delay_time_random(self, provider) -> int:
        delay_from = provider.delay_from or 0
        delay_to = provider.delay_to or 0
        if delay_from > delay_to:
            return None
        if delay_from == delay_to:
            return delay_from
        return randint(delay_from, delay_to)

    def __delay_time_predefined(self, provider) -> int:
        return None
