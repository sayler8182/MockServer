from enum import Enum


class EnvironmentStaticKey(Enum):
    date = 'date'

    @staticmethod
    def available_keys():
        return [
            EnvironmentStaticKey.date
        ]

    @property
    def description(self) -> str:
        return f'{self.value}'.upper()
