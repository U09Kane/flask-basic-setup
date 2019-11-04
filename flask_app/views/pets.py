
from flask_restplus import Resource, Namespace

from ..models import db
from ..models.pet import Pet, PetSchema
from ..models.person import Person


NS = Namespace('pets')


@NS.route('/<int:person_id>/pets')
class PetAPI(Resource):
    """The Pet's belonging to a person"""

    def get(self, person_id):
        schema = PetSchema(many=True)

        pets = Pet.query.filter(Pet.person_id == person_id).all()
        res = schema.dump(pets)
        return res

    def post(self, person_id):
        schema = PetSchema()
        person = Person.query.filter(Person.id == person_id).first()

        if person:
            pet = Pet(**NS.payload, person=person)
            db.session.add(pet)
            db.session.commit()
            return schema.jsonify(pet)
        else:
            return {'error': 'no such person found'}
