from flask_admin import Admin

admin = Admin(name='Example: SQLAlchemy', template_mode='bootstrap4')


def init_flask_admin(app):
    admin.init_app(app)
