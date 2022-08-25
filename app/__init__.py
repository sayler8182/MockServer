from flask import Flask, abort, render_template, request

from app.config.app_config import AppConfig
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config.from_object(AppConfig)

    # db
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def index():
        return 'hello world'

    return app
