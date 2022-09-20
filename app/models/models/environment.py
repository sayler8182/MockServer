from app.models.models.environment_item import EnvironmentItem
from app.models.models.environment_static_key import EnvironmentStaticKey
from app.utils.utils import get_dict


class Environment(object):
    def __init__(self,
                 dynamic: [EnvironmentItem] = None):
        self.static = Environment.static_items()
        self.dynamic = dynamic

    @staticmethod
    def static_items() -> [EnvironmentItem]:
        return list(map(lambda item: EnvironmentItem(name=item.description), EnvironmentStaticKey.available_keys()))

    def get_dict(self):
        return {
            'static': get_dict(self.static),
            'dynamic': get_dict(self.dynamic)
        }

    @staticmethod
    def environment_from_dict(object: dict):
        if object is None:
            return None

        static_list = object.get('static', None)
        dynamic_list = object.get('dynamic', None)
        static = list(map(lambda item: EnvironmentItem.environment_item_from_dict(item), static_list))
        dynamic = list(map(lambda item: EnvironmentItem.environment_item_from_dict(item), dynamic_list))
        return Environment(dynamic=dynamic)
