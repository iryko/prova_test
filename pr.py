from flask import Flask
from flask_restful import Api, Resource, reqparse
from http.client import NOT_FOUND, NO_CONTENT, OK, CREATED

app = Flask(__name__)
api = Api(app)

def non_empty_str(val, name):
    if not str(val).strip():
        raise ValueError("The argument {0} is empty".format(name))
    else:
        return str(val)


contacts = {
"Iryna_Korda":{
    "nome":"Iryna",
    "cognome":"Korda"
    "telefono":"1234567"
    },
"Oleg_Dykyi":{
    "nome":"Oleg",
    "cognome":"Dykyi",
    "telefono": "01928374"
    },
"Maria_Mariani":{
    "nome":"Maria",
    "cognome":"Mariani",
    "telefono":"9876543"
    }
}

class Contacts(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome', type=str, required=True)
        parser.add_argument('cognome', type=str, required=True)
        parser.add_argument('telefono', type=int, required=True)
        args = parser.parse_args()

        contact_id = args["nome"]+ "_" + args["cognome"]

        contacts["contact_id"] = {
            "nome": args["nome"],
            "cognome": args["cognome"],
            "telefono": args["telefono"]
        }
        return contacts[contact_id], CREATED


    def get(self):
        contact_id = nome+ "_"+ cognome
        if contact_id in contacts:
            return contact_id, OK
    else:
        return NOT_FOUND

class Contact(Resource):
    def get(self, nome, cognome):
        contact_id = nome + "_" + cognome
        if contact_id in contacts:
             return contacts[contact_id], OK
        else:
            return NOT_FOUND

    def delete(self, nome, cognome):
        contact_id = nome + "_" + cognome
        if contact_id in contacts:
            del contacts[contact_id]
            return None, NO_CONTENT
        else:
            return None, NOT_FOUND

api.add_resource(Contacts, "/contacts/")
api.add_resource(Contact, "/contacts/<name>/<surname>")
