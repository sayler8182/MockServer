from app.config.database_config import db


class SettingsProxyDb(db.Model):
    id = db.Column(db.String, primary_key=True, nullable=False)
    is_selected = db.Column(db.Boolean, default=False, nullable=False)
    is_enabled = db.Column(db.Boolean, default=False, nullable=False)
    name = db.Column(db.String, nullable=True)
    path = db.Column(db.String, nullable=True)
    delay_mode = db.Column(db.String, nullable=False)
    delay_from = db.Column(db.Integer, default=0, nullable=False)
    delay_to = db.Column(db.Integer, default=0, nullable=False)
    delay = db.Column(db.Integer, default=0, nullable=False)

    def __repr__(self):
        return 'SettingsProxyDb:' \
               f' id: {self.id} ' \
               f' is_selected: {self.is_selected}' \
               f' is_enabled: {self.is_enabled}' \
               f' name: {self.name}' \
               f' path: {self.path}' \
               f' delay_mode: {self.delay_mode}' \
               f' delay_from: {self.delay_from}' \
               f' delay_to: {self.delay_to}' \
               f' delay: {self.delay}'
