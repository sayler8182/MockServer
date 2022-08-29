from flask import Flask
import os


def create_app() -> Flask:
    flask_app = Flask(__name__)

    # init config
    from app.config.app_config import AppConfig
    flask_app.config.from_object(AppConfig)

    # init database
    from app.config.database_config import DatabaseConfig
    database_config = DatabaseConfig(flask_app)
    database_config.init_app()

    # init inject
    from app.config.inject_config import InjectConfig
    inject_config = InjectConfig(flask_app)
    inject_config.init_app()

    # init routing
    from app.router.router import Router
    router = Router(flask_app)
    router.init_app()

    # init panel
    from app.config.panel_config import PanelConfig
    panel_config = PanelConfig(flask_app)
    panel_config.init_app()

    # init database
    from app.database.database_initializer import DatabaseInitializer
    database_initializer = DatabaseInitializer(None)

    if os.getenv('FLASK_DATABASE_INITIALIZE'):
        database_initializer.init_app()

    return flask_app
