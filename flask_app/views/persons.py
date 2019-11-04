from flask_restplus import Resource, Namespace

from ..models import db
from ..models.person import Person, PersonSchema


NS = Namespace('persons')


@NS.route('/')
class PersonAPI(Resource):
    """ A person object representing a real person"""

    many = PersonSchema(many=True)

    def get(self):
        """Get a List of all Person(s)"""
        schema = PersonSchema(many=True)

        persons = Person.query.all()
        res = schema.dump(persons)
        return res

    def post(self):
        """Adds a new person to the db"""
        schema = PersonSchema()

        person = Person(**NS.payload)
        db.session.add(person)
        db.session.commit()
        return schema.jsonify(person)
