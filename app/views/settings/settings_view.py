from flask import redirect, url_for, request
from flask_admin import BaseView, expose

from app.controllers import settings_controller
from app.models.models.http_method import HTTPMethod
from app.utils.utils import call, toast, call_with_result


class View(BaseView):

    @expose('/')
    def index(self):
        settings = settings_controller.settings()
        return redirect(url_for('settings.proxy', proxy_id=settings.proxy.id))

    @expose('/proxy/<proxy_id>')
    def proxy(self, proxy_id):
        proxies = settings_controller.proxies()
        proxy = settings_controller.proxy(proxy_id)
        return self.render('admin/settings/settings.html', proxies=proxies, proxy=proxy)

    @expose('proxy/new', methods=[HTTPMethod.POST.value])
    def proxy_new(self):
        proxy = settings_controller.proxy_new()
        return redirect(url_for('settings.proxy', proxy_id=proxy.id))

    @expose('proxy/import', methods=[HTTPMethod.POST.value])
    def proxy_import_proxies(self):
        file = request.files.get('settings_proxy_form_file_import')
        call(
            lambda: settings_controller.proxy_import_proxies(file),
            lambda: toast('Proxies have been imported', category='success')
        )
        return url_for('settings.index')

    @expose('proxy/export', methods=[HTTPMethod.POST.value])
    def proxy_export_proxies(self):
        return call_with_result(
            lambda: settings_controller.proxy_export_proxies(),
            lambda: toast('Proxies have been exported', category='success')
        )

    @expose('proxy/<proxy_id>/remove', methods=[HTTPMethod.POST.value])
    def proxy_remove(self, proxy_id):
        settings_controller.proxy_remove(proxy_id)
        return redirect(url_for('settings.proxy', proxy_id=proxy_id))

    @expose('proxy/<proxy_id>/export', methods=[HTTPMethod.POST.value])
    def proxy_export_proxy(self, proxy_id):
        return call_with_result(
            lambda: settings_controller.proxy_export_proxy(proxy_id),
            lambda: toast('Proxy has been exported', category='success')
        )

    @expose('proxy/<proxy_id>/select', methods=[HTTPMethod.POST.value])
    def proxy_select(self, proxy_id):
        call(
            lambda: settings_controller.proxy_select(proxy_id, True),
            lambda: toast('Proxy has been selected', category='success')
        )
        return url_for('settings.proxy', proxy_id=proxy_id)

    @expose('proxy/<proxy_id>/enable', methods=[HTTPMethod.POST.value])
    def proxy_enable(self, proxy_id):
        call(
            lambda: settings_controller.proxy_enable(proxy_id),
            lambda: toast('Proxy has been enabled', category='success')
        )
        return url_for('settings.proxy', proxy_id=proxy_id)

    @expose('proxy/<proxy_id>/disable', methods=[HTTPMethod.POST.value])
    def proxy_disable(self, proxy_id):
        call(
            lambda: settings_controller.proxy_disable(proxy_id),
            lambda: toast('Proxy has been disabled', category='success')
        )
        return url_for('settings.proxy', proxy_id=proxy_id)

    @expose('proxy/<proxy_id>/templating/enable', methods=[HTTPMethod.POST.value])
    def proxy_templating_enable(self, proxy_id):
        call(
            lambda: settings_controller.proxy_templating_enable(proxy_id),
            lambda: toast('Proxy templating has been enabled', category='success')
        )
        return url_for('settings.proxy', proxy_id=proxy_id)

    @expose('proxy/<proxy_id>/templating/disable', methods=[HTTPMethod.POST.value])
    def proxy_templating_disable(self, proxy_id):
        call(
            lambda: settings_controller.proxy_templating_disable(proxy_id),
            lambda: toast('Proxy templating has been disabled', category='success')
        )
        return url_for('settings.proxy', proxy_id=proxy_id)

    @expose('proxy/<proxy_id>', methods=[HTTPMethod.POST.value])
    def proxy_update(self, proxy_id):
        name = request.form.get('settings_form_input_proxy_name')
        path = request.form.get('settings_form_input_proxy_path')
        call(
            lambda: settings_controller.proxy_update(proxy_id, name, path),
            lambda: toast('Proxy has been updated', category='success')
        )
        return redirect(url_for('settings.proxy', proxy_id=proxy_id))

    @expose('proxy/<proxy_id>/request/headers/<header_id>/remove', methods=[HTTPMethod.POST.value])
    def proxy_request_headers_remove(self, proxy_id, header_id):
        call(
            lambda: settings_controller.proxy_request_headers_remove(proxy_id, header_id),
            lambda: toast('Header has been removed', category='success')
        )
        return redirect(url_for('settings.proxy', proxy_id=proxy_id))

    @expose('proxy/<proxy_id>/request/headers/new', methods=[HTTPMethod.POST.value])
    def proxy_request_headers_new(self, proxy_id):
        name = request.form.get('settings_form_input_request_header_name')
        value = request.form.get('settings_form_input_request_header_value')
        call(
            lambda: settings_controller.proxy_request_headers_new(proxy_id, name, value),
            lambda: toast('Header has been added', category='success')
        )
        return redirect(url_for('settings.proxy', proxy_id=proxy_id))

    @expose('proxy/<proxy_id>/response/headers/<header_id>/remove', methods=[HTTPMethod.POST.value])
    def proxy_response_headers_remove(self, proxy_id, header_id):
        call(
            lambda: settings_controller.proxy_response_headers_remove(proxy_id, header_id),
            lambda: toast('Header has been removed', category='success')
        )
        return redirect(url_for('settings.proxy', proxy_id=proxy_id))

    @expose('proxy/<proxy_id>/response/headers/new', methods=[HTTPMethod.POST.value])
    def proxy_response_headers_new(self, proxy_id):
        name = request.form.get('settings_form_input_response_header_name')
        value = request.form.get('settings_form_input_response_header_value')
        call(
            lambda: settings_controller.proxy_response_headers_new(proxy_id, name, value),
            lambda: toast('Header has been added', category='success'))
        return redirect(url_for('settings.proxy', proxy_id=proxy_id))
