from app.utils.utils import new_id


class EnvironmentItem(object):
    def __init__(self,
                 id: str = None,
                 name: str = None,
                 value: str = None,
                 parameters: dict = None):
        self.id = id
        self.name = name
        self.value = value
        self.parameters = parameters
        self.__init_default_id()

    def __init_default_id(self):
        if self.id is None:
            self.id = new_id()

    def get_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'value': self.value,
            'parameters': self.parameters
        }

    @staticmethod
    def environment_item_from_dict(object: dict):
        if object is None:
            return None

        id = object.get('id', None)
        name = object.get('name', None)
        value = object.get('value', None)
        parameters = object.get('parameters', None)
        return EnvironmentItem(id=id,
                               name=name,
                               value=value,
                               parameters=parameters)
