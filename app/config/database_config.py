from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = None
migrate: Migrate = None


class DatabaseConfig:
    def __init__(self, flask_app):
        self.flask_app = flask_app

    def init_app(self):
        global db
        global migrate
        db = SQLAlchemy(self.flask_app)
        migrate = Migrate(self.flask_app, db)
        migrate.init_app(self.flask_app, db)
