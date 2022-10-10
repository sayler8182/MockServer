from flask import request, abort

from app.controllers import process_controller
from app.models.models.http_method import HTTPMethod
from app.utils.utils_api import response_dumps_object, response_dumps_list


class ProcessRouter(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app

    def init_router(self):
        @self.flask_app.route('/api/process', methods=[HTTPMethod.GET.value])
        def process():
            """Get processes
            ---
            tags: [process]
            responses:
              200:
                schema:
                  required: true
                  type: array
                  items:
                    $ref: '#/definitions/Process'
            """
            processes = process_controller.processes()
            return response_dumps_list(self.flask_app, 200, processes)

        @self.flask_app.route('/api/process/start', methods=[HTTPMethod.POST.value])
        def process_start():
            """Start process
            ---
            tags: [process]
            parameters:
            - name: body
              in: body
              required: true
              schema:
                type: object
                properties:
                  key:
                    type: string
                    required: true
                  file_path:
                    type: string
                    required: true
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Process'
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            content = request.get_json(force=False)
            key = content.get('key', None)
            file_path = content.get('file_path', None)
            process = process_controller.start(key, file_path)
            if not process:
                return abort(404)
            return response_dumps_object(self.flask_app, 200, process)

        @self.flask_app.route('/api/process/stop', methods=[HTTPMethod.DELETE.value])
        def process_stop():
            """Stop process
            ---
            tags: [process]
            parameters:
            - name: body
              in: body
              required: true
              schema:
                type: object
                properties:
                  key:
                    type: string
                    required: true
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Process'
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            content = request.get_json(force=False)
            key = content.get('key', None)
            process = process_controller.stop(key)
            if not process:
                return abort(404)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/process/call', methods=[HTTPMethod.POST.value])
        def process_call():
            """Call process
            ---
            tags: [process]
            parameters:
            - name: body
              in: body
              required: true
              schema:
                type: object
                properties:
                  key:
                    type: string
                    required: true
                  file_path:
                    type: string
                    required: true
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Process'
              404:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Error'
            """
            content = request.get_json(force=False)
            key = content.get('key', None)
            file_path = content.get('file_path', None)
            process = process_controller.call(key, file_path)
            if not process:
                return abort(404)
            return response_dumps_object(self.flask_app, 200, process)
