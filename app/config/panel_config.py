from flask_admin import Admin

from app.views import home_view
from app.views.environment import environment_view
from app.views.interceptors import interceptors_view
from app.views.mocks import mocks_view
from app.views.settings import settings_view

admin: Admin = None


class PanelConfig(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app

    def init_app(self):
        global admin
        admin = Admin(self.flask_app, name='MockServer', index_view=home_view.View(),
                      template_mode='bootstrap4')
        admin.add_view(
            mocks_view.View(name='Mocks', endpoint='mocks'))
        admin.add_view(
            environment_view.View(name='Environment', endpoint='environment'))
        admin.add_view(
            settings_view.View(name='Settings', endpoint='settings'))

        # hidden
        admin.add_view(
            interceptors_view.View(name='Interceptors', endpoint='interceptors'))
