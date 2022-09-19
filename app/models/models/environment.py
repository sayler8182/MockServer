from app.models.models.environment_item import EnvironmentItem
from app.utils.utils import get_dict


class Environment(object):
    def __init__(self,
                 items: [EnvironmentItem] = None):
        self.items = items

    def get_dict(self):
        return {
            'items': get_dict(self.items)
        }

    @staticmethod
    def environment_from_dict(object: dict):
        if object is None:
            return None

        items_list = object.get('items', None)
        items = list(map(lambda item: EnvironmentItem.environment_item_from_dict(item), items_list))
        return Environment(items=items)
