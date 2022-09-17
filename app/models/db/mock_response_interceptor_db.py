from app.config.database_config import db


class MockResponseInterceptorDb(db.Model):
    id = db.Column(db.String, primary_key=True, nullable=False)
    mock_id = db.Column(db.String, nullable=False)
    response_id = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    is_enabled = db.Column(db.Boolean, default=True, nullable=False)
    name = db.Column(db.String, nullable=True)
    configuration = db.Column(db.String, nullable=True)

    def __repr__(self):
        return 'MockResponseInterceptorDb:' \
               f' id: {self.id}' \
               f' mock_id: {self.mock_id}' \
               f' response_id: {self.response_id}' \
               f' type: {self.type}' \
               f' is_enabled: {self.is_enabled}' \
               f' name: {self.name}' \
               f' configuration: {self.configuration}'
