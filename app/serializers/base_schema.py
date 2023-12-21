from flask_marshmallow import Marshmallow

ma = Marshmallow()


class baseMarshmallow(ma.Schema):
    __abstract__ = True
