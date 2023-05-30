from flask_restful import Resource
from models.users import Users
from flask import request
from werkzeug.security import generate_password_hash


class AddUser(Resource):

    def post(self):
        user_data = request.get_json()
        user: Users = Users.find_by_username(username=user_data.get('user_name'))
        if user:
            return 'User already exists', 400

        hashed_password = generate_password_hash(user_data.get('pass_word'), method='pbkdf2:sha256', salt_length=8)

        user = Users(user_name=user_data.get('user_name'),
                     pass_word=hashed_password,
                     emp_name=user_data.get('emp_name'))

        user.save_user()

        return 'user added', 201

