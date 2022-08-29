import os

dir_name = os.path.dirname(__file__)
base_dir = os.path.abspath(dir_name)
database_path = os.path.join(base_dir, 'app.db')


class AppConfig(object):
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    ENV = 'development'
    FLASK_ADMIN_SWATCH = 'cosmo'
    LANGUAGES = {
        'en': 'English'
    }
    MAX_CONTENT_LENGTH = 1024 * 1024
    SECRET_KEY = '472e826304a5ad7c3b905c9c97de909b543c49102a2069e3b6773f97b251eca2'
    SQLALCHEMY_DATABASE_URI = f'sqlite:////{database_path}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
