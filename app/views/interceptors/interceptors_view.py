from flask import url_for, redirect, request
from flask_admin import BaseView, expose

from app.controllers import interceptors_controller
from app.models.models.http_method import HTTPMethod
from app.utils.utils import toast, call


class View(BaseView):
    def is_visible(self):
        return False

    @expose('/')
    def index(self):
        return self.render('admin/interceptors/interceptors.html')

    @expose('/<mock_id>/<response_id>/back')
    def interceptor_back(self, mock_id, response_id):
        return redirect(url_for('mocks.mock_response', mock_id=mock_id, response_id=response_id))

    @expose('/<mock_id>/<response_id>/<interceptor_id>')
    def interceptor(self, mock_id, response_id, interceptor_id):
        interceptor = interceptors_controller.interceptor(mock_id, response_id, interceptor_id)
        interceptor_configuration_example = interceptors_controller.interceptor_configuration_example(interceptor.type)
        return self.render('admin/interceptors/interceptors.html', mock_id=mock_id, response_id=response_id,
                           interceptor=interceptor, interceptor_configuration_example=interceptor_configuration_example)

    # interceptor
    @expose('/<mock_id>/<response_id>/<interceptor_id>/update', methods=[HTTPMethod.POST.value])
    def interceptor_update(self, mock_id, response_id, interceptor_id):
        name = request.form.get('interceptors_definition_form_name')
        call(
            lambda: interceptors_controller.interceptor_update(mock_id, response_id, interceptor_id, name),
            lambda: toast('Interceptors has been updated', category='success')
        )
        return redirect(url_for('interceptors.interceptor', mock_id=mock_id, response_id=response_id,
                                interceptor_id=interceptor_id))

    @expose('/<mock_id>/<response_id>/<interceptor_id>/enable', methods=[HTTPMethod.POST.value])
    def interceptor_enable(self, mock_id, response_id, interceptor_id):
        call(
            lambda: interceptors_controller.interceptor_enable(mock_id, response_id, interceptor_id),
            lambda: toast('Interceptor has been enabled', category='success')
        )
        return url_for('interceptors.interceptor', mock_id=mock_id, response_id=response_id, interceptor_id=interceptor_id)

    @expose('/<mock_id>/<response_id>/<interceptor_id>/disable', methods=[HTTPMethod.POST.value])
    def interceptor_disable(self, mock_id, response_id, interceptor_id):
        call(
            lambda: interceptors_controller.interceptor_disable(mock_id, response_id, interceptor_id),
            lambda: toast('Interceptor has been disabled', category='success')
        )
        return url_for('interceptors.interceptor', mock_id=mock_id, response_id=response_id, interceptor_id=interceptor_id)

    @expose('/<mock_id>/<response_id>/<interceptor_id>/configuration', methods=[HTTPMethod.POST.value])
    def interceptor_update_configuration(self, mock_id, response_id, interceptor_id):
        configuration = request.form.get("configuration")
        call(
            lambda: interceptors_controller.interceptor_update_configuration(mock_id, response_id, interceptor_id,
                                                                             configuration),
            lambda: toast('Interceptor has been updated', category='success'))
        return url_for('interceptors.interceptor', mock_id=mock_id, response_id=response_id, interceptor_id=interceptor_id)
