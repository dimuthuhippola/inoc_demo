from flask_restful import Resource
from models.users import Users
from flask import request


class AddUser(Resource):

    def post(self):
        user_data = request.get_json()
        user = Users(user_name=user_data.get('user_name'),
                     pass_word=user_data.get('pass_word'),
                     emp_name=user_data.get('emp_name'))

        user.save_user()

        return 'user added', 201

