from enum import Enum

from flask import url_for, redirect, request, flash
from flask_admin import BaseView, expose

from app.controllers import logs_controller
from app.models.models.http_method import HTTPMethod
from app.utils.utils import toast


class ViewMode(Enum):
    mock = 'mock'
    logs = 'mock'


class View(BaseView):
    def is_visible(self):
        return True

    @expose('/')
    @expose('/<log_id>')
    def index(self, log_id = None):
        logs = logs_controller.logs()
        log = logs_controller.log(log_id)
        return self.render('admin/logs/logs.html', logs=logs, log=log)

    @expose('/<mock_id>/logs/back')
    def logs_back(self, mock_id):
        return redirect(url_for('mocks.mock', mock_id=mock_id))

    @expose('/<mock_id>/logs')
    @expose('/<mock_id>/logs/<log_id>')
    def logs(self, mock_id, log_id=None):
        logs = logs_controller.logs_for_mock(mock_id)
        log = logs_controller.log(log_id)
        return self.render('admin/logs/logs.html', mock_id=mock_id, logs=logs, log=log)

    # logs
    @expose('/remove', methods=[HTTPMethod.POST.value])
    def logs_remove_all(self):
        mock_id = request.form.get('logs_form_remove_all_mock_id')
        logs_controller.logs_remove_all(mock_id)
        toast('Mocks have been removed', category='success')
        return self.__logs_list_redirect(mock_id)

    @expose('/<log_id>/details', methods=[HTTPMethod.POST.value])
    def log_details(self, log_id):
        mock_id = request.form.get('logs_form_details_mock_id')
        return self.__logs_list_redirect(mock_id, log_id)

    @expose('/<log_id>/remove', methods=[HTTPMethod.POST.value])
    def log_remove(self, log_id):
        mock_id = request.form.get('logs_form_remove_mock_id')
        logs_controller.log_remove(mock_id, log_id)
        return self.__logs_list_redirect(mock_id)

    def __logs_list_redirect(self, mock_id, log_id=None):
        if mock_id:
            return redirect(url_for('logs.logs', mock_id=mock_id, log_id=log_id))
        return redirect(url_for('logs.index', log_id=log_id))
