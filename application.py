from flask import Flask
from flask_restful import Api
from db import db
from resources.add_user import AddUser
from resources.view_user import ViewUser

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://demo_user:123456@localhost:5432/inoc_tutorial'
api = Api(application)



db.init_app(application)
with application.app_context():
        db.create_all()


api.add_resource(AddUser, '/addUser')
api.add_resource(ViewUser, '/viewUser/<int:id>')

if __name__ == '__main__':
    application.run(host="127.0.0.1", debug=True, port=5010)
