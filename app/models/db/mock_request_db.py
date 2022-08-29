from app.config.database_config import db


class MockRequestDb(db.Model):
    id = db.Column(db.String, primary_key=True, nullable=False)
    mock_id = db.Column(db.String, nullable=False)
    method = db.Column(db.String, nullable=True)
    proxy = db.Column(db.String, nullable=True)
    path = db.Column(db.String, nullable=True)

    def __repr__(self):
        return 'MockRequestDb:' \
               f' id: {self.id}' \
               f' mock_id: {self.mock_id}' \
               f' method: {self.method}' \
               f' proxy: {self.proxy}' \
               f' path: {self.path}'
