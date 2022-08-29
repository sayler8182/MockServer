from flask_admin import AdminIndexView, expose


class View(AdminIndexView):

    @expose('/')
    def index(self):
        return self.render('admin/home.html')
