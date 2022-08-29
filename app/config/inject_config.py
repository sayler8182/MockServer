from app.utils.utils import conditional_value


class InjectConfig(object):
    def __init__(self, flask_app):
        self.flask_app = flask_app

    def init_app(self):
        @self.flask_app.context_processor
        def inject_data():
            return {
                "conditional_value": conditional_value
            }
