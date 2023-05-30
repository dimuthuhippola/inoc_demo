from models.users import Users
from werkzeug.security import check_password_hash


def authenticate(username, password):
    user: Users = Users.find_by_username(username=username)
    if user and check_password_hash(user.pass_word, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return Users.find_by_id(user_id=user_id)
