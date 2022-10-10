from app.config.database_config import db


class MockDb(db.Model):
    id = db.Column(db.String, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=True)
    is_enabled = db.Column(db.Boolean, default=True, nullable=False)
    method = db.Column(db.String, nullable=False)
    response_id = db.Column(db.String, nullable=True)

    def __repr__(self):
        return 'MockDb:' \
               f' id: {self.id}' \
               f' name: {self.name}' \
               f' is_enabled: {self.is_enabled}' \
               f' method: {self.method}' \
               f' response_id: {self.response_id}'
