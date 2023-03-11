from flask_admin import BaseView, expose

from app.controllers import templating_controller


class View(BaseView):
    def is_visible(self):
        return True

    @expose('/')
    def index(self):
        environment = templating_controller.environment()
        return self.render('admin/templating/templating.html', environment=environment)
