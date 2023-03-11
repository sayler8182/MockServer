from enum import Enum


class EnvironmentStaticKey(Enum):
    date = 'date'
    uuid = 'uuid'

    @staticmethod
    def available_keys():
        return [
            EnvironmentStaticKey.date,
            EnvironmentStaticKey.uuid
        ]

    @property
    def description(self) -> str:
        return f'{self.value}'.upper()

    @property
    def comment(self) -> str:
        return {
            EnvironmentStaticKey.date: "Current date in ISO format",
            EnvironmentStaticKey.uuid: "Random uuid4",
        }.get(self)

    @property
    def parameters(self) -> dict:
        return {
            EnvironmentStaticKey.date: {
                "format": "Date format (in python style)",
                "shift": "shift between current date, separated with space: 1d 13h 2m 11s",
                "shift_direction": "shift direction 1 or -1 (add or subtract date)"
            },
            EnvironmentStaticKey.uuid: {}
        }.get(self)
