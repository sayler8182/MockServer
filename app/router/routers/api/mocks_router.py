from flask import request

from app.controllers import mocks_controller
from app.models.models.http_method import HTTPMethod
from app.utils.utils_api import response_dumps_object, response_dumps_list, response_dumps_dict


class MocksRouter(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app

    def init_router(self):
        # mocks
        @self.flask_app.route('/api/mocks', methods=[HTTPMethod.GET.value])
        def get_mocks():
            """Get mocks
            ---
            tags: [mocks]
            definitions:
              Empty:
                type: object
              Error:
                type: object
                properties:
                  error:
                    type: string
                    required: true
              Mock:
                type: object
                properties:
                  id:
                    type: string
                    required: true
                  is_enabled:
                    type: boolean
                    required: true
                  method:
                    type: string
                    required: true
                    enum: [rotate, sequential]
                  response_id:
                    type: string
                  request_id:
                    type: object
                    required: true
                    $ref: '#/definitions/MockRequest'
                  responses:
                    type: array
                    required: true
                    items:
                      $ref: '#/definitions/MockResponse'
              MockRequest:
                type: object
                properties:
                  id:
                    type: string
                    required: true
                  mock_id:
                    type: string
                    required: true
                  method:
                    type: string
                    required: true
                    enum: [GET, POST, DELETE, PUT, PATCH]
                  proxy:
                    type: string
                  path:
                    type: string
              MockResponse:
                type: object
                properties:
                  id:
                    type: string
                    required: true
                  mock_id:
                    type: string
                    required: true
                  is_enabled:
                    type: boolean
                    required: true
                  is_single_use:
                    type: boolean
                    required: true
                  type:
                    type: string
                    required: true
                    enum: [mock_json, mock_file, proxy]
                  name:
                    type: string
                  status:
                    type: integer
                    required: true
                  delay_mode:
                    type: string
                    required: true
                    enum: [none, static, random]
                  delay_from:
                    type: integer
                    required: true
                  delay_to:
                    type: integer
                    required: true
                  delay:
                    type: integer
                    required: true
                  body:
                    type: string
                  body_path:
                    type: string
                  order:
                    type: integer
                    required: true
                  response_headers:
                    type: array
                    items:
                      $ref: '#/definitions/RequestHeader'
                  response_interceptors:
                    type: array
                    items:
                      $ref: '#/definitions/ResponseInterceptor'
              RequestHeader:
                type: object
                properties:
                  id:
                    type: string
                    required: true
                  type:
                    type: string
                    enum: [proxy_request, proxy_response, mock_request, mock_response]
                  proxy_id:
                    type: string
                  mock_id:
                    type: string
                  request_id:
                    type: string
                  response_id:
                    type: string
                  name:
                    type: string
                  value:
                    type: string
              ResponseInterceptor:
                type: object
                properties:
                  id:
                    type: string
                    required: true
                  mock_id:
                    type: string
                    required: true
                  response_id:
                    type: string
                    required: true
                  type:
                    type: string
                    required: true
                    enum: [custom, templating, update_environment, value_replace]
                  is_enabled:
                    type: boolean
                    required: true
                  name:
                    type: string
                  configuration:
                    type: string
              MockLogsCount:
                type: object
                properties:
                  count:
                    type: integer
                    required: true
              ResponseInterceptorConfigurationExample:
                type: object
                properties:
                  configuration_example:
                    type: string
              ResponseInterceptorConfigurationIsConfigurable:
                type: object
                properties:
                  is_configurable:
                    type: boolean
                    required: true
              ResponseLog:
                type: object
                properties:
                  id:
                    type: string
                    required: true
                  mock_id:
                    type: string
                  response_id:
                    type: string
                  date:
                    type: string
                    required: true
                  data:
                    type: string
              ExportedFile:
                type: object
                properties:
                  version:
                    type: string
                    required: true
                  type:
                    type: string
                    required: true
                  data:
                    type: object
                    required: true
              Environment:
                type: object
                properties:
                  static:
                    type: array
                    required: true
                    items:
                      $ref: '#/definitions/EnvironmentItem'
                  dynamic:
                    type: array
                    required: true
                    items:
                      $ref: '#/definitions/EnvironmentItem'
              Process:
                type: object
                properties:
                  pid:
                    type: integer
                    required: true
                    description: Process pid
                  key:
                    type: string
                    required: true
                    description: Process unique key
                  file_path:
                    type: string
                    required: true
                    description: Process script path
                  result:
                    type: string
                    description: Process strout
                  error:
                    type: string
                    description: Process strerr
              EnvironmentItem:
                type: object
                properties:
                  id:
                    type: string
                    required: true
                  name:
                    type: string
                    required: true
                  value:
                    type: string
              Settings:
                type: object
                properties:
                  proxy:
                    type: object
                    required: true
                    $ref: '#/definitions/Proxy'
              Proxy:
                type: object
                properties:
                  id:
                    type: string
                    required: true
                  is_selected:
                    type: boolean
                    required: true
                  is_enabled:
                    type: boolean
                    required: true
                  is_templating_enabled:
                    type: boolean
                    required: true
                  name:
                    type: string
                  path:
                    type: string
                  delay_mode:
                    type: string
                    required: true
                    enum: [none, static, random]
                  delay_from:
                    type: integer
                    required: true
                  delay_to:
                    type: integer
                    required: true
                  delay:
                    type: integer
                    required: true
                  request_headers:
                    type: array
                    required: true
                    items:
                      $ref: '#/definitions/RequestHeader'
                  response_headers:
                    type: array
                    required: true
                    items:
                      $ref: '#/definitions/RequestHeader'
              DelayMode:
                type: string
                enum: [none, static, random]
              HTTPMethod:
                type: string
                enum: [GET, POST, DELETE, PUT, PATCH]
              MockMethod:
                type: string
                enum: [rotate, sequential]
              MockResponseInterceptorType:
                type: string
                enum: [custom, templating, update_environment, value_replace]
              MockResponseType:
                type: string
                enum: [mock_json, mock_file, proxy]
              RequestHeaderType:
                type: string
                enum: [proxy_request, proxy_response, mock_request, mock_response]
            responses:
              200:
                schema:
                  required: true
                  type: array
                  items:
                    $ref: '#/definitions/Mock'
            """
            mocks = mocks_controller.mocks()
            return response_dumps_list(self.flask_app, 200, mocks)

        @self.flask_app.route('/api/mocks/conflicts', methods=[HTTPMethod.GET.value])
        def get_mocks_conflicts():
            """Get mocks conflicts
            ---
            tags: [mocks]
            parameters:
            - name: mock_id
              in: path
              required: true
              schema:
                type: string
            responses:
              200:
                schema:
                  required: true
                  type: array
                  items:
                    $ref: '#/definitions/Mock'
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            mocks = mocks_controller.mocks_conflicts()
            return response_dumps_list(self.flask_app, 200, mocks)

        @self.flask_app.route('/api/mocks/<mock_id>', methods=[HTTPMethod.GET.value])
        def get_mock(mock_id: str):
            """Get mock
            ---
            tags: [mocks]
            parameters:
            - name: mock_id
              in: path
              required: true
              schema:
                type: string
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Mock'
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            mock = mocks_controller.mock(mock_id)
            return response_dumps_object(self.flask_app, 200, mock)

        @self.flask_app.route('/api/mocks/<mock_id>/logs/count', methods=[HTTPMethod.GET.value])
        def post_mock_logs_count(mock_id: str):
            """Logs mock count
            ---
            tags: [mocks]
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/MockLogsCount'
            """
            count = mocks_controller.mock_logs_count(mock_id)
            response = {"count": count}
            return response_dumps_dict(self.flask_app, 200, response)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>', methods=[HTTPMethod.GET.value])
        def get_mock_response(mock_id: str, response_id: str):
            """Get mock response
            ---
            tags: [mocks]
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
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/MockResponse'
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            mock_response = mocks_controller.mock_response(mock_id, response_id)
            return response_dumps_object(self.flask_app, 200, mock_response)

        @self.flask_app.route('/api/mocks/new', methods=[HTTPMethod.POST.value])
        def post_mock_new():
            """Create mock new
            ---
            tags: [mocks]
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Mock'
            """
            mock = mocks_controller.mock_new()
            return response_dumps_object(self.flask_app, 200, mock)

        @self.flask_app.route('/api/mocks', methods=[HTTPMethod.DELETE.value])
        def delete_mocks():
            """Delete all mocks
            ---
            tags: [mocks]
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
            """
            mocks_controller.mock_remove_all()
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>', methods=[HTTPMethod.DELETE.value])
        def delete_mock(mock_id: str):
            """Delete mock
            ---
            tags: [mocks]
            parameters:
            - name: mock_id
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
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            mocks_controller.mock_remove(mock_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/enable', methods=[HTTPMethod.POST.value])
        def post_mock_enable(mock_id: str):
            """Enable mock
            ---
            tags: [mocks]
            parameters:
            - name: mock_id
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
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            mocks_controller.mock_enable(mock_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/disable', methods=[HTTPMethod.POST.value])
        def post_mock_disable(mock_id: str):
            """Disable mock
            ---
            tags: [mocks]
            parameters:
            - name: mock_id
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
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            mocks_controller.mock_disable(mock_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/update', methods=[HTTPMethod.POST.value])
        def post_mock_update(mock_id: str):
            """Update mock
            ---
            tags: [mocks]
            parameters:
            - name: mock_id
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
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            content = request.get_json(force=False)
            name = content.get('name', None)
            mocks_controller.mock_update(mock_id, name)
            return response_dumps_object(self.flask_app)

        # mock request
        @self.flask_app.route('/api/mocks/<mock_id>/request/update', methods=[HTTPMethod.POST.value])
        def post_mock_request_update(mock_id: str):
            """Update mock request
            ---
            tags: [mocks]
            parameters:
            - name: mock_id
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
                  method:
                    type: string
                    required: true
                    enum: [GET, POST, DELETE, PUT, PATCH]
                  path:
                    type: string
                    required: true
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            content = request.get_json(force=False)
            method = content.get('method', None)
            path = content.get('path', None)
            mocks_controller.mock_request_update(mock_id, method, path)
            return response_dumps_object(self.flask_app)

        # mock response
        @self.flask_app.route('/api/mocks/<mock_id>/method/update', methods=[HTTPMethod.POST.value])
        def post_mock_method_update(mock_id: str):
            """Update mock method
            ---
            tags: [mocks]
            parameters:
            - name: mock_id
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
                  method:
                    type: string
                    required: true
                    enum: [rotate, sequential]
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            content = request.get_json(force=False)
            method = content.get('method', None)
            mocks_controller.mock_method_update(mock_id, method)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/new', methods=[HTTPMethod.POST.value])
        def post_mock_response_new(mock_id: str):
            """Create mock response
            ---
            tags: [mocks]
            parameters:
            - name: mock_id
              in: path
              required: true
              schema:
                type: string
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/MockResponse'
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            response = mocks_controller.mock_response_new(mock_id)
            return response_dumps_object(self.flask_app, 200, response)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>', methods=[HTTPMethod.DELETE.value])
        def delete_mock_response(mock_id: str, response_id: str):
            """Delete mock response
            ---
            tags: [mocks]
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
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            mocks_controller.mock_response_remove(mock_id, response_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/order_up', methods=[HTTPMethod.POST.value])
        def delete_mock_response_order_up(mock_id: str, response_id: str):
            """Update mock response order
            ---
            tags: [mocks]
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
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            mocks_controller.mock_response_order_up(mock_id, response_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/order_down', methods=[HTTPMethod.POST.value])
        def delete_mock_response_order_down(mock_id: str, response_id: str):
            """Update mock response order
            ---
            tags: [mocks]
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
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            mocks_controller.mock_response_order_down(mock_id, response_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/enable', methods=[HTTPMethod.POST.value])
        def post_mock_response_enable(mock_id: str, response_id: str):
            """Enable mock response
            ---
            tags: [mocks]
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
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            mocks_controller.mock_response_enable(mock_id, response_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/disable', methods=[HTTPMethod.POST.value])
        def post_mock_response_disable(mock_id: str, response_id: str):
            """Disable mock response
            ---
            tags: [mocks]
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
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            mocks_controller.mock_response_disable(mock_id, response_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/set', methods=[HTTPMethod.POST.value])
        def post_mock_response_set(mock_id: str, response_id: str):
            """Set mock response as next response
            ---
            tags: [mocks]
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
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            mocks_controller.mock_response_set(mock_id, response_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/unset', methods=[HTTPMethod.POST.value])
        def post_mock_response_unset(mock_id: str, response_id: str):
            """Unset mock response as next response
            ---
            tags: [mocks]
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
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            mocks_controller.mock_response_unset(mock_id, response_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/single_use', methods=[HTTPMethod.POST.value])
        def post_mock_response_single_use(mock_id: str, response_id: str):
            """Unset mock response as single use
            ---
            tags: [mocks]
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
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            mocks_controller.mock_response_single_use(mock_id, response_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/not_single_use', methods=[HTTPMethod.POST.value])
        def post_mock_response_not_single_use(mock_id: str, response_id: str):
            """Unset mock response as not single use
            ---
            tags: [mocks]
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
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            mocks_controller.mock_response_not_single_use(mock_id, response_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/update', methods=[HTTPMethod.POST.value])
        def post_mock_response_update(mock_id: str, response_id: str):
            """Update mock response
            ---
            tags: [mocks]
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
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            content = request.get_json(force=False)
            name = content.get('name', None)
            mocks_controller.mock_response_update(mock_id, response_id, name)
            return response_dumps_object(self.flask_app)

        # mock response type
        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/update/type', methods=[HTTPMethod.POST.value])
        def post_mock_response_update_type(mock_id: str, response_id: str):
            """Update mock response type
            ---
            tags: [mocks]
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
            - name: body
              in: body
              required: true
              schema:
                type: object
                properties:
                  type:
                    type: string
                    required: true
                    enum: [mock_json, mock_file, proxy]
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            content = request.get_json(force=False)
            type = content.get('type', None)
            mocks_controller.mock_response_update_type(mock_id, response_id, type)
            return response_dumps_object(self.flask_app)

        # mock response delay
        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/update/delay/mode', methods=[HTTPMethod.POST.value])
        def post_mock_response_update_delay_mode(mock_id: str, response_id: str):
            """Update mock response delay mode
            ---
            tags: [mocks]
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
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            content = request.get_json(force=False)
            delay_mode = content.get('delay_mode', None)
            mocks_controller.mock_response_update_delay_mode(mock_id, response_id, delay_mode)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/update/delay/static', methods=[HTTPMethod.POST.value])
        def post_mock_response_update_delay_static(mock_id: str, response_id: str):
            """Update mock response delay static
            ---
            tags: [mocks]
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
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            content = request.get_json(force=False)
            delay = content.get('delay', None)
            mocks_controller.mock_response_update_delay_static(mock_id, response_id, delay)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/update/delay/random', methods=[HTTPMethod.POST.value])
        def post_mock_response_update_delay_random(mock_id: str, response_id: str):
            """Update mock response delay static
            ---
            tags: [mocks]
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
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            content = request.get_json(force=False)
            delay_from = content.get('delay_from', None)
            delay_to = content.get('delay_to', None)
            mocks_controller.mock_response_update_delay_random(mock_id, response_id, delay_from, delay_to)
            return response_dumps_object(self.flask_app)

        # mock response status
        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/update/status', methods=[HTTPMethod.POST.value])
        def post_mock_response_update_status(mock_id: str, response_id: str):
            """Update mock response status
            ---
            tags: [mocks]
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
            - name: body
              in: body
              required: true
              schema:
                type: object
                properties:
                  status:
                    type: integer
                    required: true
                    example: 200
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            content = request.get_json(force=False)
            status = content.get('status', None)
            mocks_controller.mock_response_update_status(mock_id, response_id, status)
            return response_dumps_object(self.flask_app)

        # mock response headers
        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/headers/<headers_id>',
                              methods=[HTTPMethod.DELETE.value])
        def delete_mock_response_headers(mock_id: str, response_id: str, headers_id: str):
            """Delete mock response header
            ---
            tags: [mocks]
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
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            mocks_controller.mock_response_headers_remove(mock_id, response_id, headers_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/headers/new', methods=[HTTPMethod.POST.value])
        def post_mock_response_headers(mock_id: str, response_id: str):
            """Create mock response header
             ---
             tags: [mocks]
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
               404:
                 type: object
                 required: true
                 schema:
                   $ref: '#/definitions/Error'
             """
            content = request.get_json(force=False)
            name = content.get('name', None)
            value = content.get('value', None)
            header = mocks_controller.mock_response_headers_new(mock_id, response_id, name, value)
            return response_dumps_object(self.flask_app, 200, header)

        # mock response body
        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/update/body/json', methods=[HTTPMethod.POST.value])
        def post_mock_response_update_body_json(mock_id: str, response_id: str):
            """Update mock response body
             ---
             tags: [mocks]
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
             - name: body
               in: body
               required: true
               schema:
                 type: object
                 properties:
                   body:
                     type: string
                     required: true
             responses:
               200:
                 type: object
                 required: true
                 schema:
                     $ref: '#/definitions/Empty'
               404:
                 type: object
                 required: true
                 schema:
                   $ref: '#/definitions/Error'
             """
            content = request.get_json(force=False)
            body = content.get('body', None)
            mocks_controller.mock_response_update_body_json(mock_id, response_id, body)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/update/body/path', methods=[HTTPMethod.POST.value])
        def post_mock_response_update_body_path(mock_id: str, response_id: str):
            """Update mock response body
             ---
             tags: [mocks]
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
             - name: body
               in: body
               required: true
               schema:
                 type: object
                 properties:
                   body_path:
                     type: string
                     required: true
             responses:
               200:
                 type: object
                 required: true
                 schema:
                     $ref: '#/definitions/Empty'
               404:
                 type: object
                 required: true
                 schema:
                   $ref: '#/definitions/Error'
             """
            content = request.get_json(force=False)
            body_path = content.get('body_path', None)
            mocks_controller.mock_response_update_body_path(mock_id, response_id, body_path)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/interceptors/<interceptor_id>',
                              methods=[HTTPMethod.DELETE.value])
        def delete_mock_response_interceptors(mock_id: str, response_id: str, interceptor_id: str):
            """Delete mock response interceptor
             ---
             tags: [mocks]
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
                     $ref: '#/definitions/Empty'
               404:
                 type: object
                 required: true
                 schema:
                   $ref: '#/definitions/Error'
             """
            mocks_controller.mock_response_interceptors_remove(mock_id, response_id, interceptor_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/interceptors/new', methods=[HTTPMethod.POST.value])
        def post_mock_response_interceptors_new(mock_id: str, response_id: str):
            """Delete mock response interceptor
             ---
             tags: [mocks]
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
             - name: body
               in: body
               required: true
               schema:
                 type: object
                 properties:
                   name:
                     type: string
                     required: true
                   type:
                     type: string
                     required: true
                     enum: [custom, templating, update_environment, value_replace]
             responses:
               200:
                 type: object
                 required: true
                 schema:
                     $ref: '#/definitions/ResponseInterceptor'
               404:
                 type: object
                 required: true
                 schema:
                   $ref: '#/definitions/Error'
             """
            content = request.get_json(force=False)
            name = content.get('name', None)
            type = content.get('type', None)
            interceptor = mocks_controller.mock_response_interceptors_new(mock_id, response_id, name, type)
            return response_dumps_object(self.flask_app, 200, interceptor)
