from app.config.database_config import db


class MockResponseDb(db.Model):
    id = db.Column(db.String, primary_key=True, nullable=False)
    mock_id = db.Column(db.String, nullable=False)
    is_enabled = db.Column(db.Boolean, default=True, nullable=False)
    is_single_use = db.Column(db.Boolean, nullable=True)
    type = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=True)
    status = db.Column(db.Integer, nullable=True)
    delay_mode = db.Column(db.String, nullable=False)
    delay_from = db.Column(db.Integer, default=0, nullable=False)
    delay_to = db.Column(db.Integer, default=0, nullable=False)
    delay = db.Column(db.Integer, default=200, nullable=False)
    body = db.Column(db.String, nullable=True)
    order = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return 'MockResponseDb:' \
               f' id: {self.id}' \
               f' mock_id: {self.mock_id}' \
               f' is_enabled: {self.is_enabled}' \
               f' is_single_use: {self.is_single_use}' \
               f' type: {self.type}' \
               f' name: {self.name}' \
               f' status: {self.status}' \
               f' delay_mode: {self.delay_mode}' \
               f' delay_from: {self.delay_from}' \
               f' delay_to: {self.delay_to}' \
               f' delay: {self.delay}' \
               f' body: {self.body}' \
               f' order: {self.order}'
