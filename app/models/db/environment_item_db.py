from app.config.database_config import db


class EnvironmentItemDb(db.Model):
    id = db.Column(db.String, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=True)
    value = db.Column(db.String, nullable=True)

    def __repr__(self):
        return 'EnvironmentItemDb:' \
               f' id: {self.id}' \
               f' name: {self.name}' \
               f' value: {self.value}'
