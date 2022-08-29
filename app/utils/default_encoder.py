import json


class DefaultEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__
