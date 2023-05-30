from flask_restful import Resource
from models.users import Users
from flask_jwt import jwt_required, current_identity
class ViewUser(Resource):
    @jwt_required()
    def get(self, id):

        user: Users = Users.find_user(id=id)
        if current_identity.user_name=='dimuthuh':
            return 'Unauthorized', 401
        if user:
            return {
                'user_name': user.user_name,
                'emp_name': user.emp_name,
            }
        return 'User not found', 404
