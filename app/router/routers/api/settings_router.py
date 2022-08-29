from flask import request

from app.controllers import settings_controller
from app.models.models.http_method import HTTPMethod
from app.utils.utils_api import response_dumps_object


class SettingsRouter(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app

    def init_router(self):
        # settings
        @self.flask_app.route('/api/settings', methods=[HTTPMethod.GET.value])
        def get_settings():
            settings = settings_controller.settings()
            return response_dumps_object(self.flask_app, settings)

        # proxy
        @self.flask_app.route('/api/settings/proxy/enable', methods=[HTTPMethod.POST.value])
        def post_settings_proxy_enable():
            settings_controller.proxy_enable(True)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/settings/proxy/disable', methods=[HTTPMethod.POST.value])
        def post_settings_proxy_disable():
            settings_controller.proxy_enable(False)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/settings/proxy/update', methods=[HTTPMethod.POST.value])
        def post_settings_proxy_update():
            content = request.get_json(force=True)
            url = content.get('url')
            settings_controller.proxy_update(url)
            return response_dumps_object(self.flask_app)

        # request headers
        @self.flask_app.route('/api/settings/request/header', methods=[HTTPMethod.POST.value])
        def post_settings_request_header():
            content = request.get_json(force=True)
            name = content.get('name')
            value = content.get('value')
            settings_controller.request_headers_new(name, value)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/settings/request/header', methods=[HTTPMethod.DELETE.value])
        def delete_settings_request_header():
            content = request.get_json(force=True)
            id = content.get('id')
            settings_controller.request_headers_remove(id)
            return response_dumps_object(self.flask_app)

        # response headers
        @self.flask_app.route('/api/settings/response/header', methods=[HTTPMethod.POST.value])
        def post_settings_response_header():
            content = request.get_json(force=True)
            name = content.get('name')
            value = content.get('value')
            settings_controller.response_headers_new(name, value)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/settings/response/header', methods=[HTTPMethod.DELETE.value])
        def delete_settings_response_header():
            content = request.get_json(force=True)
            id = content.get('id')
            settings_controller.response_headers_remove(id)
            return response_dumps_object(self.flask_app)
