from flask import request

from app.controllers import mocks_controller
from app.models.models.http_method import HTTPMethod
from app.utils.utils_api import response_dumps_object, response_dumps_list, response_error


class MocksRouter(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app

    def init_router(self):
        # mocks
        @self.flask_app.route('/api/mocks', methods=[HTTPMethod.GET.value])
        def get_mocks():
            mocks = mocks_controller.mocks()
            return response_dumps_list(self.flask_app, 200, mocks)

        @self.flask_app.route('/api/mocks/<mock_id>', methods=[HTTPMethod.GET.value])
        def get_mock(mock_id: str):
            mock = mocks_controller.mock(mock_id)
            if mock is None:
                return response_error(self.flask_app, 404, 'Can\'t find mock')
            return response_dumps_object(self.flask_app, 200, mock)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>', methods=[HTTPMethod.GET.value])
        def get_mock_response(mock_id: str, response_id: str):
            mock_response = mocks_controller.mock_response(mock_id, response_id)
            if mock_response is None:
                return response_error(self.flask_app, 404, 'Can\'t find mock response')
            return response_dumps_object(self.flask_app, 200, mock_response)

        @self.flask_app.route('/api/mocks/new', methods=[HTTPMethod.POST.value])
        def post_mock_new():
            mock = mocks_controller.mock_new()
            return response_dumps_object(self.flask_app, 200, mock)

        @self.flask_app.route('/api/mocks', methods=[HTTPMethod.DELETE.value])
        def delete_mocks():
            mocks_controller.mock_remove_all()
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>', methods=[HTTPMethod.DELETE.value])
        def delete_mock(mock_id: str):
            mocks_controller.mock_remove(mock_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/enable', methods=[HTTPMethod.POST.value])
        def post_mock_enable(mock_id: str):
            mocks_controller.mock_enable(mock_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/disable', methods=[HTTPMethod.POST.value])
        def post_mock_disable(mock_id: str):
            mocks_controller.mock_disable(mock_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/update', methods=[HTTPMethod.POST.value])
        def post_mock_update(mock_id: str):
            content = request.get_json(force=True)
            name = content.get('name', None)
            mocks_controller.mock_update(mock_id, name)
            return response_dumps_object(self.flask_app)

        # mock request
        @self.flask_app.route('/api/mocks/<mock_id>/request/update', methods=[HTTPMethod.POST.value])
        def post_mock_request_update(mock_id: str):
            content = request.get_json(force=True)
            method = content.get('method', None)
            path = content.get('path', None)
            mocks_controller.mock_request_update(mock_id, method, path)
            return response_dumps_object(self.flask_app)

        # mock response
        @self.flask_app.route('/api/mocks/<mock_id>/method/update', methods=[HTTPMethod.POST.value])
        def post_mock_method_update(mock_id: str):
            content = request.get_json(force=True)
            method = content.get('method', None)
            mocks_controller.mock_method_update(mock_id, method)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/new', methods=[HTTPMethod.POST.value])
        def post_mock_response_new(mock_id: str):
            response = mocks_controller.mock_response_new(mock_id)
            return response_dumps_object(self.flask_app, 200, response)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>', methods=[HTTPMethod.DELETE.value])
        def delete_mock_response(mock_id: str, response_id):
            mocks_controller.mock_response_remove(mock_id, response_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/enable', methods=[HTTPMethod.POST.value])
        def post_mock_response_enable(mock_id: str, response_id):
            mocks_controller.mock_response_enable(mock_id, response_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/disable', methods=[HTTPMethod.POST.value])
        def post_mock_response_disable(mock_id: str, response_id):
            mocks_controller.mock_response_disable(mock_id, response_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/set', methods=[HTTPMethod.POST.value])
        def post_mock_response_set(mock_id: str, response_id):
            mocks_controller.mock_response_set(mock_id, response_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/unset', methods=[HTTPMethod.POST.value])
        def post_mock_response_unset(mock_id: str, response_id):
            mocks_controller.mock_response_unset(mock_id, response_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/update', methods=[HTTPMethod.POST.value])
        def post_mock_response_update(mock_id: str, response_id: str):
            content = request.get_json(force=True)
            name = content.get('name', None)
            mocks_controller.mock_response_update(mock_id, response_id, name)
            return response_dumps_object(self.flask_app)

        # mock response type
        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/update/type', methods=[HTTPMethod.POST.value])
        def post_mock_response_update_type(mock_id: str, response_id: str):
            content = request.get_json(force=True)
            type = content.get('type', None)
            mocks_controller.mock_response_update_type(mock_id, response_id, type)
            return response_dumps_object(self.flask_app)

        # mock response status
        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/update/status', methods=[HTTPMethod.POST.value])
        def post_mock_response_update_status(mock_id: str, response_id: str):
            content = request.get_json(force=True)
            status = content.get('status', None)
            mocks_controller.mock_response_update_status(mock_id, response_id, status)
            return response_dumps_object(self.flask_app)

        # mock response headers
        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/headers/<headers_id>',
                              methods=[HTTPMethod.DELETE.value])
        def delete_mock_response_headers(mock_id: str, response_id: str, headers_id: str):
            mocks_controller.mock_response_headers_remove(mock_id, response_id, headers_id)
            return response_dumps_object(self.flask_app)

        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/headers/new', methods=[HTTPMethod.POST.value])
        def post_mock_response_headers(mock_id: str, response_id: str):
            content = request.get_json(force=True)
            name = content.get('name', None)
            value = content.get('value', None)
            header = mocks_controller.mock_response_headers_new(mock_id, response_id, name, value)
            return response_dumps_object(self.flask_app, 200, header)

        # mock response body
        @self.flask_app.route('/api/mocks/<mock_id>/<response_id>/update/body', methods=[HTTPMethod.POST.value])
        def post_mock_response_update_body(mock_id: str, response_id: str):
            content = request.get_json(force=True)
            body = content.get('body', None)
            header = mocks_controller.mock_response_update_body(mock_id, response_id, body)
            return response_dumps_object(self.flask_app, 200, header)