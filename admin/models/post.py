import arrow
from sqlalchemy_utils import ColorType, ArrowType, UUIDType

from admin.extensions.init_sqlalchemy import db
from admin.models.user import User

# Create M2M table
post_tags_table = db.Table('post_tags', db.Model.metadata,
                           db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                           db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                           )


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date)

    # some sqlalchemy_utils data types (see https://sqlalchemy-utils.readthedocs.io/)
    background_color = db.Column(ColorType)
    created_at = db.Column(ArrowType, default=arrow.utcnow())
    user_id = db.Column(UUIDType(binary=False), db.ForeignKey(User.id))

    user = db.relationship(User, foreign_keys=[user_id], backref='posts')
    tags = db.relationship('Tag', secondary=post_tags_table)

    def __str__(self):
        return "{}".format(self.title)


