from admin.extensions.init_sqlalchemy import db


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64), unique=True)

    def __str__(self):
        return "{}".format(self.name)