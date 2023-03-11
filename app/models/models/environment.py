from app.models.models.environment_item import EnvironmentItem
from app.models.models.environment_static_key import EnvironmentStaticKey
from app.utils.utils import get_dict


class Environment(object):
    def __init__(self,
                 static: [EnvironmentItem] = None,
                 dynamic: [EnvironmentItem] = None):
        self.static = static
        self.dynamic = dynamic
        self.__init_default_static()

    def __init_default_static(self):
        if self.static is None:
            self.static = Environment.static_items()

    @staticmethod
    def static_items() -> [EnvironmentItem]:
        return list(
            map(lambda item: EnvironmentItem(name=item.description, value=item.comment, parameters=item.parameters),
                EnvironmentStaticKey.available_keys()))

    def get_dict(self):
        return {
            'static': get_dict(self.static),
            'dynamic': get_dict(self.dynamic)
        }

    @staticmethod
    def environment_from_dict(object: dict):
        if object is None:
            return None

        static_list = object.get('static', None) or []
        static = list(map(lambda item: EnvironmentItem.environment_item_from_dict(item), static_list))
        dynamic_list = object.get('dynamic', None) or []
        dynamic = list(map(lambda item: EnvironmentItem.environment_item_from_dict(item), dynamic_list))
        return Environment(static=static,
                           dynamic=dynamic)
