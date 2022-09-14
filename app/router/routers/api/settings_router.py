from flask import request

from app.controllers import settings_controller
from app.models.models.http_method import HTTPMethod
from app.utils.utils_api import response_dumps_object, response_dumps_list, response_error


class SettingsRouter(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app

    def init_router(self):
        # settings
        @self.flask_app.route('/api/settings', methods=[HTTPMethod.GET.value])
        def get_settings():
            settings = settings_controller.settings()
            if settings is None:
                return response_error(self.flask_app, 404, 'Can\'t find settings')
            return response_dumps_object(self.flask_app, 200, settings)

        # proxy
        @self.flask_app.route('/api/settings/proxy', methods=[HTTPMethod.GET.value])
        def get_settings_proxies():
            proxies = settings_controller.proxies()
            return response_dumps_list(self.flask_app, 200, proxies)

        @self.flask_app.route('/api/settings/proxy/<proxy_id>', methods=[HTTPMethod.GET.value])
        def get_settings_proxy(proxy_id: str):
            proxy = settings_controller.proxy(proxy_id)
            if proxy is None:
                return response_error(self.flask_app, 404, 'Can\'t find proxy')
            return response_dumps_object(self.flask_app, 200, proxy)

        @self.flask_app.route('/api/settings/proxy/<proxy_id>', methods=[HTTPMethod.DELETE.value])
        def delete_settings_proxy(proxy_id: str):
            settings_controller.proxy_remove(proxy_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/settings/proxy/<proxy_id>/select', methods=[HTTPMethod.POST.value])
        def post_settings_proxy_select(proxy_id: str):
            settings_controller.proxy_select(proxy_id, True)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/settings/proxy/<proxy_id>/enable', methods=[HTTPMethod.POST.value])
        def post_settings_proxy_enable(proxy_id: str):
            settings_controller.proxy_enable(proxy_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/settings/proxy/<proxy_id>/disable', methods=[HTTPMethod.POST.value])
        def post_settings_proxy_disable(proxy_id: str):
            settings_controller.proxy_disable(proxy_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/settings/proxy/<proxy_id>/update', methods=[HTTPMethod.POST.value])
        def post_settings_proxy_update(proxy_id: str):
            content = request.get_json(force=True)
            name = content.get('name', None)
            path = content.get('path', None)
            settings_controller.proxy_update(proxy_id, name, path)
            return response_dumps_object(self.flask_app)

        # request headers
        @self.flask_app.route('/api/settings/proxy/<proxy_id>/request/headers/<header_id>',
                              methods=[HTTPMethod.DELETE.value])
        def delete_settings_request_header(proxy_id: str, header_id: str):
            settings_controller.proxy_request_headers_remove(proxy_id, header_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/settings/proxy/<proxy_id>/request/headers/new', methods=[HTTPMethod.POST.value])
        def post_settings_request_header(proxy_id: str):
            content = request.get_json(force=True)
            name = content.get('name', None)
            value = content.get('value', None)
            header = settings_controller.proxy_request_headers_new(proxy_id, name, value)
            return response_dumps_object(self.flask_app, 200, header)

        # response headers
        @self.flask_app.route('/api/settings/proxy/<proxy_id>/response/headers/<header_id>',
                              methods=[HTTPMethod.DELETE.value])
        def delete_settings_response_header(proxy_id: str, header_id: str):
            settings_controller.proxy_response_headers_remove(proxy_id, header_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/settings/proxy/<proxy_id>/response/headers/new', methods=[HTTPMethod.POST.value])
        def post_settings_response_header(proxy_id: str):
            content = request.get_json(force=True)
            name = content.get('name', None)
            value = content.get('value', None)
            header = settings_controller.proxy_response_headers_new(proxy_id, name, value)
            return response_dumps_object(self.flask_app, 200, header)
