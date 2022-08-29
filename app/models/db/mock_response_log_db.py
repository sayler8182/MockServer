
from app.config.database_config import db


class MockResponseLogDb(db.Model):
    id = db.Column(db.String, primary_key=True, nullable=False)
    mock_id = db.Column(db.String, nullable=False)
    response_id = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return 'MockResponseDb:' \
               f' id: {self.id}' \
               f' mock_id: {self.mock_id}' \
               f' response_id: {self.response_id}' \
               f' date: {self.date}'
