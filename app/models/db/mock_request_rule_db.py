from app.config.database_config import db


class MockRequestRuleDb(db.Model):
    id = db.Column(db.String, primary_key=True, nullable=False)
    mock_id = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    is_enabled = db.Column(db.Boolean, default=True, nullable=False)
    key = db.Column(db.String, nullable=True)
    value = db.Column(db.String, nullable=True)

    def __repr__(self):
        return 'MockRequestRuleDb:' \
               f' id: {self.id}' \
               f' mock_id: {self.mock_id}' \
               f' type: {self.type}' \
               f' is_enabled: {self.is_enabled}' \
               f' key: {self.key}' \
               f' value: {self.value}'
