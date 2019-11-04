from . import db, ma
from .pet import Pet


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    pets = db.relationship(Pet, backref='person', lazy='joined')


class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person
