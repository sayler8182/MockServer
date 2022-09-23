from flask import redirect, url_for, request
from flask_admin import BaseView, expose

from app.controllers import mocks_controller
from app.models.models.http_method import HTTPMethod
from app.utils.utils import call, toast, call_with_result


class View(BaseView):

    @expose('/')
    def index(self):
        configuration = mocks_controller.configuration()
        mocks = mocks_controller.mocks()
        return self.render('admin/mocks/mocks.html', configuration=configuration, mocks=mocks)

    @expose('/<mock_id>')
    def mock(self, mock_id):
        configuration = mocks_controller.configuration(mock_id=mock_id)
        mocks = mocks_controller.mocks()
        mock = mocks_controller.mock(mock_id)
        response_next = mocks_controller.mock_response_next(mock_id)
        return self.render('admin/mocks/mocks.html', configuration=configuration, mocks=mocks, mock=mock,
                           response_next=response_next)

    @expose('/<mock_id>/<response_id>')
    def mock_response(self, mock_id, response_id):
        configuration = mocks_controller.configuration(mock_id=mock_id, response_id=response_id)
        mocks = mocks_controller.mocks()
        mock = mocks_controller.mock(mock_id)
        response_next = mocks_controller.mock_response_next(mock_id)
        response = mocks_controller.mock_response(mock_id, response_id)
        return self.render('admin/mocks/mocks.html', configuration=configuration, mocks=mocks, mock=mock,
                           response_next=response_next, response=response)

    # mock
    @expose('new', methods=[HTTPMethod.POST.value])
    def mock_new(self):
        mock = mocks_controller.mock_new()
        return redirect(url_for('mocks.index', mock_id=mock.id))

    @expose('/import', methods=[HTTPMethod.POST.value])
    def mock_import_mocks(self):
        file = request.files.get('mocks_form_file_import')
        call(
            lambda: mocks_controller.mock_import_mocks(file),
            lambda: toast('Mocks have been imported', category='success')
        )
        return url_for('mocks.index')

    @expose('/export', methods=[HTTPMethod.POST.value])
    def mock_export_mocks(self):
        return call_with_result(
            lambda: mocks_controller.mock_export_mocks(),
            lambda: toast('Mocks have been exported', category='success')
        )

    @expose('remove', methods=[HTTPMethod.POST.value])
    def mock_remove_all(self):
        mocks_controller.mock_remove_all()
        toast('Mocks have been removed', category='success')
        return redirect(url_for('mocks.index'))

    @expose('<mock_id>/remove', methods=[HTTPMethod.POST.value])
    def mock_remove(self, mock_id):
        mocks_controller.mock_remove(mock_id)
        toast('Mock has been removed', category='success')
        return redirect(url_for('mocks.index'))

    @expose('/<mock_id>/export', methods=[HTTPMethod.POST.value])
    def mock_export_mock(self, mock_id):
        return call_with_result(
            lambda: mocks_controller.mock_export_mock(mock_id),
            lambda: toast('Mock has been exported', category='success')
        )

    @expose('/<mock_id>/enable', methods=[HTTPMethod.POST.value])
    def mock_enable(self, mock_id):
        call(
            lambda: mocks_controller.mock_enable(mock_id),
            lambda: toast('Mock has been enabled', category='success')
        )
        return redirect(url_for('mocks.mock', mock_id=mock_id))

    @expose('/<mock_id>/disable', methods=[HTTPMethod.POST.value])
    def mock_disable(self, mock_id):
        call(
            lambda: mocks_controller.mock_disable(mock_id),
            lambda: toast('Mock has been disabled', category='success')
        )
        return redirect(url_for('mocks.mock', mock_id=mock_id))

    @expose('/<mock_id>/update', methods=[HTTPMethod.POST.value])
    def mock_update(self, mock_id):
        name = request.form.get('mocks_definition_form_name')
        call(
            lambda: mocks_controller.mock_update(mock_id, name),
            lambda: toast('Mock has been updated', category='success')
        )
        return redirect(url_for('mocks.mock', mock_id=mock_id))

    # mock request
    @expose('/<mock_id>/request/update', methods=[HTTPMethod.POST.value])
    def mock_request_update(self, mock_id):
        method = request.form.get('mocks_definition_form_request_method')
        path = request.form.get('mocks_definition_form_request_path')
        call(
            lambda: mocks_controller.mock_request_update(mock_id, method, path),
            lambda: toast('Request has been updated', category='success')
        )
        return redirect(url_for('mocks.mock', mock_id=mock_id))

    # mock response
    @expose('/<mock_id>/method/update', methods=[HTTPMethod.POST.value])
    def mock_method_update(self, mock_id):
        method = request.form.get('mocks_definition_form_mock_method')
        call(
            lambda: mocks_controller.mock_method_update(mock_id, method),
            lambda: toast('Mock has been updated', category='success')
        )
        return redirect(url_for('mocks.mock', mock_id=mock_id))

    @expose('/<mock_id>/new', methods=[HTTPMethod.POST.value])
    def mock_response_new(self, mock_id):
        response = mocks_controller.mock_response_new(mock_id)
        return redirect(url_for('mocks.mock_response', mock_id=mock_id, response_id=response.id))

    @expose('<mock_id>/<response_id>/remove', methods=[HTTPMethod.POST.value])
    def mock_response_remove(self, mock_id, response_id):
        mocks_controller.mock_response_remove(mock_id, response_id)
        return redirect(url_for('mocks.mock', mock_id=mock_id))

    @expose('<mock_id>/<response_id>/order/up', methods=[HTTPMethod.POST.value])
    def mock_response_order_up(self, mock_id, response_id):
        mocks_controller.mock_response_order_up(mock_id, response_id)
        return redirect(url_for('mocks.mock', mock_id=mock_id))

    @expose('<mock_id>/<response_id>/order/down', methods=[HTTPMethod.POST.value])
    def mock_response_order_down(self, mock_id, response_id):
        mocks_controller.mock_response_order_down(mock_id, response_id)
        return redirect(url_for('mocks.mock', mock_id=mock_id))

    @expose('/<mock_id>/<response_id>/enable', methods=[HTTPMethod.POST.value])
    def mock_response_enable(self, mock_id, response_id):
        call(
            lambda: mocks_controller.mock_response_enable(mock_id, response_id),
            lambda: toast('Mock has been enabled', category='success')
        )
        return redirect(url_for('mocks.mock_response', mock_id=mock_id, response_id=response_id))

    @expose('/<mock_id>/<response_id>/disable', methods=[HTTPMethod.POST.value])
    def mock_response_disable(self, mock_id, response_id):
        call(
            lambda: mocks_controller.mock_response_disable(mock_id, response_id),
            lambda: toast('Mock has been disabled', category='success')
        )
        return redirect(url_for('mocks.mock_response', mock_id=mock_id, response_id=response_id))

    @expose('/<mock_id>/<response_id>/set', methods=[HTTPMethod.POST.value])
    def mock_response_set(self, mock_id, response_id):
        call(
            lambda: mocks_controller.mock_response_set(mock_id, response_id),
            lambda: toast('Mock has been set', category='success')
        )
        return url_for('mocks.mock_response', mock_id=mock_id, response_id=response_id)

    @expose('/<mock_id>/<response_id>/unset', methods=[HTTPMethod.POST.value])
    def mock_response_unset(self, mock_id, response_id):
        call(
            lambda: mocks_controller.mock_response_unset(mock_id, response_id),
            lambda: toast('Mock has been unset', category='success')
        )
        return url_for('mocks.mock_response', mock_id=mock_id, response_id=response_id)

    @expose('/<mock_id>/<response_id>/single_use', methods=[HTTPMethod.POST.value])
    def mock_response_single_use(self, mock_id, response_id):
        call(
            lambda: mocks_controller.mock_response_single_use(mock_id, response_id),
            lambda: toast('Mock has been enabled', category='success')
        )
        return redirect(url_for('mocks.mock_response', mock_id=mock_id, response_id=response_id))

    @expose('/<mock_id>/<response_id>/not_single_use', methods=[HTTPMethod.POST.value])
    def mock_response_not_single_use(self, mock_id, response_id):
        call(
            lambda: mocks_controller.mock_response_not_single_use(mock_id, response_id),
            lambda: toast('Mock has been disabled', category='success')
        )
        return redirect(url_for('mocks.mock_response', mock_id=mock_id, response_id=response_id))

    @expose('/<mock_id>/<response_id>/update', methods=[HTTPMethod.POST.value])
    def mock_response_update(self, mock_id, response_id):
        name = request.form.get('mocks_definition_response_form_name')
        call(
            lambda: mocks_controller.mock_response_update(mock_id, response_id, name),
            lambda: toast('Mock has been updated', category='success')
        )
        return redirect(url_for('mocks.mock_response', mock_id=mock_id, response_id=response_id))

    # mock response type
    @expose('/<mock_id>/<response_id>/update/type', methods=[HTTPMethod.POST.value])
    def mock_response_update_type(self, mock_id, response_id):
        type = request.form.get('mocks_definition_response_form_type')
        call(
            lambda: mocks_controller.mock_response_update_type(mock_id, response_id, type),
            lambda: toast('Mock has been updated', category='success')
        )
        return redirect(url_for('mocks.mock_response', mock_id=mock_id, response_id=response_id))

    # mock response delay
    @expose('/<mock_id>/<response_id>/update/delay/mode', methods=[HTTPMethod.POST.value])
    def mock_response_update_delay_mode(self, mock_id, response_id):
        delay_mode = request.form.get('mocks_definition_response_form_delay_mode')
        call(
            lambda: mocks_controller.mock_response_update_delay_mode(mock_id, response_id, delay_mode),
            lambda: toast('Mock has been updated', category='success')
        )
        return redirect(url_for('mocks.mock_response', mock_id=mock_id, response_id=response_id))

    @expose('/<mock_id>/<response_id>/update/delay/static', methods=[HTTPMethod.POST.value])
    def mock_response_update_delay_static(self, mock_id, response_id):
        delay = request.form.get('mocks_definition_response_form_input_delay_static')
        call(
            lambda: mocks_controller.mock_response_update_delay_static(mock_id, response_id, delay),
            lambda: toast('Mock has been updated', category='success')
        )
        return redirect(url_for('mocks.mock_response', mock_id=mock_id, response_id=response_id))

    @expose('/<mock_id>/<response_id>/update/delay/random', methods=[HTTPMethod.POST.value])
    def mock_response_update_delay_random(self, mock_id, response_id):
        delay_from = request.form.get('mocks_definition_response_form_input_delay_random_from')
        delay_to = request.form.get('mocks_definition_response_form_input_delay_random_to')
        call(
            lambda: mocks_controller.mock_response_update_delay_random(mock_id, response_id, delay_from, delay_to),
            lambda: toast('Mock has been updated', category='success')
        )
        return redirect(url_for('mocks.mock_response', mock_id=mock_id, response_id=response_id))

    # mock response status
    @expose('/<mock_id>/<response_id>/update/status', methods=[HTTPMethod.POST.value])
    def mock_response_update_status(self, mock_id, response_id):
        status = request.form.get('mocks_definition_response_form_status')
        call(
            lambda: mocks_controller.mock_response_update_status(mock_id, response_id, status),
            lambda: toast('Mock has been updated', category='success')
        )
        return redirect(url_for('mocks.mock_response', mock_id=mock_id, response_id=response_id))

    # mock response headers
    @expose('/<mock_id>/<response_id>/headers/<header_id>/remove', methods=[HTTPMethod.POST.value])
    def mock_response_headers_remove(self, mock_id, response_id, header_id):
        call(
            lambda: mocks_controller.mock_response_headers_remove(mock_id, response_id, header_id),
            lambda: toast('Header has been removed', category='success')
        )
        return redirect(url_for('mocks.mock_response', mock_id=mock_id, response_id=response_id))

    @expose('/<mock_id>/<response_id>/headers/new', methods=[HTTPMethod.POST.value])
    def mock_response_headers_new(self, mock_id, response_id):
        name = request.form.get('mocks_definition_response_form_input_response_header_name')
        value = request.form.get('mocks_definition_response_form_input_response_header_value')
        call(
            lambda: mocks_controller.mock_response_headers_new(mock_id, response_id, name, value),
            lambda: toast('Header has been added', category='success'))
        return redirect(url_for('mocks.mock_response', mock_id=mock_id, response_id=response_id))

    # mock response body
    @expose('/<mock_id>/<response_id>/update/body/json', methods=[HTTPMethod.POST.value])
    def mock_response_update_body_json(self, mock_id, response_id):
        body = request.form.get("body")
        call(
            lambda: mocks_controller.mock_response_update_body_json(mock_id, response_id, body),
            lambda: toast('Mock has been updated', category='success'))
        return url_for('mocks.mock_response', mock_id=mock_id, response_id=response_id)

    @expose('/<mock_id>/<response_id>/update/body/path', methods=[HTTPMethod.POST.value])
    def mock_response_update_body_path(self, mock_id, response_id):
        body_path = request.form.get("mocks_definition_response_form_body_path")
        call(
            lambda: mocks_controller.mock_response_update_body_path(mock_id, response_id, body_path),
            lambda: toast('Mock has been updated', category='success'))
        return redirect(url_for('mocks.mock_response', mock_id=mock_id, response_id=response_id))

    @expose('/<mock_id>/<response_id>/update/body/path/open', methods=[HTTPMethod.POST.value])
    def mock_response_update_body_path_open(self, mock_id, response_id):
        body_path = request.form.get("mocks_definition_response_form_body_path")
        call(
            lambda: mocks_controller.mock_response_update_body_path_open(mock_id, response_id, body_path),
            lambda: toast('File have been imported', category='success')
        )
        return url_for('mocks.mock_response', mock_id=mock_id, response_id=response_id)

    @expose('/<mock_id>/<response_id>/update/body/path/import', methods=[HTTPMethod.POST.value])
    def mock_response_update_body_path_import(self, mock_id, response_id):
        file = request.files.get('mocks_definition_response_form_file_body_path_import')
        call(
            lambda: mocks_controller.mock_response_update_body_path_import(mock_id, response_id, file),
            lambda: toast('File have been imported', category='success')
        )
        return url_for('mocks.mock_response', mock_id=mock_id, response_id=response_id)

    # mock response interceptors
    @expose('/<mock_id>/<response_id>/interceptors/<interceptor_id>/remove', methods=[HTTPMethod.POST.value])
    def mock_response_interceptors_remove(self, mock_id, response_id, interceptor_id):
        call(
            lambda: mocks_controller.mock_response_interceptors_remove(mock_id, response_id, interceptor_id),
            lambda: toast('Interceptor has been removed', category='success')
        )
        return redirect(url_for('mocks.mock_response', mock_id=mock_id, response_id=response_id))

    @expose('/<mock_id>/<response_id>/interceptors/new', methods=[HTTPMethod.POST.value])
    def mock_response_interceptors_new(self, mock_id, response_id):
        type = request.form.get('mocks_definition_response_form_input_response_interceptor_type')
        call(
            lambda: mocks_controller.mock_response_interceptors_new(mock_id, response_id, None, type),
            lambda: toast('Interceptor has been added', category='success'))
        return redirect(url_for('mocks.mock_response', mock_id=mock_id, response_id=response_id))

    @expose('/<mock_id>/<response_id>/interceptors/<interceptor_id>/edit', methods=[HTTPMethod.POST.value])
    def mock_response_interceptors_edit(self, mock_id, response_id, interceptor_id):
        return redirect(url_for('interceptors.interceptor', mock_id=mock_id, response_id=response_id,
                                interceptor_id=interceptor_id))
