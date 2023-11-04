import os

from flask import Flask

from .common.scripts import init_scripts
from .config import ConfigBase
from .extensions import init_plugs
from .views import init_blueprints


def create_app():
    app = Flask(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    app.config.from_object(ConfigBase)

    # register plugins
    init_plugs(app)

    # register blueprints
    init_blueprints(app)

    # register scripts
    init_scripts(app)

    return app
