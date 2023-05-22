from flask_restful import Resource
from models.users import Users
class ViewUser(Resource):
    def get(self, id):
        user: Users = Users.find_user(id=id)
        if user:
            return {
                'user_name': user.user_name,
                'emp_name': user.emp_name,
            }
        return 'User not found', 404
