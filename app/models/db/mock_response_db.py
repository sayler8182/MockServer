from app.config.database_config import db


class MockResponseDb(db.Model):
    id = db.Column(db.String, primary_key=True, nullable=False)
    mock_id = db.Column(db.String, nullable=False)
    is_enabled = db.Column(db.Boolean, default=True, nullable=False)
    type = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=True)
    status = db.Column(db.Integer, nullable=True)
    delay_mode = db.Column(db.String, nullable=False)
    delay = db.Column(db.Integer, default=200, nullable=False)
    body = db.Column(db.String, nullable=True)
    order = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return 'MockResponseDb:' \
               f' id: {self.id}' \
               f' mock_id: {self.mock_id}' \
               f' is_enabled: {self.is_enabled}' \
               f' type: {self.type}' \
               f' name: {self.name}' \
               f' status: {self.status}' \
               f' delay_mode: {self.delay_mode}' \
               f' delay: {self.delay}' \
               f' body: {self.body}' \
               f' order: {self.order}'
