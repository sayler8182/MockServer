from flask import request

from app.controllers import importing_exporting_controller
from app.models.models.http_method import HTTPMethod
from app.utils.utils_api import response_dumps_object


class ImportingExportingRouter(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app

    def init_router(self):
        @self.flask_app.route('/api/import', methods=[HTTPMethod.POST.value])
        def import_file():
            """Import file
            ---
            tags: [importing / exporting]
            consumes:
            - multipart / form - data
            parameters:
            - in: formData
              name: file
              type: file
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/Empty'
            """
            file = request.files.get('file')
            environment = importing_exporting_controller.import_file(file)
            return response_dumps_object(self.flask_app, 200, environment)

        @self.flask_app.route('/api/export/mocks', methods=[HTTPMethod.GET.value])
        def export_file_mocks():
            """Export file with mocks
            ---
            tags: [importing / exporting]
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/ExportedFile'
            """
            return importing_exporting_controller.export_file_mocks()

        @self.flask_app.route('/api/export/mocks/<mock_id>', methods=[HTTPMethod.GET.value])
        def export_file_mock(mock_id: str):
            """Export file with mock
            ---
            tags: [importing / exporting]
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
                  $ref: '#/definitions/ExportedFile'
            """
            return importing_exporting_controller.export_file_mock(mock_id)

        @self.flask_app.route('/api/export/environment', methods=[HTTPMethod.GET.value])
        def export_file_environment():
            """Export file with environment
            ---
            tags: [importing / exporting]
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/ExportedFile'
            """
            return importing_exporting_controller.export_file_environment()

        @self.flask_app.route('/api/export/proxies', methods=[HTTPMethod.GET.value])
        def export_file_proxies():
            """Export file with proxies
            ---
            tags: [importing / exporting]
            responses:
              200:
                type: object
                required: true
                schema:
                  $ref: '#/definitions/ExportedFile'
            """
            return importing_exporting_controller.export_file_proxies()

        @self.flask_app.route('/api/export/proxies/<proxy_id>', methods=[HTTPMethod.GET.value])
        def export_file_proxy(proxy_id: str):
            """Export file with proxy
            ---
            tags: [importing / exporting]
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
                  $ref: '#/definitions/ExportedFile'
            """
            return importing_exporting_controller.export_file_proxy(proxy_id)
