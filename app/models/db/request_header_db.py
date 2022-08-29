from app.config.database_config import db


class RequestHeaderDb(db.Model):
    id = db.Column(db.String, primary_key=True, nullable=False)
    type = db.Column(db.String, nullable=False)
    proxy_id = db.Column(db.String, nullable=True)
    mock_id = db.Column(db.String, nullable=True)
    request_id = db.Column(db.String, nullable=True)
    response_id = db.Column(db.String, nullable=True)
    name = db.Column(db.String, nullable=True)
    value = db.Column(db.String, nullable=True)

    def __repr__(self):
        return 'RequestHeaderDb:' \
               f' id: {self.id}' \
               f' type: {self.type}' \
               f' proxy_id: {self.proxy_id}' \
               f' mock_id: {self.mock_id}' \
               f' request_id: {self.request_id}' \
               f' response_id: {self.response_id}' \
               f' name: {self.name}' \
               f' value: {self.value}'
