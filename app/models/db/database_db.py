from app.config.database_config import db


class DatabaseDb(db.Model):
    id = db.Column(db.String, primary_key=True, nullable=False)
    is_initiated = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return 'DatabaseDb:' \
               f' id: {self.id}' \
               f' is_initiated: {self.is_initiated}'
