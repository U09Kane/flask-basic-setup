from . import db, ma


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    animal_type = db.Column(db.String(20), nullable=False)

    # Pet's belonging to a person
    person_id = db.Column(
        db.Integer,
        db.ForeignKey('person.id'),
        nullable=False
    )


class PetSchema(ma.ModelSchema):
    class Meta:
        model = Pet
