from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
import validators

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('rent', type=int)
parser.add_argument('membership_fee', type=int)
parser.add_argument('postcode', type=str)
parser.add_argument('client_id', type=int)

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
            return {'config': config[0]}, 200

class Flatbond(Resource):
    def post(self):
        args = parser.parse_args()
        rent = args.get('rent')
        membership_fee = args.get('membership_fee')
        client_id = args.get('client_id')
        postcode = args.get('postcode')

        if any([not rent, not membership_fee, not client_id, not postcode]):
            return {'msg': 'Invalid request'}, 400

        postcode_valid = validators.validate_postcode(str(postcode))

        try:
            user_config = next(item for item in CONFIG if item.get('id') == client_id)
        except StopIteration:
            user_config = None

        membership_fee_valid = validators.validate_fee(user_config, rent, membership_fee)
        rent_valid = validators.validate_rent(rent)

        if any([not membership_fee_valid, not postcode_valid, not rent_valid]):
            if not membership_fee_valid:
                return {'msg': 'Invalid fee'}, 403

            elif not postcode_valid:
                return {'msg': 'Invalid postcode'}, 403
            
            else:
                return {'msg': "Invalid rent amount"}, 403
        
        return {'status': 'OK', 'flatbond': args}

api.add_resource(Hello, '/')
api.add_resource(ConfigList, '/config')
api.add_resource(Config, '/config/<client_id>')
api.add_resource(Flatbond, '/flatbond')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')