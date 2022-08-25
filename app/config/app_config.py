import os

base_dir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(base_dir, 'app.db')


class AppConfig(object):
    ENV = 'development'
    SECRET_KEY = '472e826304a5ad7c3b905c9c97de909b543c49102a2069e3b6773f97b251eca2'
    MAX_CONTENT_LENGTH = 1024 * 1024
    FLASK_ADMIN_FLUID_LAYOUT = True
    FLASK_ADMIN_SWATCH = 'cosmo'
    SQLALCHEMY_DATABASE_URI = f'sqlite:////{database_path}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
