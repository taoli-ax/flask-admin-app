from flask import Blueprint

bp = Blueprint('passport', __name__, url_prefix='/passport')


@bp.get('/login')
def login():
    return 'login'
