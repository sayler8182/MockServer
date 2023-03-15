
from app.config.database_config import db


class MockResponseLogDb(db.Model):
    id = db.Column(db.String, primary_key=True, nullable=False)
    mock_id = db.Column(db.String, nullable=True)
    response_id = db.Column(db.String, nullable=True)
    date = db.Column(db.DateTime, nullable=False)
    data_request = db.Column(db.String, nullable=True)
    data = db.Column(db.String, nullable=True)

    def __repr__(self):
        return 'MockResponseDb:' \
               f' id: {self.id}' \
               f' mock_id: {self.mock_id}' \
               f' response_id: {self.response_id}' \
               f' date: {self.date}' \
               f' data_request: {self.data_request}' \
               f' data: {self.data}'
