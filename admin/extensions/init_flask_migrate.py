from flask_migrate import Migrate
from admin.extensions.init_sqlalchemy import db
from admin.models import *

migrate = Migrate()


def init_migrate(app):
    migrate.init_app(app, db)
