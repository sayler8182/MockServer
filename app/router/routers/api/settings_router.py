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
            """Get settings
            ---
            tags: [settings]
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Settings'
            """
            settings = settings_controller.settings()
            return response_dumps_object(self.flask_app, 200, settings)

        # proxy
        @self.flask_app.route('/api/settings/proxy', methods=[HTTPMethod.GET.value])
        def get_settings_proxies():
            """Get selected proxy
            ---
            tags: [settings]
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Proxy'
            """
            proxies = settings_controller.proxies()
            return response_dumps_list(self.flask_app, 200, proxies)

        @self.flask_app.route('/api/settings/proxy/<proxy_id>', methods=[HTTPMethod.GET.value])
        def get_settings_proxy(proxy_id: str):
            """Get proxy
            ---
            tags: [settings]
            parameters:
            - name: proxy_id
              in: path
              required: true
              schema:
                type: string
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Proxy'
            """
            proxy = settings_controller.proxy(proxy_id)
            return response_dumps_object(self.flask_app, 200, proxy)

        @self.flask_app.route('/api/settings/proxy/<proxy_id>', methods=[HTTPMethod.DELETE.value])
        def delete_settings_proxy(proxy_id: str):
            """Delete proxy
            ---
            tags: [settings]
            parameters:
            - name: proxy_id
              in: path
              required: true
              schema:
                type: string
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
            """
            settings_controller.proxy_remove(proxy_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/settings/proxy/<proxy_id>/select', methods=[HTTPMethod.POST.value])
        def post_settings_proxy_select(proxy_id: str):
            """Select proxy
            ---
            tags: [settings]
            parameters:
            - name: proxy_id
              in: path
              required: true
              schema:
                type: string
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
            """
            settings_controller.proxy_select(proxy_id, True)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/settings/proxy/<proxy_id>/enable', methods=[HTTPMethod.POST.value])
        def post_settings_proxy_enable(proxy_id: str):
            """Enable proxy
            ---
            tags: [settings]
            parameters:
            - name: proxy_id
              in: path
              required: true
              schema:
                type: string
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
            """
            settings_controller.proxy_enable(proxy_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/settings/proxy/<proxy_id>/disable', methods=[HTTPMethod.POST.value])
        def post_settings_proxy_disable(proxy_id: str):
            """Disable proxy
            ---
            tags: [settings]
            parameters:
            - name: proxy_id
              in: path
              required: true
              schema:
                type: string
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
            """
            settings_controller.proxy_disable(proxy_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/settings/proxy/<proxy_id>/templating/enable', methods=[HTTPMethod.POST.value])
        def post_settings_proxy_templating_enable(proxy_id: str):
            """Enable templating proxy
            ---
            tags: [settings]
            parameters:
            - name: proxy_id
              in: path
              required: true
              schema:
                type: string
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
            """
            settings_controller.proxy_templating_enable(proxy_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/settings/proxy/<proxy_id>/templating/disable', methods=[HTTPMethod.POST.value])
        def post_settings_proxy_templating_disable(proxy_id: str):
            """Disable templating proxy
            ---
            tags: [settings]
            parameters:
            - name: proxy_id
              in: path
              required: true
              schema:
                type: string
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
            """
            settings_controller.proxy_templating_disable(proxy_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/settings/proxy/<proxy_id>/update', methods=[HTTPMethod.POST.value])
        def post_settings_proxy_update(proxy_id: str):
            """Update proxy
            ---
            tags: [settings]
            parameters:
            - name: proxy_id
              in: path
              required: true
              schema:
                type: string
            - name: body
              in: body
              required: true
              schema:
                type: object
                properties:
                  name:
                    type: string
                    required: true
                  path:
                    type: string
                    required: true
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
            """
            content = request.get_json(force=False)
            name = content.get('name', None)
            path = content.get('path', None)
            settings_controller.proxy_update(proxy_id, name, path)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/settings/proxy/<proxy_id>/update/delay/mode', methods=[HTTPMethod.POST.value])
        def post_settings_proxy_update_delay_mode(proxy_id: str):
            """Update proxy delay mode
            ---
            tags: [settings]
            parameters:
            - name: proxy_id
              in: path
              required: true
              schema:
                type: string
            - name: body
              in: body
              required: true
              schema:
                type: object
                properties:
                  delay_mode:
                    type: string
                    required: true
                    enum: [none, static, random]
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
            """
            content = request.get_json(force=False)
            delay_mode = content.get('delay_mode', None)
            settings_controller.proxy_update_delay_mode(proxy_id, delay_mode)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/settings/proxy/<proxy_id>/update/delay/static', methods=[HTTPMethod.POST.value])
        def post_settings_proxy_update_delay_static(proxy_id: str):
            """Update proxy delay static
            ---
            tags: [settings]
            parameters:
            - name: proxy_id
              in: path
              required: true
              schema:
                type: string
            - name: body
              in: body
              required: true
              schema:
                type: object
                properties:
                  delay:
                    type: integer
                    required: true
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
            """
            content = request.get_json(force=False)
            delay = content.get('delay', None)
            settings_controller.proxy_update_delay_static(proxy_id, delay)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/settings/proxy/<proxy_id>/update/delay/random', methods=[HTTPMethod.POST.value])
        def post_settings_proxy_update_delay_random(proxy_id: str):
            """Update proxy delay random
            ---
            tags: [settings]
            parameters:
            - name: proxy_id
              in: path
              required: true
              schema:
                type: string
            - name: body
              in: body
              required: true
              schema:
                type: object
                properties:
                  delay_from:
                    type: integer
                    required: true
                  delay_to:
                    type: integer
                    required: true
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
            """
            content = request.get_json(force=False)
            delay_from = content.get('delay_from', None)
            delay_to = content.get('delay_to', None)
            settings_controller.proxy_update_delay_random(proxy_id, delay_from, delay_to)
            return response_dumps_object(self.flask_app)

        # request headers
        @self.flask_app.route('/api/settings/proxy/<proxy_id>/request/headers/<header_id>',
                              methods=[HTTPMethod.DELETE.value])
        def delete_settings_request_header(proxy_id: str, header_id: str):
            """Delete proxy request header
            ---
            tags: [settings]
            parameters:
            - name: proxy_id
              in: path
              required: true
              schema:
                type: string
            - name: header_id
              in: path
              required: true
              schema:
                type: string
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
            """
            settings_controller.proxy_request_headers_remove(proxy_id, header_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/settings/proxy/<proxy_id>/request/headers/new', methods=[HTTPMethod.POST.value])
        def post_settings_request_header(proxy_id: str):
            """Create proxy request header
            ---
            tags: [settings]
            parameters:
            - name: proxy_id
              in: path
              required: true
              schema:
                type: string
            - name: body
              in: body
              required: true
              schema:
                type: object
                properties:
                  name:
                    type: string
                    required: true
                  value:
                    type: string
                    required: true
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/RequestHeader'
            """
            content = request.get_json(force=False)
            name = content.get('name', None)
            value = content.get('value', None)
            header = settings_controller.proxy_request_headers_new(proxy_id, name, value)
            return response_dumps_object(self.flask_app, 200, header)

        # response headers
        @self.flask_app.route('/api/settings/proxy/<proxy_id>/response/headers/<header_id>',
                              methods=[HTTPMethod.DELETE.value])
        def delete_settings_response_header(proxy_id: str, header_id: str):
            """Delete proxy response header
            ---
            tags: [settings]
            parameters:
            - name: proxy_id
              in: path
              required: true
              schema:
                type: string
            - name: header_id
              in: path
              required: true
              schema:
                type: string
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
            """
            settings_controller.proxy_response_headers_remove(proxy_id, header_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/settings/proxy/<proxy_id>/response/headers/new', methods=[HTTPMethod.POST.value])
        def post_settings_response_header(proxy_id: str):
            """Create proxy response header
            ---
            tags: [settings]
            parameters:
            - name: proxy_id
              in: path
              required: true
              schema:
                type: string
            - name: body
              in: body
              required: true
              schema:
                type: object
                properties:
                  name:
                    type: string
                    required: true
                  value:
                    type: string
                    required: true
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/RequestHeader'
            """
            content = request.get_json(force=False)
            name = content.get('name', None)
            value = content.get('value', None)
            header = settings_controller.proxy_response_headers_new(proxy_id, name, value)
            return response_dumps_object(self.flask_app, 200, header)
