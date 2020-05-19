from models import Person
from db import session
from pd_return import req_get_id

from flask_restplus import reqparse
from flask_restplus import abort
from flask_restplus import Resource
from flask_restplus import fields
from flask_restplus import marshal_with

# Модель, по которой будут формироваться данные в декораторе marshal_with
person_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'surname': fields.String,
    'html': fields.String(),
    'uri': fields.Url('person', absolute=True)
}

# Ввод функции-проверки корректности ввода данных

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('surname', type=str)
parser.add_argument('html_code', type=str)

# Класс для работы с ресурсами


class PersonResource(Resource):

    # реализация get запроса к ресурсу
    @marshal_with(person_fields)
    def get(self):
        person = session.query(Person).all()
        if not person:
            abort(404, message="Nothing to see here")
        return person, 200

    # реализация post запроса
    """
    В качестве одного из доп.заданий была реализация взаимодействия pandas с postgreSQL.
    Я решил реализвать функцию создания в БД через pandas html-кода страницы, на которой будет отражена запись.
    Способ описан в модулях config, postgre_to_pd, pd-return
    """
    @marshal_with(person_fields)
    def post(self):
        parsed_args = parser.parse_args()
        person = Person(name=parsed_args['name'], surname=parsed_args['surname'])
        session.add(person)
        session.commit()
        person_change = session.query(Person).filter(Person.id == person.id).first()
        person_change.html = req_get_id(person.id)
        session.add(person_change)
        session.commit()
        return person_change, 201

# класс обработки запросов к экземплярам


class PersonInstance(Resource):

    # GET запрос к конкретной записи
    @marshal_with(person_fields)
    def get(self, id):
        person = session.query(Person).filter(Person.id == id).first()
        if not person:
            abort(404, message="Person {} doesn't exist".format(id))
        return person, 200

    # PUT запрос
    @marshal_with(person_fields)
    def put(self, id):
        parsed_args = parser.parse_args()
        person = session.query(Person).filter(Person.id == id).first()
        person.name = parsed_args['name']
        person.surname = parsed_args['surname']
        session.add(person)
        session.commit()
        return person, 200

    # Удаление записи
    def delete(self, id):
        person = session.query(Person).filter(Person.id == id).first()
        if not person:
            abort(404, message="Person {} doesn't exist".format(id))
        session.delete(person)
        session.commit()
        return {}, 204

