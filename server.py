#!/usr/bin/env python

from flask import Flask
from flask_restful import Api
from flask_restful import Resource
from flask_restful import reqparse
from http.client import NO_CONTENT
from http.client import NOT_FOUND
from http.client import CREATED
from http.client import OK

app = Flask(__name__)
api = Api(app)

contacts = {
    "gigio_gigione": {
        "telephone": "057409098",
        "name": "gigio",
        "surname": "gigione"
    },
    "gigio1_gigione1": {
        "telephone": "057409098",
        "name": "gigio1",
        "surname": "gigione1"
    }
}


def non_empty_str(val, name):
    if not str(val).strip():
        raise ValueError('The argument {} is empty'.format(name))
    return str(val)


class Contacts(Resource):
    """Contacts endpoints"""

    def get(self):
        return list(contacts.values()), OK

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=non_empty_str, required=True)
        parser.add_argument('surname', type=non_empty_str, required=True)
        parser.add_argument('telephone', type=non_empty_str, required=True)
        args = parser.parse_args(strict=True)

        contact_id = args['name'] + "_" + args['surname']
        contacts[contact_id] = {
            'name': args['name'],
            'surname': args['surname'],
            'telephone': args['telephone'],
        }
        return contacts[contact_id], CREATED


class Contact(Resource):
    """Contact endpoints"""

    def delete(self, name, surname):
        contact_id = name + "_" + surname
        if contact_id in contacts:
            del contacts[contact_id]
            return None, NO_CONTENT
        else:
            return None, NOT_FOUND


api.add_resource(Contacts, '/contacts/')
api.add_resource(Contact, '/contact/<name>/<surname>')
