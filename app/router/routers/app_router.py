from flask import render_template


class AppRouter(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app

    def init_router(self):
        @self.flask_app.route("/favicon.ico")
        def favicon():
            return render_template('404.html'), 404

        @self.flask_app.errorhandler(404)
        def page_not_found(e):
            return render_template('404.html'), 404

        # @self.flask_app.errorhandler(Exception)
        # def server_error(e):
        #     response = {"message": str(e)}
        #     return response_dumps(self.flask_app, response, status=500)
