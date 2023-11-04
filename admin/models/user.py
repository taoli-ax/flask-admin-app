
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import sql, cast
import uuid

from sqlalchemy_utils import ChoiceType, EmailType, UUIDType, URLType, CurrencyType
from sqlalchemy_utils import ColorType, ArrowType, IPAddressType, TimezoneType
import arrow
import enum

from admin.extensions.init_sqlalchemy import db

AVAILABLE_USER_TYPES = [
    (u'admin', u'Admin'),
    (u'content-writer', u'Content writer'),
    (u'editor', u'Editor'),
    (u'regular-user', u'Regular user'),
]


class EnumChoices(enum.Enum):
    first = 1
    second = 2


# Create models
class User(db.Model):
    id = db.Column(UUIDType(binary=False), default=uuid.uuid4, primary_key=True)

    # use a regular string field, for which we can specify a list of available choices later on
    type = db.Column(db.String(100))

    # fixed choices can be handled in a number of different ways:
    enum_choice_field = db.Column(db.Enum(EnumChoices), nullable=True)
    sqla_utils_choice_field = db.Column(ChoiceType(AVAILABLE_USER_TYPES), nullable=True)
    sqla_utils_enum_choice_field = db.Column(ChoiceType(EnumChoices, impl=db.Integer()), nullable=True)

    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))

    # some sqlalchemy_utils data types (see https://sqlalchemy-utils.readthedocs.io/)
    email = db.Column(EmailType, unique=True, nullable=False)
    website = db.Column(URLType)
    ip_address = db.Column(IPAddressType)
    currency = db.Column(CurrencyType, nullable=True, default=None)
    timezone = db.Column(TimezoneType(backend='pytz'))

    dialling_code = db.Column(db.Integer())
    local_phone_number = db.Column(db.String(10))

    featured_post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    featured_post = db.relationship('Post', foreign_keys=[featured_post_id])

    @hybrid_property
    def phone_number(self):
        if self.dialling_code and self.local_phone_number:
            number = str(self.local_phone_number)
            return "+{} ({}) {} {} {}".format(self.dialling_code, number[0], number[1:3], number[3:6], number[6::])
        return

    @phone_number.expression
    def phone_number(cls):
        return sql.operators.ColumnOperators.concat(cast(cls.dialling_code, db.String), cls.local_phone_number)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)

    def __repr__(self):
        return "{}: {}".format(self.id, self.__str__())





