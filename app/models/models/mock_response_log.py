from datetime import datetime

from app.utils.utils import new_id


class MockResponseLog(object):
    def __init__(self,
                 mock_id: str,
                 response_id: str,
                 id: str = None,
                 date: datetime = None):
        self.id = id
        self.mock_id = mock_id
        self.response_id = response_id
        self.date = date
        self.__init_default_id()
        self.__init_default_date()

    def __init_default_id(self):
        if self.id is None:
            self.id = new_id()

    def __init_default_date(self):
        if self.date is None:
            self.date = datetime.now()

    def get_dict(self):
        return {
            'id': self.id,
            'mock_id': self.mock_id,
            'response_id': self.response_id,
            'date': self.date.isoformat()
        }
