import json

from flask import request

from app.controllers import interceptors_controller
from app.models.models.http_method import HTTPMethod
from app.utils.utils_api import response_dumps_object, response_dumps_dict


class InterceptorRouter(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app

    def init_router(self):
        @self.flask_app.route('/api/interceptors/<mock_id>/<response_id>/interceptors/<interceptor_id>',
                              methods=[HTTPMethod.GET.value])
        def get_interceptor(mock_id: str, response_id: str, interceptor_id: str):
            """Get interceptor
            ---
            tags: [interceptors]
            parameters:
            - name: mock_id
              in: path
              required: true
              schema:
                type: string
            - name: response_id
              in: path
              required: true
              schema:
                type: string
            - name: interceptor_id
              in: path
              required: true
              schema:
                type: string
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/ResponseInterceptor'
            """
            interceptor = interceptors_controller.interceptor(mock_id, response_id, interceptor_id)
            return response_dumps_object(self.flask_app, 200, interceptor)

        @self.flask_app.route('/api/interceptors/<type>/configuration/example', methods=[HTTPMethod.GET.value])
        def get_interceptor_configuration_example(type: str):
            """Get interceptor configuration example
            ---
            tags: [interceptors]
            parameters:
            - name: type
              in: path
              required: true
              enum: [custom, templating, update_environment, value_replace]
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/ResponseInterceptorConfigurationExample'
            """
            configuration_example = interceptors_controller.interceptor_configuration_example(type)
            response = {"configuration_example": configuration_example}
            return response_dumps_dict(self.flask_app, 200, response)

        @self.flask_app.route('/api/interceptors/<type>/is_configurable', methods=[HTTPMethod.GET.value])
        def get_interceptor_is_configurable(type: str):
            """Get interceptor is configurable
            ---
            tags: [interceptors]
            parameters:
            - name: type
              in: path
              required: true
              enum: [custom, templating, update_environment, value_replace]
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/ResponseInterceptorConfigurationIsConfigurable'
            """
            is_configurable = interceptors_controller.interceptor_is_configurable(type)
            response = {"is_configurable": is_configurable}
            return response_dumps_dict(self.flask_app, 200, response)

        @self.flask_app.route('/api/interceptors/<mock_id>/<response_id>/interceptors/<interceptor_id>/update',
                              methods=[HTTPMethod.POST.value])
        def post_interceptor_update(mock_id: str, response_id: str, interceptor_id: str):
            """Update interceptor
            ---
            tags: [interceptors]
            parameters:
            - name: mock_id
              in: path
              required: true
            - name: response_id
              in: path
              required: true
            - name: interceptor_id
              in: path
              required: true
            - name: body
              in: body
              required: true
              schema:
                type: object
                properties:
                  name:
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
            interceptors_controller.interceptor_update(mock_id, response_id, interceptor_id, name)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/interceptors/<mock_id>/<response_id>/interceptors/<interceptor_id>/enable',
                              methods=[HTTPMethod.POST.value])
        def post_interceptor_enable(mock_id: str, response_id: str, interceptor_id: str):
            """Enable interceptor
            ---
            tags: [interceptors]
            parameters:
            - name: mock_id
              in: path
              required: true
            - name: response_id
              in: path
              required: true
            - name: interceptor_id
              in: path
              required: true
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
            """
            interceptors_controller.interceptor_enable(mock_id, response_id, interceptor_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/interceptors/<mock_id>/<response_id>/interceptors/<interceptor_id>/disable',
                              methods=[HTTPMethod.POST.value])
        def post_interceptor_disable(mock_id: str, response_id: str, interceptor_id: str):
            """Disable interceptor
            ---
            tags: [interceptors]
            parameters:
            - name: mock_id
              in: path
              required: true
            - name: response_id
              in: path
              required: true
            - name: interceptor_id
              in: path
              required: true
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
            """
            interceptors_controller.interceptor_disable(mock_id, response_id, interceptor_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route(
            '/api/interceptors/<mock_id>/<response_id>/interceptors/<interceptor_id>/update/configuration',
            methods=[HTTPMethod.POST.value])
        def post_interceptor_update_configuration(mock_id: str, response_id: str, interceptor_id: str):
            """Disable interceptor
            ---
            tags: [interceptors]
            parameters:
            - name: mock_id
              in: path
              required: true
            - name: response_id
              in: path
              required: true
            - name: interceptor_id
              in: path
              required: true
            - name: configuration
              in: body
              required: true
              schema:
                type: object
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
            """
            body = request.get_json(force=False)
            configuration = json.dumps(body)
            interceptors_controller.interceptor_update_configuration(mock_id, response_id, interceptor_id,
                                                                     configuration)
            return response_dumps_object(self.flask_app)
