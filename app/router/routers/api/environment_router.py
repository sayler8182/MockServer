from flask import request

from app.controllers import environment_controller
from app.models.models.http_method import HTTPMethod
from app.utils.utils_api import response_dumps_object


class EnvironmentRouter(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app

    def init_router(self):
        @self.flask_app.route('/api/environment', methods=[HTTPMethod.GET.value])
        def get_environment():
            """Get environment
            ---
            tags: [environment]
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Environment'
            """
            environment = environment_controller.environment()
            return response_dumps_object(self.flask_app, 200, environment)

        @self.flask_app.route('/api/environment/<item_id>', methods=[HTTPMethod.GET.value])
        def get_environment_item(item_id: str):
            """Get environment item
            ---
            tags: [environment]
            parameters:
            - name: item_id
              in: path
              required: true
              schema:
                type: string
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/EnvironmentItem'
            """
            environment_item = environment_controller.environment_item(item_id)
            return response_dumps_object(self.flask_app, 200, environment_item)

        @self.flask_app.route('/api/environment/new', methods=[HTTPMethod.POST.value])
        def post_environment_item():
            """Create environment item
            ---
            tags: [environment]
            parameters:
            - name: item_id
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
                  $ref: '#/definitions/EnvironmentItem'
            """
            content = request.get_json(force=False)
            name = content.get('name', None)
            value = content.get('value', None)
            environment_item = environment_controller.environment_new(name, value)
            return response_dumps_object(self.flask_app, 200, environment_item)

        @self.flask_app.route('/api/environment/<item_id>/update', methods=[HTTPMethod.POST.value])
        def post_environment_item_update(item_id: str):
            """Update environment item
            ---
            tags: [environment]
            parameters:
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
                  $ref: '#/definitions/EnvironmentItem'
            """
            content = request.get_json(force=False)
            name = content.get('name', None)
            value = content.get('value', None)
            environment_controller.environment_update(item_id, name, value)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/environment', methods=[HTTPMethod.DELETE.value])
        def delete_environment():
            """Delete dynamic environment items
            ---
            tags: [environment]
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
            """
            environment_controller.environment_remove_all()
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/environment/<item_id>', methods=[HTTPMethod.DELETE.value])
        def delete_environment_item(item_id: str):
            """Delete environment item
            ---
            tags: [environment]
            parameters:
            - name: item_id
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
            environment_controller.environment_remove(item_id)
            return response_dumps_object(self.flask_app)
