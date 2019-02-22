from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

CONFIG = [
    {'id': 123, 'fixed_membership_fee': True, 'fixed_membership_amount': 15000}, 
    {'id': 321, 'fixed_membership_fee': False, 'fixed_membership_amount': 25000},
    ]

class Hello(Resource):
    def get(self):
        return {'msg': 'Hello World!'}

class ConfigList(Resource):
    def get(self):
        return {'configs': CONFIG}

class Config(Resource):
    def get(self, client_id):
        config = [item for item in CONFIG if item.get('id') == int(client_id)]
        if len(config) == 0:
            return {'msg': 'User not found'}, 404
        else:
            return {'config': config[0]}

api.add_resource(Hello, '/')
api.add_resource(ConfigList, '/config')
api.add_resource(Config, '/config/<client_id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')