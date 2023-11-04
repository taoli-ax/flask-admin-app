from flask import Flask
from .init_flask_admin import init_flask_admin
from .init_sqlalchemy import init_sqlalchemy
from .init_flask_migrate import init_migrate
from .init_babel import init_flask_babel


def init_plugs(app: Flask):
    init_flask_admin(app)
    init_sqlalchemy(app)
    init_migrate(app)
    init_flask_babel(app)
