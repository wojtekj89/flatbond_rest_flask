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

api.add_resource(Hello, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')