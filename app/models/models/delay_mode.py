from enum import Enum


class DelayMode(Enum):
    none = 'none'
    static = 'static'
    random = 'random'
    predefined = 'predefined'  # not supported yet - 3G / 4G / LTE / LTE+ / 5G

    @property
    def description(self) -> str:
        return {
            DelayMode.none: 'None',
            DelayMode.static: 'Static',
            DelayMode.random: 'Random',
            DelayMode.predefined: 'Predefined'
        }.get(self)

    @staticmethod
    def supported_modes():
        return [
            DelayMode.none,
            DelayMode.static,
            DelayMode.random
        ]

    def get_dict(self):
        return self.value
