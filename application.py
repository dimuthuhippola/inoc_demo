from flask import Flask
from flask_restful import Api

from resources.first_resource import FirstResource

application = Flask(__name__)

api = Api(application)

api.add_resource(FirstResource, '/firstResource/<string:name>')

@application.route('/')
def home():
    return {
        'Key': 'key',
        'value': 'value'
    }


if __name__ == '__main__':
    application.run(host="127.0.0.1", debug=True, port=5010)
