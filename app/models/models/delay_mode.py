from enum import Enum


class DelayMode(Enum):
    static = 'static'
    random = 'random'

    def get_dict(self):
        return self.value
