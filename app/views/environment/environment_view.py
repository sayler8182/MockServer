from flask import redirect, url_for, request
from flask_admin import BaseView, expose

from app.controllers import environment_controller
from app.models.models.http_method import HTTPMethod
from app.utils.utils import call, toast, call_with_result


class View(BaseView):
    @expose('/')
    def index(self):
        environment = environment_controller.environment()
        return self.render('admin/environment/environment.html', environment=environment)

    @expose('/<item_id>')
    def environment(self, item_id):
        environment = environment_controller.environment()
        item = environment_controller.environment_item(item_id)
        return self.render('admin/environment/environment.html', environment=environment, item=item)

    @expose('/end_edit')
    def environment_end_edit(self):
        return url_for('environment.index')

    @expose('/new', methods=[HTTPMethod.POST.value])
    def environment_new(self):
        name = request.form.get('environment_form_input_name')
        value = request.form.get('environment_form_input_value')
        call(
            lambda: environment_controller.environment_new(name, value),
            lambda: toast('Environment has been added', category='success')
        )
        return redirect(url_for('environment.index'))

    @expose('/<item_id>/update', methods=[HTTPMethod.POST.value])
    def environment_update(self, item_id):
        name = request.form.get('environment_form_input_name')
        value = request.form.get('environment_form_input_value')
        call(
            lambda: environment_controller.environment_update(item_id, name, value),
            lambda: toast('Environment has been updated', category='success')
        )
        return redirect(url_for('environment.index'))

    @expose('/import', methods=[HTTPMethod.POST.value])
    def environment_import_environment(self):
        file = request.files.get('environment_form_file_import')
        call(
            lambda: environment_controller.environment_import_environment(file),
            lambda: toast('Environment have been imported', category='success')
        )
        return url_for('environment.index')

    @expose('/export', methods=[HTTPMethod.POST.value])
    def environment_export_environment(self):
        return call_with_result(
            lambda: environment_controller.environment_export_environment(),
            lambda: toast('Environment have been exported', category='success')
        )

    @expose('/remove', methods=[HTTPMethod.POST.value])
    def environment_remove_all(self):
        environment_controller.environment_remove_all()
        toast('Environment have been removed', category='success')
        return redirect(url_for('environment.index'))

    @expose('/<item_id>/remove', methods=[HTTPMethod.POST.value])
    def environment_remove(self, item_id):
        environment_controller.environment_remove(item_id)
        toast('Environment has been removed', category='success')
        return redirect(url_for('environment.index'))
