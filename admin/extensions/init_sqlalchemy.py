import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.query import Query as BaseQuery
from flask_marshmallow import Marshmallow

class Query(BaseQuery):
    def soft_delete(self):
        return self.update({'delete_at': datetime.datetime.now()})

    def logic_all(self):
        return self.filter_by(delete_at=None).all()

    def all_json(self):
        return

    def layui_paginate(self):
        return

    def layui_paginate_json(self):
        return

    def layui_paginate_db_json(self):
        return


db = SQLAlchemy()
ma = Marshmallow()

def init_sqlalchemy(app):
    db.init_app(app)
    with app.app_context():
        try:
            db.engine.connect()
        except Exception as e:
            exit(f"数据库连接失败：{e}")
