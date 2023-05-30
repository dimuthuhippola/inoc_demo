from flask import Flask
from flask_restful import Api
from db import db
from flask_jwt import JWT
from security import authenticate, identity
from resources.add_user import AddUser
from resources.view_user import ViewUser
import datetime as dt

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://demo_user:123456@localhost:5432/inoc_tutorial'
application.config['JWT_EXPIRATION_DELTA'] = dt.timedelta(days=7)
api = Api(application)

application.secret_key = "mysecretkey"


jwt = JWT(app=application, authentication_handler=authenticate, identity_handler=identity)


db.init_app(application)
with application.app_context():
    db.create_all()

api.add_resource(AddUser, '/addUser')
api.add_resource(ViewUser, '/viewUser/<int:id>')

if __name__ == '__main__':
    application.run(host="127.0.0.1", debug=True, port=5010)
