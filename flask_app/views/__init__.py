from flask_restplus import Api
from flask import Blueprint

from .persons import NS as persons_NS
from .pets import NS as pets_NS


def init_app(app):
    api = Api(app, prefix='/api')
    api.add_namespace(persons_NS)
    api.add_namespace(pets_NS)
