from flask import Flask
from flask_restplus import Api
from resources import PersonResource
from resources import PersonInstance

# Создание приложения и формирования страницы с методами API в swaggerUI

app = Flask(__name__)
api = Api(app=app,
          version="1.0",
          title="Записи людей",
          description="Программа заносящая людей в БД и выводящая инфомацию о них")

# добваление конечных точек для каждого класса
api.add_resource(PersonResource, '/persons', endpoint='persons')
api.add_resource(PersonInstance, '/persons/<string:id>', endpoint='person')


if __name__ == '__main__':
    # Запуск приложение в режиме дебага
    app.run(host='0.0.0.0')
