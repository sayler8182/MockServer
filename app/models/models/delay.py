class Delay(object):
    def __init__(self,
                 name: str,
                 delay: int):
        self.name = name
        self.delay = delay

    @staticmethod
    def supported_delays():
        return [
            Delay('Low', 50),
            Delay('Mid', 250),
            Delay('High', 750)
        ]

    def get_dict(self):
        return {
            'name': self.name,
            'delay': self.delay
        }
