from admin.extensions.init_sqlalchemy import db


class Tree(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    # recursive relationship
    parent_id = db.Column(db.Integer, db.ForeignKey('tree.id'))
    parent = db.relationship('Tree', remote_side=[id], backref='children')

    def __str__(self):
        return "{}".format(self.name)