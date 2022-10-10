from app.controllers import logs_controller
from app.models.models.http_method import HTTPMethod
from app.utils.utils_api import response_dumps_list, response_dumps_object


class LogsRouter(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app

    def init_router(self):
        @self.flask_app.route('/api/logs', methods=[HTTPMethod.GET.value])
        def get_logs():
            """Get logs
            ---
            tags: [logs]
            responses:
              200:
                schema:
                  required: true
                  type: array
                  items:
                    $ref: '#/definitions/ResponseLog'
            """
            logs = logs_controller.logs()
            return response_dumps_list(self.flask_app, 200, logs)

        @self.flask_app.route('/api/logs/<mock_id>/logs', methods=[HTTPMethod.GET.value])
        def get_logs_for_mock(mock_id: str):
            """Get logs for mock
            ---
            tags: [logs]
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
                    $ref: '#/definitions/ResponseLog'
            """
            logs = logs_controller.logs_for_mock(mock_id)
            return response_dumps_list(self.flask_app, 200, logs)

        @self.flask_app.route('/api/logs/<log_id>', methods=[HTTPMethod.GET.value])
        def get_log(log_id: str):
            """Get log
            ---
            tags: [logs]
            parameters:
            - name: log_id
              in: path
              required: true
              schema:
                type: string
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/ResponseLog'
            """
            log = logs_controller.log(log_id)
            return response_dumps_object(self.flask_app, 200, log)

        @self.flask_app.route('/api/logs', methods=[HTTPMethod.DELETE.value])
        def delete_logs():
            """Delete logs
            ---
            tags: [logs]
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
            """
            logs_controller.logs_remove_all(None)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/logs/<mock_id>/logs', methods=[HTTPMethod.DELETE.value])
        def delete_logs_for_mock(mock_id: str):
            """Delete logs for mock
            ---
            tags: [logs]
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
            """
            logs_controller.logs_remove_all(mock_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/logs/<log_id>', methods=[HTTPMethod.DELETE.value])
        def delete_log(log_id: str):
            """Delete log
            ---
            tags: [logs]
            parameters:
            - name: log_id
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
            logs_controller.log_remove(None, log_id)
            return response_dumps_object(self.flask_app)
