from app.utils.utils import new_id


class Database(object):
    def __init__(self,
                 id: str = None,
                 is_initiated: bool = None):
        self.id = id
        self.is_initiated = is_initiated
        self.__init_default_id()
        self.__init_default_is_initiated()

    def __init_default_id(self):
        if self.id is None:
            self.id = new_id()

    def __init_default_is_initiated(self):
        if self.is_initiated is None:
            self.is_initiated = False

    def get_dict(self):
        return {
            'id': self.id,
            'is_initiated': self.is_initiated
        }
