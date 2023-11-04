from flask import Blueprint, Flask
from .passport import bp as passport_bp
from .index import bp as index_bp

bp = Blueprint('system', __name__, url_prefix='/system')


def init_blueprints(app: Flask):
    bp.register_blueprint(passport_bp)
    bp.register_blueprint(index_bp)
    app.register_blueprint(bp)