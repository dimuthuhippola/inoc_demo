from flask_restful import Resource
from flask import request


class FirstResource(Resource):
    def get(self, name):
        return f'Hello- {name}'

    def post(self, name):

        data = request.get_json()
        print(data)
        return 'Updated', 201
